import time
from utils import header

def staff_menu(staff_list, user):
    """เมนูหลักสำหรับจัดการรายชื่อบุคลากร พร้อมระบบเช็คสิทธิ์"""
    while True:
        header("Juristic Office Staff", user['firstname'])
        # แสดงรายชื่อ
        print(f"{'ID':<8} | {'NAME':<18} | {'ROLE':<25} | {'STATUS'}")
        print("-" * 65)
        
        for s in staff_list:
            status_icon = "🟢" if s['status'] == "On Duty" else "⚪"
            print(f"{s['id']:<8} | {s['name']:<18} | {s['role']:<25} | {status_icon} {s['status']}")
            
        print("-" * 65)
        print("1. 🔍 View Detailed Info (ดูรายละเอียด/เบอร์โทร)")
        
        # แสดงเมนูเฉพาะ Admin
        if user['role'] == 'admin':
            print("2. ➕ Add New Staff (Admin Only)")
            print("3. ✏️  Edit Staff Detail (Admin Only)")
            print("4. 🔙 Back to Main Menu")
        else:
            print("2. 🔙 Back to Main Menu")

        choice = input("\nSelect Action: ")

        if choice == '1':
            view_staff_detail(staff_list)
        elif user['role'] == 'admin':
            if choice == '2': add_staff(staff_list)
            elif choice == '3': edit_staff(staff_list)
            elif choice == '4': break
        else:
            if choice == '2': break

def view_staff_detail(staff_list):
    header("Staff Detail Search")
    query = input("Enter Staff ID or Name to view: ").lower()
    found = False
    
    for s in staff_list:
        if query in s['id'].lower() or query in s['name'].lower():
            print(f"\n--- Information of {s['name']} ---")
            print(f"🆔 ID       : {s['id']}")
            print(f"🛠️  Position : {s['role']}")
            print(f"⏰ Shift    : {s['shift']}")
            print(f"📞 Phone    : {s['phone']}")
            print(f"📊 Status   : {s['status']}")
            found = True
            break
            
    if not found:
        print("\n❌ Staff member not found.")
    input("\nPress Enter to continue...")

def add_staff(staff_list):
    header("Add New Staff Member")
    new_id = f"ST{len(staff_list) + 1:03d}"
    name = input("Enter Name: ")
    role = input("Enter Role (e.g., ช่างเทคนิค): ")
    shift = input("Enter Shift (e.g., 08:00 - 17:00): ")
    phone = input("Enter Phone Number: ")
    
    if name and role:
        staff_list.append({
            "id": new_id, "name": name, "role": role, 
            "shift": shift, "phone": phone, "status": "Off Duty"
        })
        print(f"\n✅ Staff {new_id} added successfully!")
    else:
        print("\n❌ Error: Name and Role are required.")
    time.sleep(1.5)

def edit_staff(staff_list):
    header("Edit Staff Information")
    
    print(f"{'ID':<8} | {'NAME':<18} | {'ROLE':<25}")
    print("-" * 55)
    for s in staff_list:
        print(f"{s['id']:<8} | {s['name']:<18} | {s['role']:<25}")
    print("-" * 55)

    target_id = input("\nEnter Staff ID to edit (e.g., ST001) หรือกด Enter เพื่อยกเลิก: ").upper()
    
    if not target_id: return

    for s in staff_list:
        if s['id'] == target_id:
            print(f"\nEditing: {s['name']}")
            print("(Leave blank to keep current value / กด Enter หากไม่ต้องการเปลี่ยน)")
            
            new_role = input(f"New Role [{s['role']}]: ")
            new_phone = input(f"New Phone [{s['phone']}]: ")
            new_status = input(f"New Status (On Duty/Off Duty) [{s['status']}]: ")
            
            # ตรวจสอบการกรอกข้อมูล ถ้าไม่กรอก --> ใช้ค่าเดิม
            if new_role: s['role'] = new_role
            if new_phone: s['phone'] = new_phone
            if new_status: s['status'] = new_status
            
            print("\n✅ Staff details updated!")
            time.sleep(1)
            return
            
    print("\n❌ Staff ID not found.")
    time.sleep(1.5)