from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.all_tasks, name='all_tasks'), 
    path('all_tasks_complaints/', views.complaint_tasks, name='complaint_tasks'), 
    path('all_tasks_maintainance/', views.maintainance_tasks, name='maintainance_tasks'),
    
]