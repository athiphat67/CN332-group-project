from django.db import models

class House(models.Model):
    # Diagram: houseID (String), houseNumber (String)
    # houseID อาจจะใช้ ID อัตโนมัติของ Django หรือถ้ามีรหัสบ้านเฉพาะก็ใช้ Field นี้ครับ
    house_id = models.CharField(max_length=20, unique=True, help_text="Ex. A-101") 
    house_number = models.CharField(max_length=20, help_text="Ex. 99/101")
    
    # Diagram: owner: Resident
    # เราใช้ 'users.Resident' เพื่ออ้างอิงข้าม App
    # related_name='owned_houses' ทำให้เรียกจาก Resident กลับมาหาบ้านที่ตัวเองเป็นเจ้าของได้
    owner = models.ForeignKey(
        'users.Resident', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='owned_houses'
    )

    def __str__(self):
        return f"House {self.house_number} (ID: {self.house_id})"

class Vehicle(models.Model):
    # Diagram: registeredVehicles: List<String> -> แปลงเป็น Table แยกดีกว่าเก็บเป็น String ยาวๆ
    license_plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    
    # รถผูกกับบ้านหลังไหน
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='vehicles')
    
    def __str__(self):
        return f"{self.license_plate} ({self.house.house_number})"