PDF to Image Converter (Single File)

เว็บแอปสำหรับแปลงไฟล์ PDF เป็นรูปภาพ PNG หรือ JPG โดยเน้นการใช้งานไฟล์เดียว:

อัปโหลด PDF 1 ไฟล์

เลือกคุณภาพ (Normal / High)

เลือกรูปแบบไฟล์ (PNG / JPG)

Preview ไฟล์แบบขยายใหญ่

ลบไฟล์ที่ไม่ต้องการ

ดาวน์โหลดไฟล์แปลงแล้วทันที

ระบบจะลบไฟล์ชั่วคราวหลังดาวน์โหลดเสร็จ

โครงสร้างโปรเจกต์

pdf_converter/
├── app.py - Flask backend
├── requirements.txt - Python dependencies
├── README.txt
├── uploads/ - โฟลเดอร์เก็บไฟล์ PDF ชั่วคราว
├── output/ - โฟลเดอร์เก็บไฟล์รูปภาพชั่วคราว
├── templates/
│ └── index.html - หน้าเว็บหลัก
└── static/
└── style.css - CSS ของเว็บ

Dependencies

Python 3.9+

Flask

PyMuPDF (fitz)

uuid

ติดตั้ง dependencies ด้วยคำสั่ง:
pip install flask pymupdf

วิธีรันโปรเจกต์

เปิด terminal หรือ command line

เข้าไปยังโฟลเดอร์โปรเจกต์

รัน Flask ด้วยคำสั่ง: python app.py

เปิดเว็บเบราว์เซอร์แล้วไปที่: http://127.0.0.1:5000

การใช้งาน

คลิกหรือ drag & drop PDF ลงใน Upload Box

เลือกคุณภาพและฟอร์แมต (PNG / JPG)

คลิกไอคอน Preview เพื่อดูขนาดใหญ่

คลิกไอคอน Delete เพื่อลบไฟล์ที่ไม่ต้องการ

คลิก Convert → ดาวน์โหลดรูปภาพทันที

หลังดาวน์โหลด ระบบจะลบไฟล์เดิมอัตโนมัติ

หมายเหตุ

ไฟล์ PDF จะเก็บใน uploads/ ชั่วคราว

รูปภาพที่แปลงแล้วจะเก็บใน output/ ชั่วคราว

ไฟล์ที่ถูกดาวน์โหลดแล้วจะถูกลบจากระบบโดยอัตโนมัติ

รองรับ PDF ปกติทั่วไป หาก PDF มีการเข้ารหัสหรือ protected อาจไม่สามารถแปลงได้

PDF ขนาดใหญ่หรือหลายหน้า → การแปลงอาจใช้เวลานานขึ้น

เทคโนโลยีที่ใช้

Backend: Python + Flask

PDF → Image: PyMuPDF (fitz)

Frontend: HTML, CSS, JavaScript (Vanilla)

Icon: Remix Icon (https://remixicon.com/)
