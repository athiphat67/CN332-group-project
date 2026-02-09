from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks, name='all_tasks'),
    path('complaints/', views.complaint_tasks, name='complaint_tasks'), 
    path('maintenance/', views.maintenance_tasks, name='maintenance_tasks'),
    path('create/complaint/', views.create_complaint, name='create_complaint'),
    path('create/maintenance/', views.create_maintenance, name='create_maintenance'),
]