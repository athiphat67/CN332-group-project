from django.shortcuts import render
from .models import Issue

def all_tasks(request):
    issues = Issue.objects.all() # ดึงงานทั้งหมดออกมา
    return render(request, 'issues/all_tasks.html', {'issues': issues})