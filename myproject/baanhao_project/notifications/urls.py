from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.notification_view, name="list"),
    path("broadcast/", views.broadcast_system, name="broadcast_system"),
]