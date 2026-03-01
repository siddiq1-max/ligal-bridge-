from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Case, Enquiry
from users.models import CustomUser

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        messages.warning(request, "Access denied.")
        return redirect('home')
    
    cases = Case.objects.all().order_by('-date_created')
    users = CustomUser.objects.all()
    recent_enquiries = Enquiry.objects.filter(is_resolved=False).order_by('-date_sent')[:5]
    
    context = {
        'total_cases': cases.count(),
        'pending_cases': cases.filter(status='pending').count(),
        'active_cases': cases.filter(status='approved').count(),
        'cases': cases[:10],
        'users': users,
        'recent_enquiries': recent_enquiries
    }
    return render(request, 'cases/admin_dashboard.html', context)

@login_required
def lawyer_dashboard(request):
    if request.user.role != 'lawyer':
        messages.warning(request, "Access denied.")
        return redirect('home')
        
    assigned_cases = Case.objects.filter(lawyer=request.user).order_by('-last_updated')
    
    context = {
        'assigned_cases': assigned_cases,
        'active_count': assigned_cases.exclude(status='closed').count(),
        'closed_count': assigned_cases.filter(status='closed').count()
    }
    return render(request, 'cases/lawyer_dashboard.html', context)

@login_required
def client_dashboard(request):
    if request.user.role != 'client':
        messages.warning(request, "Access denied.")
        return redirect('home')
        
    my_cases = Case.objects.filter(client=request.user).order_by('-date_created')
    
    if request.method == 'POST':
        # Simple case creation logical here for demo, ideally uses a Form
        title = request.POST.get('title')
        description = request.POST.get('description')
        case_type = request.POST.get('case_type')
        if title and description:
            Case.objects.create(title=title, description=description, case_type=case_type, client=request.user)
            messages.success(request, "Case submitted successfully.")
            return redirect('client_dashboard')

    context = {
        'my_cases': my_cases,
    }
    return render(request, 'cases/client_dashboard.html', context)

@login_required
def update_case_status(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    
    # Allow Admin or the assigned Lawyer to update status
    if request.user.role == 'admin' or (request.user.role == 'lawyer' and case.lawyer == request.user):
        if request.method == 'POST':
            new_status = request.POST.get('status')
            if new_status in dict(Case.STATUS_CHOICES):
                case.status = new_status
                case.save()
                messages.success(request, f"Case status updated to {case.get_status_display()}")
            else:
                messages.error(request, "Invalid status.")
    else:
        messages.error(request, "Permission denied.")
        
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def assign_lawyer(request, case_id):
    if request.user.role != 'admin':
        messages.error(request, "Access denied.")
        return redirect('home')
        
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        lawyer_id = request.POST.get('lawyer_id')
        try:
            lawyer = CustomUser.objects.get(id=lawyer_id, role='lawyer')
            case.lawyer = lawyer
            case.status = 'approved' # Auto approve when lawyer is assigned
            case.save()
            messages.success(request, f"Lawyer {lawyer.username} assigned to case.")
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid lawyer selected.")
            
    return redirect('admin_dashboard')
