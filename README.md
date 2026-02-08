j# 🏡 ระบบบริหารจัดการหมู่บ้านจัดสรรอัจฉริยะ

> **Course:** CN332 - Object-Oriented Analysis and Design  
> **Instructor:** ผู้ช่วยศาสตราจารย์ ดร.พิศาล แก้วประภา
---

## 👥 สมาชิกในกลุ่ม (Team Members)

| รหัสนักศึกษา | ชื่อ-นามสกุล |
|:---:|:---|
| 6710615060 | โชติวิชช์ ดังสะท้าน |
| 6710615292 | อธิภัทร ศูนย์สิทธิ์ |
| 6710615185 | ภูริช อัมพะวา |
| 6710685055 | พัชรพล มาลัยศรี |
| 6710685014 | ธีภพ รัตนทรัพย์ศิริ |
| 6710545010 | นพัตธีรา เหลาเกิ้มหุ่ง |
| 6710615144 | ปณิธาน ตันตื้อ |

---

## 📄 Project Concept

### 1. ภาพรวมและวัตถุประสงค์
โครงการนี้มุ่งเน้นการแก้ Pain Points เดิมๆ ของการจัดการหมู่บ้านด้วยเทคโนโลยีอัจฉริยะ:
* **Smart Assistant 24/7:** เป็นผู้ช่วยอัจฉริยะคอยตอบคำถาม รับเรื่องร้องเรียน และเฝ้าระวังภัยผ่านการวิเคราะห์เสียงและเซ็นเซอร์ 
* **Seamless Communication:** เชื่อมต่อนิติบุคคลและลูกบ้านผ่าน LINE OA และ NLP Chatbot ลดระยะเวลารอคอย 
* **Automated Operations:** ลดภาระงานเอกสารด้วยระบบตรวจสอบสลิปโอนเงินอัตโนมัติ (OCR) และคัดกรองงานด้วย AI 
* **Transparency:** จัดเก็บข้อมูลโปร่งใส ตรวจสอบสถานะงานและบัญชีได้แบบ Real-time 

### 2. ฟีเจอร์หลัก

#### 📱 A. Line OA & Intelligent Service (ส่วนบริการลูกบ้าน)
* **AI Complaint Handling:** รับเรื่องร้องเรียน (เช่น เสียงดังรบกวน) โดย AI จะวิเคราะห์แยกประเภทและส่งเรื่องให้ รปภ. ทันที 
* **Rules & Regulations Query (RAG):** ลูกบ้านสามารถถามกฎระเบียบ (เช่น การเลี้ยงสัตว์) และได้รับคำตอบที่ถูกต้องจากคู่มือหมู่บ้านทันที 
* **Visitor Management:** ระบบลงทะเบียนผู้มาติดต่อล่วงหน้า สร้าง QR Code ให้แขกสแกนเข้าไม้กั้นอัตโนมัติ พร้อมแจ้งเตือนลูกบ้านเมื่อแขกมาถึง
* **Smart Payment:** ตรวจสอบสลิปโอนเงินค่าส่วนกลางด้วย OCR เทียบกับยอดเงินและบัญชีธนาคาร พร้อมออก E-Receipt ภายใน 3 วินาที 
* **Smart Broadcast:** แจ้งเตือนกิจกรรมต่างๆ (เช่น ฉีดปลวก) ตามตารางปฏิทินกลางของนิติบุคคล 

---

## 💡 Use Case Scenarios (สถานการณ์ตัวอย่าง)

| Scenario | รายละเอียดการทำงาน |
| :--- | :--- |
| **1. ถามกฎระเบียบ** | ลูกบ้านพิมพ์ถาม "เลี้ยงสุนัขบางแก้วได้ไหม?" -> AI ค้นข้อมูลจากคู่มือ (RAG) -> ตอบกลับข้อกำหนดและคำแนะนำการเลี้ยง  |
| **2. เพื่อนมาหา** | ลูกบ้านแจ้งทะเบียนรถเพื่อน -> AI ส่ง QR Code (Visitor Pass) ให้ -> เพื่อนสแกนเข้าป้อมยาม -> ไม้กั้นเปิดและแจ้งเตือนลูกบ้าน  |
| **3. จ่ายค่าส่วนกลาง** | ลูกบ้านส่งสลิปโอนเงิน -> AI (OCR) อ่านค่าวันที่/ยอดเงิน เทียบกับธนาคาร -> บันทึกสถานะ "ชำระแล้ว" และส่งใบเสร็จทันที  |

---

## 🚀 Project Progess

### Week 1: Concept
- **Documentation:** [📄 Concept Paper](Documents/Iteration1/hm1_CONCEPT_PAPER.pdf)
- **Presentation:** [📊 Iteration 1 Slides](Documents/Iteration1/iteration1-BaanHao.pdf)

### Week 2: Requirements
- **Documentation:** [📄 การแจกแจง Requirement](Documents/Iteration2/hm2_การแจกแจงrequirement.pdf)
- **Presentation:** [📊 Iteration 2 Slides](Documents/Iteration2/iteration2-BaanHao.pdf)

### Week 3: Development
- **Design Tool:** [🎨 Canva Link](https://www.canva.com/design/DAG-12vJwHI/FFv4AjDZGIT0hqmoKelIXQ/view?utm_content=DAG-12vJwHI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h50f6ef177b)
- **Presentation:** [📊 Iteration 3 Slides](Documents/Iteration3/Iteration3_BannHao.pdf)

### Week 4: UX/UI Demo
- **GUI Website:** [🎥 Walkthrough Video](https://youtu.be/igLxI9eYJGI?si=iCysm1rsU2UA-4bB)
- **Line OA:** [📱 Short Demo Video](https://youtube.com/shorts/j89uEZ3Yu6c?feature=share)

### Week 5: Facade Pattern in project
- **Presentation:** [Iteration 5 Slides](https://www.canva.com/design/DAHAvvavFFM/HOUiDaKPhY2ek7LEpf9VWA/view?utm_content=DAHAvvavFFM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he9fad04ba6)

---

## 📝 Instructor Feedback Log

> [!IMPORTANT]
> **Date: 26/01/2026 (Iteration 1-3)**
> - **Comment:** ให้ดูตัวอย่างการสืบทอด Class (Inheritance) ที่ยืดหยุ่นมากขึ้น เพื่อให้ Code Clean และจัดการ Logic ได้ง่ายขึ้น

---
*Last Updated: 2026-02-08*
