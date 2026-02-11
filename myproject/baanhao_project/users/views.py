from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, UserRole
from django.shortcuts import get_object_or_404
from django.utils import timezone

def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to next page if specified, otherwise to dashboard
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Username หรือ Password ไม่ถูกต้อง')
    
    return render(request, 'users/login.html')

def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'ออกจากระบบเรียบร้อยแล้ว')
    return redirect('users:login')

def staff_list(request):
    # 1. Base Query: ดึง User ทั้งหมดที่ไม่ใช่ Resident และไม่ใช่ Superuser (ถ้าไม่อยากให้เห็น Superuser)
    # เรียงตาม Role และ ชื่อ
    staff_users = User.objects.exclude(role=UserRole.RESIDENT).order_by('role', 'first_name')

    # 2. Role Filter Logic (จาก Tabs ด้านบน)
    role_filter = request.GET.get('role')
    
    if role_filter == 'juristic':
        staff_users = staff_users.filter(role=UserRole.JURISTIC)
    elif role_filter == 'technician':
        staff_users = staff_users.filter(role=UserRole.TECHNICIAN)
    elif role_filter == 'security':
        staff_users = staff_users.filter(role=UserRole.SECURITY)
    elif role_filter == 'admin':
        staff_users = staff_users.filter(role=UserRole.ADMIN)

    # 3. Count Data (นับจำนวน Staff ทั้งหมดเพื่อแสดงใน Badge)
    all_staff_count = User.objects.exclude(role=UserRole.RESIDENT).count()

    # 4. Pagination (8 คนต่อหน้า ตาม Design)
    paginator = Paginator(staff_users, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'staffs': page_obj, # ส่ง page_obj ไปวนลูป
        'all_count': all_staff_count,
        'current_role': role_filter if role_filter else 'all'
    }

    return render(request, 'users/staff_list.html', context)

def staff_detail(request, staff_id):
    # ดึง User ที่ระบุ
    staff = get_object_or_404(User, id=staff_id)
    
    # Logic หา Previous/Next staff (โดยเรียงตาม role, first_name เหมือนหน้า list)
    # หมายเหตุ: วิธีนี้เป็นแบบพื้นฐาน ถ้า User เยอะมากอาจต้องปรับ Logic
    all_staff = User.objects.exclude(role=UserRole.RESIDENT).order_by('role', 'first_name')
    staff_list = list(all_staff)
    
    try:
        current_index = staff_list.index(staff)
        previous_staff = staff_list[current_index - 1] if current_index > 0 else None
        next_staff = staff_list[current_index + 1] if current_index < len(staff_list) - 1 else None
    except ValueError:
        previous_staff = None
        next_staff = None

    context = {
        'staff': staff,
        'previous_staff': previous_staff,
        'next_staff': next_staff,
    }
    return render(request, 'users/staff_detail.html', context)

def dashboard_view(request):
    context = {
        'waiting_count': 12,
        'progress_count': 34,
        'overdue_count': 5,
        'completed_count': 58,
        'last_update': timezone.now().strftime('%d/%m/%Y %I:%M %p'),
        'road_count': 10,
        'electric_count': 7,
        'water_count': 5,
        'maintenance_total': 22,
        'chart_labels': ['Jan','Feb','Mar','Apr','May','Jun'],
        'chart_data': [5, 12, 8, 20, 15, 25],
    }
    return render(request, 'templates/dashboard/dashboard.html', context)

def all_tasks_view(request):
    return render(request, 'tasks/all_tasks.html')

def analytics_view(request):
    return render(request, "analytics/analytics.html")