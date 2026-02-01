import os

def clear_screen():
    """ฟังก์ชันสำหรับล้างหน้าจอ Terminal ให้สะอาด"""
    # ตรวจสอบระบบปฏิบัติการ (nt คือ Windows, อื่นๆ คือ Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title, user_name=None):
    """
    ฟังก์ชันสำหรับแสดงหัวกระดาษในทุกๆ หน้า
    :param title: ชื่อของหน้าปัจจุบัน (เช่น Dashboard, All Tasks)
    :param user_name: ชื่อของผู้ใช้งานที่ Login อยู่ (ถ้ามี)
    """
    clear_screen()
    print("=" * 60)
    # แสดงชื่อโปรเจกต์และชื่อหน้าที่กำลังใช้งานอยู่
    header_text = f"🏠 BAAN HAO SMART LIVING : {title.upper()}"
    print(f"{header_text:^60}")
    
    # ถ้ามีการส่งชื่อผู้ใช้มา ให้แสดงชื่อผู้ใช้ที่มุมขวา
    if user_name:
        user_display = f"User: {user_name}"
        print(f"{user_display:>60}") # >60 คือการชิดขวา
        
    print("=" * 60 + "\n")

def format_table_header():
    """ฟังก์ชันเสริมสำหรับช่วยจัดหัวตารางให้สวยงาม (ใช้ใน tasks_manager)"""
    print(f"{'ID':<10} | {'TYPE':<10} | {'STATUS':<15} | {'ASSIGNEE'}")
    print("-" * 60)