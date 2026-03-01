from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        # Here we would typically send an email or save to DB
        name = request.POST.get('name')
        messages.success(request, f"Thank you {name}, your message has been sent!")
        return render(request, 'core/contact.html')
    return render(request, 'core/contact.html')

def features(request):
    return render(request, 'core/features.html')
