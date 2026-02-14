from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    path('all_tasks/', views.all_tasks, name='all_tasks'),
    path('complaints/', views.complaint_tasks, name='complaint_tasks'), 
    path('maintenance/', views.maintenance_tasks, name='maintenance_tasks'),
    path('create/complaint/', views.create_complaint, name='create_complaint'),
    path('create/maintenance/', views.create_maintenance, name='create_maintenance'),
    path('maintenance/<int:pk>/', views.maintenance_detail, name='maintenance_detail'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path("maintenance/calendar/", views.maintenance_calendar, name="maintenance_calendar"),
    path("complaint/calendar/", views.complaint_calendar, name="complaint_calendar"),
]