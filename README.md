<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
<div class="canvas">
<h1>PDF to Image Converter (Single File)</h1>

<p>เว็บแอปสำหรับแปลง PDF เป็นรูปภาพ PNG/JPG ไฟล์เดียว</p>

<h2>ฟีเจอร์หลัก</h2>
<ul>
<li>อัปโหลด PDF 1 ไฟล์</li>
<li>เลือกคุณภาพ (Normal / High)</li>
<li>เลือกรูปแบบไฟล์ (PNG / JPG)</li>
<li>Preview ไฟล์ขนาดใหญ่</li>
<li>ลบไฟล์ไม่ต้องการ</li>
<li>ดาวน์โหลดรูปภาพทันที</li>
<li>ระบบลบไฟล์ชั่วคราวหลังดาวน์โหลด</li>
</ul>

<h2>โครงสร้างโปรเจกต์</h2>
<pre>
pdf_converter/
├── app.py
├── requirements.txt
├── README.md
├── uploads/
├── output/
├── templates/index.html
└── static/style.css
</pre>

<h2>Dependencies</h2>
<p>Python 3.9+, Flask, PyMuPDF (fitz)</p>
<pre>pip install flask pymupdf</pre>

<h2>วิธีรัน</h2>
<pre>
python app.py
เปิดเว็บเบราว์เซอร์ที่ http://127.0.0.1:5000
</pre>

<h2>การใช้งาน</h2>
<ol>
<li>คลิกหรือ drag & drop PDF ลงใน Upload Box</li>
<li>เลือกคุณภาพและฟอร์แมต</li>
<li>Preview ไฟล์ใหญ่</li>
<li>ลบไฟล์ไม่ต้องการ</li>
<li>Convert → ดาวน์โหลดรูปภาพ</li>
<li>หลังดาวน์โหลด ระบบลบไฟล์อัตโนมัติ</li>
</ol>

<h2>หมายเหตุ</h2>
<ul>
<li>รองรับ PDF ปกติทั่วไป (PDF protected อาจไม่สามารถแปลงได้)</li>
<li>PDF ขนาดใหญ่หลายหน้า → การแปลงอาจใช้เวลานาน</li>
</ul>

<h2>เทคโนโลยี</h2>
<ul>
<li>Backend: Python + Flask</li>
<li>PDF → Image: PyMuPDF (fitz)</li>
<li>Frontend: HTML, CSS, JavaScript (Vanilla)</li>
<li>Icon: Remix Icon</li>
</ul>

<h2>License</h2>
<p>Open Source, Free to use & modify</p>
</div>
</body>
</html>
