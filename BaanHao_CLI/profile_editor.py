import time
from utils import header

def profile_menu(user_data):
    while True:
        header("Profile Settings", user_data['firstname'])
        print(f"Current Information:")
        print(f"First Name : {user_data.get('firstname', 'N/A')}")
        print(f"Last Name  : {user_data.get('lastname', 'Living')}")
        print(f"Department : {user_data.get('department', 'Juristic')}")
        print(f"Phone Num  : {user_data.get('phone', '012-345-6789')}")
        print("-" * 50)
        
        print("1. ✏️  Edit Personal Information (แก้ไขข้อมูลส่วนตัว)")
        print("2. 🔑 Change Password (เปลี่ยนรหัสผ่าน)")
        print("3. 🔙 Back to Main Menu")
        
        choice = input("\nSelect Action (1-3): ")
        
        if choice == '1':
            edit_personal_info(user_data)
        elif choice == '2':
            change_password(user_data)
        elif choice == '3':
            break

def edit_personal_info(user_data):
    header("Edit Information")
    print("Leave blank to keep current value (กด Enter หากไม่ต้องการแก้ไข)")
    
    new_first = input(f"New First Name [{user_data['firstname']}]: ")
    new_last  = input(f"New Last Name [{user_data.get('lastname', 'Living')}]: ")
    new_phone = input(f"New Phone Number [{user_data.get('phone', '012-345-6789')}]: ")
    
    # Update ข้อมูลใหม่
    if new_first: user_data['firstname'] = new_first
    if new_last:  user_data['lastname'] = new_last
    if new_phone: user_data['phone'] = new_phone
    
    print("\n Saving changes...")
    time.sleep(1)
    print("✅ Profile Updated Successfully!")
    time.sleep(1)

# เป็นฟังก์ชันเปลี่ยนรหัสแบบ demo อยู่
def change_password(user_data):
    header("Change Password")
    old_p = input("Enter Current Password: ")
    
    if old_p == user_data['password']:
        new_p = input("Enter New Password: ")
        confirm_p = input("Confirm New Password: ")
        
        if new_p == confirm_p and len(new_p) >= 4:
            user_data['password'] = new_p
            print("\n✅ Password changed successfully!")
        else:
            print("\n❌ Error: Passwords do not match or too short.")
    else:
        print("\n❌ Error: Incorrect current password.")
    
    input("\nPress Enter to continue...")