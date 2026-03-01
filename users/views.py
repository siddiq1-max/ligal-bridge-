from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import ClientRegistrationForm

def register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            
            if user.role == 'admin':
                return redirect('/admin-dashboard/') # Placeholder URL
            elif user.role == 'lawyer':
                return redirect('/lawyer-dashboard/') # Placeholder URL
            else:
                return redirect('client_dashboard')
    else:
        form = ClientRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
    
    def get_success_url(self):
        user = self.request.user
        if user.role == 'admin':
            return '/admin-dashboard/'
        elif user.role == 'lawyer':
            return '/lawyer-dashboard/'
        elif user.role == 'client':
            return '/client-dashboard/'
        return '/'
