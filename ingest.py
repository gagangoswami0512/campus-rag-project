from pathlib import Path
from pypdf import PdfReader

PDF_FOLDER = Path("data/raw_pdfs")

def load_pdfs():
    documents = []

    for pdf_file in PDF_FOLDER.glob("*.pdf"):
        reader = PdfReader(pdf_file)

        #We start from 1 instead of 0 to match the page numbering in the PDF

        for page_num,page in enumerate(reader.pages,start=1):
            text = page.extract_text()
            
            if text:
                documents.append({
                    "filename": pdf_file.name,
                    "page_number": page_num,
                    "text": text
                })
    return documents

if __name__ == "__main__":
    docs = load_pdfs()

    print(f"Loaded {len(docs)} pages.\n")

    for doc in docs[:3]:
        print(f"{doc['filename']} | Page {doc['page_number']}")
        print(doc["text"][:200])
        print("-" * 50)
