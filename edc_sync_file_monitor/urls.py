from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, include

from .admin_site import edc_sync_file_monitor_admin
from .views import AdministrationView, HomeView, ReportView


app_name = 'edc_sync_file_monitor'

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    path('admin/', edc_sync_file_monitor_admin.urls),
    path('admin/', admin.site.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    
    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    re_path('^file_monitor_report/(?P<site_value>\w+)/$',
            ReportView.as_view(), name='file_monitor_report_url'),
    path('', HomeView.as_view(), name='home_url'),
]
