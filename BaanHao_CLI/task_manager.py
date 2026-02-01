import time
from utils import header, format_table_header

def manage_tasks_menu(tasks, user):
    """เมนูหลักของการจัดการงาน (Routing)"""
    while True:
        header("Task Management")
        print("1. View All Tasks (ดูรายการทั้งหมด)")
        print("2. Search Task (ค้นหาด้วย ID/ประเภท)")
        
        # Admin tag
        admin_tag = " [Admin Only]" if user['role'] != 'admin' else ""
        print(f"3. ➕ Add New Task{admin_tag}")
        print(f"4. ✏️  Update Task Status{admin_tag}")
        print(f"5. ❌ Delete Task{admin_tag}")
        print("6. 🔙 Back")

        choice = input("\nSelect Action (1-6): ")

        if choice == "1":
            view_all_tasks(tasks)
        elif choice == "2":
            search_task(tasks)
        elif choice in ["3", "4", "5"]:
            if user["role"] == "admin":
                if choice == "3":
                    add_task(tasks)
                elif choice == "4":
                    update_task(tasks, user) 
                elif choice == "5":
                    delete_task(tasks, user)
            else:
                print("\n🚫 Access Denied: ท่านไม่มีสิทธิ์ในการแก้ไขข้อมูล (View Only)")
                time.sleep(0.5)
        elif choice == "6":
            break


def view_all_tasks(tasks):
    header("All Maintenance Tasks")
    format_table_header()

    for t in tasks:
        icon = (
            "🟡"
            if t["status"] == "Waiting"
            else "🟠"
            if t["status"] == "In progress"
            else "🔴"
            if t["status"] == "Overdue"
            else "✅"
        )
        print(
            f"{t['id']:<10} | {t['type']:<10} | {icon} {t['status']:<12} | {t['assignee']}"
        )
        print(f"   Detail: {t['detail']}")
        print("-" * 60)

    input("\nPress Enter to return...")


def search_task(tasks):
    header("Search Task")
    query = input("Enter Task ID or Type to search (e.g., 1023 or ถนน): ")
    print("\n" + "-" * 60)

    found = False
    for t in tasks:
        if query.lower() in t["id"].lower() or query in t["type"]:
            print(f"✅ Found: [{t['id']}] {t['type']} | Status: {t['status']}")
            print(f"   Detail: {t['detail']} | Assignee: {t['assignee']}\n")
            found = True

    if not found:
        print("❌ No task found matching your search.")

    input("\nPress Enter to continue...")

def update_task(tasks, user):
    header("Update Status", user['firstname'])
    
    # show all tasks
    view_all_tasks(tasks) 
    print("\n" + "="*60)
    
    target_id = input("Enter Task ID to update (e.g., 10/1023) หรือกด Enter เพื่อยกเลิก: ")
    if not target_id: return

    for t in tasks:
        if t['id'] == target_id:
            print(f"\n📌 Current Task: {t['type']} - {t['detail']}")
            print(f"Current Status: {t['status']}")
            print("-" * 30)
            print("Select New Status: 1. Waiting | 2. In progress | 3. Overdue | 4. Complete")
            s_choice = input("Choice (1-4): ")
            status_map = {"1": "Waiting", "2": "In progress", "3": "Overdue", "4": "Complete"}
            
            if s_choice in status_map:
                t['status'] = status_map[s_choice]
                print(f"✅ Status updated to '{status_map[s_choice]}' successfully!")
            else:
                print("❌ Invalid choice.")
            time.sleep(0.5)
            return
            
    print("❌ Task ID not found.")
    time.sleep(0.5)


def delete_task(tasks, user):
    """ลบรายการงาน (Delete) โดยแสดงรายการทั้งหมดก่อน"""
    header("Delete Task", user['firstname'])
    
    # show all task before delete task
    view_all_tasks(tasks)
    print("\n" + "="*60)
    
    target_id = input("Enter Task ID to delete หรือกด Enter เพื่อยกเลิก: ")
    if not target_id: return
    
    target_item = next((t for t in tasks if t['id'] == target_id), None)
    
    if target_item:
        print(f"\n⚠️  Found Task: [{target_item['id']}] {target_item['type']}")
        print(f"   Detail: {target_item['detail']}")
        confirm = input("\nAre you sure you want to delete this task? (y/n): ")

        if confirm.lower() == "y":
            tasks.remove(target_item)
            print("✅ Task deleted successfully.")
        else:
            print("❌ Deletion cancelled.")
    else:
        print(f"❌ Error: Task ID '{target_id}' not found.")

    time.sleep(0.5)

def add_task(tasks):
    header("Add New Task")
    print("Please enter task details:")
    cat = input("Category Code (10/20/30): ")

    # ป้องกันการกรอก Category ผิด (Input Validation)
    if cat not in ["10", "20", "30"]:
        print("❌ Invalid Category! Please use 10, 20, or 30.")
        time.sleep(0.5)
        return

    new_id = f"{cat}/{int(time.time()) % 10000}"
    t_type = input("Type: ")
    detail = input("Detail: ")
    assign = input("Assign to: ")

    if not t_type or not detail:
        print("❌ Error: Type and Detail cannot be empty.")
        time.sleep(0.5)
        return

    tasks.append(
        {
            "id": new_id,
            "type": t_type,
            "detail": detail,
            "assignee": assign,
            "status": "Waiting",
        }
    )
    print(f"\n✅ Task {new_id} added successfully!")
    time.sleep(1)
