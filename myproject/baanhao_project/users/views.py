from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, UserRole

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
