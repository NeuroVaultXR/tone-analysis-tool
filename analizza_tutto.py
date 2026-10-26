
import os
import fitz  # PyMuPDF

CATEGORIE = [
    "Positive", "Negative", "Uncertainty", "Litigious",
    "Strong_Modal", "Weak_Modal", "Constraining", "Complexity"
]

PDF_FOLDER = "pdf"

def load_keywords(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

def analyze_pdf(file_path, categorie_keywords):
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text().lower()
    risultati = {}
    for categoria, parole in categorie_keywords.items():
        count = sum(text.count(p) for p in parole)
        risultati[categoria] = count
    return risultati

def main():
    # Carica tutte le liste di parole
    categorie_keywords = {}
    for cat in CATEGORIE:
        fname = f"{cat}.txt"
        if not os.path.exists(fname):
            print(f"[!] File parole mancante: {fname}")
            continue
        categorie_keywords[cat] = load_keywords(fname)

    print("Analisi multipla su tutte le categorie:")
    for filename in os.listdir(PDF_FOLDER):
        if not filename.lower().endswith(".pdf"):
            continue
        filepath = os.path.join(PDF_FOLDER, filename)
        print(f"📄 File: {filename}")
        risultati = analyze_pdf(filepath, categorie_keywords)
        for cat, count in risultati.items():
            print(f"  - {cat}: {count}")
        print("-" * 40)

if __name__ == "__main__":
    main()
