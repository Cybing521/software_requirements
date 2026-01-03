import os
from pypdf import PdfReader

pdf_dir = "en"
output_dir = "extracted_text"
os.makedirs(output_dir, exist_ok=True)

pdf_files = ["1-FourWs.pdf", "2-StartingPoint.pdf"]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    txt_filename = os.path.splitext(pdf_file)[0] + ".txt"
    txt_path = os.path.join(output_dir, txt_filename)
    
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue

    print(f"Extracting text from {pdf_file}...")
    try:
        reader = PdfReader(pdf_path)
        with open(txt_path, "w", encoding="utf-8") as f:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    f.write(text + "\n\n")
        print(f"Saved to {txt_path}")
    except Exception as e:
        print(f"Error extracting {pdf_file}: {e}")
