from django.contrib import admin
from .models import Issue, Complaint, Maintenance

# 1. หน้าจอรวม (Dashboard) สำหรับดูทุกเรื่องที่เข้ามา
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    # โชว์ข้อมูลสำคัญ: เลขที่, หัวข้อ, ใครแจ้ง, สถานะ, ความด่วน, วันที่
    list_display = ('id', 'title', 'reporter', 'status', 'priority', 'created_date')
    
    # ตัวกรองด้านขวา (สำคัญมากสำหรับนิติฯ ใช้ดูงานค้าง)
    list_filter = ('status', 'priority', 'created_date')
    
    # ช่องค้นหา: ค้นจากหัวข้อ หรือ ชื่อคนแจ้ง (ต้องอ้างอิงข้ามตารางด้วย __)
    search_fields = ('title', 'description', 'reporter__user__username', 'reporter__user__first_name')
    
    # วันที่สร้าง ห้ามแก้ (Read only)
    readonly_fields = ('created_date',)
    
    # เรียงลำดับจาก ใหม่ -> เก่า
    ordering = ('-created_date',)

# 2. หน้าจอเฉพาะเรื่องร้องเรียน (Complaint)
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status', 'reporter')
    list_filter = ('status', 'category')
    search_fields = ('title', 'reporter__user__username')
    
    fieldsets = (
        ('Info', {
            'fields': ('reporter', 'title', 'description', 'category', 'priority')
        }),
        ('Status', {
            'fields': ('status', 'location')
        }),
        ('Evidence', {
            'fields': ('evidence_image', 'analysis_json') # โชว์ผล AI ด้วย
        }),
    )

# 3. หน้าจอเฉพาะงานช่าง (Maintenance)
@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'equipment_type', 'technician', 'status', 'appointment_date')
    list_filter = ('status', 'equipment_type', 'appointment_date')
    search_fields = ('title', 'technician__user__username')
    
    # เพิ่ม Actions พิเศษ: เช่น กดเลือกหลายงานแล้วสั่ง "ปิดงาน" พร้อมกัน (ถ้าต้องการ)
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(status='RESOLVED')
    mark_as_completed.short_description = "Mark selected tasks as RESOLVED"