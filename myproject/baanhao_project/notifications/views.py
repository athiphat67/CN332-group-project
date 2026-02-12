from django.core.paginator import Paginator
from django.shortcuts import render


def notification_view(request):

    # 🔥 สร้างข้อมูลปลอม 15 อัน
    fake_notifications = []

    for i in range(1, 16):
        fake_notifications.append({
            "title": "TASK#133 (Receive) : Pumpler Configuration",
            "message": "Mark Gonzales - Technician - 13 Nov",
            "is_read": True if i % 2 == 0 else False,
        })

    paginator = Paginator(fake_notifications, 8)  # 8 ต่อหน้า
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "notifications/notifications.html", {
        "page_obj": page_obj
    })