from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('lawyer-dashboard/', views.lawyer_dashboard, name='lawyer_dashboard'),
    path('client-dashboard/', views.client_dashboard, name='client_dashboard'),
    path('update-status/<int:case_id>/', views.update_case_status, name='update_case_status'),
    path('assign-lawyer/<int:case_id>/', views.assign_lawyer, name='assign_lawyer'),
]
