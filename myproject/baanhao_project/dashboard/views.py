from django.shortcuts import render

def dashboard(request):
    # จำลองข้อมูล (ในอนาคตคุณค่อยเปลี่ยนไปดึงจาก Database จริง)
    context = {
        'username': 'Jome',
        
        # ข้อมูลการ์ดด้านบน
        'total_residents': 1824,
        'total_tasks': 1123,
        'waiting_tasks': 114,
        'completed_tasks': 1237,

        # ข้อมูล Works Progress
        'progress_waiting': 21,
        'progress_inprogress': 58,
        'progress_overdue': 21,

        # ข้อมูลกราฟรายเดือน (แสดงเป็นตารางแทน)
        'monthly_data': [
            {'month': 'Jan', 'current': 30, 'past': 20},
            {'month': 'Feb', 'current': 45, 'past': 30},
            {'month': 'Mar', 'current': 35, 'past': 25},
            # ... ใส่เพิ่มได้
        ],

        # ข้อมูล Common Fee
        'fee_achieved': 67
    }
    return render(request, 'dashboard/dashboard.html', context)