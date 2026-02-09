from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('staff/', views.staff_list, name='staff_list'),
]