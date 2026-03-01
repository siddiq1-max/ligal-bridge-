from django.contrib import admin
from django.urls import path, include
from cases import views as cases_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('cases/', include('cases.urls')),
    # Top-level dashboard access
    path('client-dashboard/', cases_views.client_dashboard, name='client_dashboard_top'),
    path('lawyer-dashboard/', cases_views.lawyer_dashboard, name='lawyer_dashboard_top'),
    path('admin-dashboard/', cases_views.admin_dashboard, name='admin_dashboard_top'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
