
import os
import fitz  # PyMuPDF

KEYWORDS_FILE = "Negative.txt"
PDF_FOLDER = "pdf"

def load_keywords():
    with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

def analyze_pdfs(keywords):
    results = []
    for filename in os.listdir(PDF_FOLDER):
        if not filename.lower().endswith(".pdf"):
            continue
        filepath = os.path.join(PDF_FOLDER, filename)
        try:
            doc = fitz.open(filepath)
            full_text = ""
            for page in doc:
                full_text += page.get_text()
            full_text = full_text.lower()
            count = sum(full_text.count(w) for w in keywords)
            results.append((filename, count))
        except Exception as e:
            print(f"Errore nel file {filename}: {e}")
    return results

def main():
    keywords = load_keywords()
    results = analyze_pdfs(keywords)
    print("Risultati per la categoria: Negative")
    for file, count in results:
        print(f"File: {file}, Occorrenze: {count}")

if __name__ == "__main__":
    main()
