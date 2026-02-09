from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User, UserRole

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