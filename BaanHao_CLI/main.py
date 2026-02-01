import os
import time
from utils import header, clear_screen
from task_manager import manage_tasks_menu
from profile_editor import profile_menu
from staff_viewer import staff_menu

user_data = [
    {
        "username": "Admin",
        "password": "1234",
        "firstname": "Admin",
        "department": "Juristic",
        "role": "admin",
    },
    {
        "username": "Big",
        "password": "1234",
        "firstname": "Athiphat",
        "department": "Maintenance",
        "role": "staff",
    },
    {
        "username": "Rich",
        "password": "1234",
        "firstname": "Purich",
        "department": "Security",
        "role": "staff",
    },
    {
        "username": "Jome",
        "password": "1234",
        "firstname": "Theepop",
        "department": "Maintenance",
        "role": "staff",
    },
]

current_user = None

tasks_list = [
    {
        "id": "10/1023",
        "type": "ถนน",
        "detail": "ถนนหน้าบ้านเป็นหลุมเป็นบ่อ",
        "assignee": "ช่างวิชัย ไชโย",
        "status": "In progress",
    },
    {
        "id": "10/2475",
        "type": "น้ำ",
        "detail": "ท่อประปาแตก",
        "assignee": "ช่างน้ำใจ ไม่มี",
        "status": "Overdue",
    },
    {
        "id": "10/1270",
        "type": "ไฟฟ้า",
        "detail": "สายไฟเปลือยๆ หล่นลงมาที่พื้น",
        "assignee": "ช่างอาทิตย์ เฉิดฉาย",
        "status": "Waiting",
    },
    {
        "id": "20/2510",
        "type": "ถนน",
        "detail": "ลูกระนาดแตกเสียหาย",
        "assignee": "ช่างวิชัย ไชโย",
        "status": "Waiting",
    },
    {
        "id": "20/4412",
        "type": "ส่วนกลาง",
        "detail": "กิ่งไม้ใหญ่บังกล้อง CCTV",
        "assignee": "ทีมสวนสะอาด",
        "status": "In progress",
    },
    {
        "id": "30/5001",
        "type": "ความปลอดภัย",
        "detail": "พบบุคคลภายนอกเดินเตร่ผิดปกติ",
        "assignee": "รปภ. สมชาย",
        "status": "Complete",
    },
]

staff_list = [
    {
        "id": "ST001",
        "name": "วิชัย ไชโย",
        "role": "technician",
        "shift": "08:00 - 17:00",
        "phone": "081-111-2222",
        "status": "On Duty",
    },
    {
        "id": "ST002",
        "name": "อาทิตย์ เฉิดฉาย",
        "role": "technician",
        "shift": "13:00 - 22:00",
        "phone": "082-222-3333",
        "status": "On Duty",
    },
    {
        "id": "ST003",
        "name": "สมชาย ปลอดภัย",
        "role": "security",
        "shift": "19:00 - 07:00",
        "phone": "083-333-4444",
        "status": "Off Duty",
    },
    {
        "id": "ST004",
        "name": "น้ำใจ ไม่มี",
        "role": "technician",
        "shift": "08:00 - 17:00",
        "phone": "084-444-5555",
        "status": "On Duty",
    },
    {
        "id": "ST05",
        "name": "ใจดี รักสวน",
        "role": "cleaner",
        "shift": "07:00 - 16:00",
        "phone": "085-555-6666",
        "status": "On Duty",
    },
]

def dashboard():
    while True:
        header("Main Dashboard", current_user["firstname"])

        print(f"--- Summary Weekly Status ---")
        print(f" Waiting: 23 | In progress: 58 | Overdue: 40")
        print(f" Already Complete: 389 works")
        print("-" * 50)
        print("1. [Manage] All Tasks (View/Search/Edit/Delete)")
        print("2. [Settings] Profile Editor")
        print("3. [Staff] Juristic Officer")
        print("4. [Logout] Exit Dashboard")

        choice = input("\nSelect Menu (1-4): ")

        if choice == "1":
            manage_tasks_menu(tasks_list, current_user)
        elif choice == "2":
            profile_menu(current_user)
        elif choice == "3":
            staff_menu(staff_list, current_user)
        elif choice == "4":
            print("Logging out...")
            break


if __name__ == "__main__":
    clear_screen()
    header("Login")
    u = input("👤 Username: ")
    p = input("🔑 Password: ")

    found_user = next(
        (item for item in user_data if item["username"] == u and item["password"] == p),
        None,
    )

    if found_user:
        current_user = found_user
        dashboard()
    else:
        print("\n Invalid User or Password")
