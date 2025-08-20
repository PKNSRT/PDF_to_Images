from flask import Flask, render_template, request, jsonify, send_file, url_for, after_this_request
import os, uuid
import fitz
from zipfile import ZipFile

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def pdf_to_images(pdf_path, output_folder, pages=None, dpi=150, fmt="PNG"):
    pdf_document = fitz.open(pdf_path)
    saved_files = []
    total_pages = len(pdf_document)
    selected_pages = pages if pages else range(total_pages)
    for i in selected_pages:
        page = pdf_document[i]
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{i+1}.{fmt.lower()}")
        pix.save(output_file)
        saved_files.append(output_file)
    pdf_document.close()
    return saved_files

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("pdf_files[]")
    response = []
    for file in files:
        if file.filename.endswith(".pdf"):
            file_id = str(uuid.uuid4())
            file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
            file.save(file_path)
            doc = fitz.open(file_path)
            num_pages = len(doc)
            doc.close()
            response.append({
                "id": file_id,
                "name": file.filename,
                "pages": num_pages
            })
    return jsonify(response)

@app.route("/delete_file", methods=["POST"])
def delete_file():
    data = request.json
    file_id = data.get("id")
    file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
    if os.path.exists(file_path):
        os.remove(file_path)
    return jsonify({"success": True})

@app.route("/thumbnail/<file_id>/<int:page_num>")
def thumbnail(file_id, page_num):
    pdf_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
    if not os.path.exists(pdf_path):
        return "", 404
    doc = fitz.open(pdf_path)
    if page_num >= len(doc):
        return "", 404
    page = doc[page_num]
    mat = fitz.Matrix(72/72, 72/72)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    thumb_path = os.path.join(OUTPUT_FOLDER, f"{file_id}_{page_num+1}_thumb.png")
    pix.save(thumb_path)
    doc.close()
    return send_file(thumb_path, mimetype="image/png")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    files = data["files"]
    quality = data.get("quality","Normal")
    fmt = data.get("format","PNG")
    dpi = 150 if quality=="Normal" else 300

    # ถ้าไฟล์เดียวและหน้าเดียว
    if len(files) == 1 and len(files[0]["pages"]) == 1:
        f = files[0]
        pdf_file = os.path.join(UPLOAD_FOLDER, f"{f['id']}.pdf")
        out_files = pdf_to_images(pdf_file, OUTPUT_FOLDER, pages=f['pages'], dpi=dpi, fmt=fmt)
        os.remove(pdf_file)
        img_url = url_for('serve_output', filename=os.path.basename(out_files[0]))
        return jsonify({"single_image": img_url})

    # ถ้ามีหลายไฟล์หรือหลายหน้า -> ZIP
    zip_name = f"converted_{uuid.uuid4()}.zip"
    zip_path = os.path.join(OUTPUT_FOLDER, zip_name)
    with ZipFile(zip_path, 'w') as zipf:
        for f in files:
            pdf_file = os.path.join(UPLOAD_FOLDER, f"{f['id']}.pdf")
            out_files = pdf_to_images(pdf_file, OUTPUT_FOLDER, pages=f['pages'], dpi=dpi, fmt=fmt)
            for of in out_files:
                zipf.write(of, os.path.basename(of))
                os.remove(of)
            os.remove(pdf_file)
    zip_url = url_for('serve_output', filename=zip_name)
    return jsonify({"zip_url": zip_url})

@app.route("/output/<path:filename>")
def serve_output(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)

    @after_this_request
    def remove_file(response):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file: {e}")
        return response

    return send_file(file_path)

if __name__ == "__main__":
    app.run(debug=True)
