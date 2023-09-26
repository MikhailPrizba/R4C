from django.urls import path
from .views import robots_report


urlpatterns = [
    path('get_excel_report/', robots_report, name='robots_get_report')
]