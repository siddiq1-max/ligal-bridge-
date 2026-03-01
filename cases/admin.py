from django.contrib import admin
from .models import Case, Enquiry

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'lawyer', 'status', 'date_created')
    list_filter = ('status', 'case_type')
    search_fields = ('title', 'client__username', 'lawyer__username')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'case', 'date_sent', 'is_resolved')
    list_filter = ('is_resolved', 'date_sent')
