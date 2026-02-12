from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Resident, Technician, JuristicOfficer, Security, Admin as AdminModel, RegistrationRequest

# 1. ปรับแต่ง User Admin ให้รองรับ Custom Fields ของเรา
class CustomUserAdmin(UserAdmin):
    model = User
    
    # 1.1 หน้าแสดงรายการ (List View) ให้โชว์คอลัมน์อะไรบ้าง
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['role', 'is_staff', 'is_active'] # เพิ่มตัวกรองด้านขวา
    
    # 1.2 หน้าแก้ไข (Edit Form) ต้องเพิ่ม Field ใหม่เข้าไป
    # fieldsets คือการจัดกลุ่มข้อมูลในหน้าแก้ไข
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role', 'line_id', 'phone_number', 'profile_image', 'gender')}),
    )
    
    # 1.3 หน้าสร้าง User ใหม่ (Add Form)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('role', 'line_id', 'phone_number', 'email')}),
    )

# ลงทะเบียน User หลัก
admin.site.register(User, CustomUserAdmin)

# 2. ลงทะเบียน Role ย่อยๆ (แบบเรียบง่าย)
# ถ้าอยากเห็นว่าใครเป็นเจ้าของ Profile นี้ ให้โชว์ column 'user'

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'house', 'is_owner']
    search_fields = ['user__username', 'house__house_number'] # ค้นหาจากชื่อ user หรือเลขที่บ้านได้

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'current_status']
    list_filter = ['current_status']

@admin.register(JuristicOfficer)
class JuristicOfficerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'officer_id']

@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'station_id', 'shift_time']

@admin.register(AdminModel)
class AdminRoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'permission_level']

@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'reviewed_at', 'reviewed_by']
    list_filter = ['status']
    search_fields = ['user__username', 'user__email']