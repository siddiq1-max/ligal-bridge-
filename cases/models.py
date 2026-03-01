from django.db import models
from django.conf import settings

class Case(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved/Active'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    courthouse = models.CharField(max_length=200, blank=True)
    case_type = models.CharField(max_length=100) # e.g., Civil, Criminal, Family
    
    # Relationships
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_cases', limit_choices_to={'role': 'client'})
    lawyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lawyer_cases', limit_choices_to={'role': 'lawyer'})
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # Documents can be added later as a separate model or FileField here

    def __str__(self):
        return f"{self.title} ({self.status})"

class Enquiry(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='enquiries', null=True, blank=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Enquiry from {self.sender.username}: {self.subject}"
