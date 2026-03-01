from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('client', 'Client'), ('lawyer', 'Lawyer')], widget=forms.Select(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'phone_number', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user
