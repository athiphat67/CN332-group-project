from django.shortcuts import render

# Create your views here.
def notifications_view(request):
    return render(request, "notifications/notifications.html")