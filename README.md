# Tone Analysis Tool
**NeuroVaultXR · Python · Analisi deterministica**

[Italiano](#italiano) · [English](#english)

## Italiano
Uno strumento per esplorare il linguaggio di bilanci e report di sostenibilità. Elabora localmente PDF con testo estraibile e restituisce conteggi lessicali in otto categorie.

### Installazione e uso
1. Installa Python 3.10 o successivo.
2. Scarica il repository, estrailo e apri il terminale nella cartella del progetto.
3. Installa le dipendenze con `python -m pip install -r requirements.txt`.
4. Aggiungi nella cartella principale i vocabolari che sei autorizzato a usare, in formato UTF-8 con una voce per riga:

   `Positive.txt`, `Negative.txt`, `Uncertainty.txt`, `Litigious.txt`, `Strong_Modal.txt`, `Weak_Modal.txt`, `Constraining.txt`, `Complexity.txt`.

5. Inserisci i documenti nella cartella `pdf`.
6. Esegui `python analizza_tutto.py`. I risultati appaiono nel terminale. Puoi analizzare una sola categoria con il relativo script `analizza_*.py`.

**I vocabolari originali non sono inclusi nel repository:** per utilizzare lo strumento occorre aggiungere proprie liste autorizzate. La lingua dei documenti deve essere coerente con quella dei vocabolari.

### Come leggere i risultati
Il conteggio è deterministico: a parità di testo estratto, vocabolari e versione del software restituisce gli stessi risultati. Conta le corrispondenze testuali anche all’interno di parole più lunghe, senza interpretare il contesto o le negazioni.

I conteggi aiutano a esplorare il linguaggio, ma non verificano le dichiarazioni o le prestazioni ESG. I risultati dipendono dai vocabolari e dalla qualità del testo estratto. Le scansioni senza testo richiedono un OCR preliminare, non incluso nel tool.

## English
A local Python tool for exploring the language of financial and sustainability reports through lexical counts in eight categories.

### Setup and use
1. Install Python 3.10 or later and download the repository.
2. Open a terminal in the project folder and run `python -m pip install -r requirements.txt`.
3. Add your authorized UTF-8 word lists at the repository root, using the eight filenames listed above and one entry per line.
4. Place text-based PDFs in `pdf/` and run `python analizza_tutto.py`. Results appear in the terminal; individual category scripts are also available.

**Original word lists are not included.** You must supply authorized lists whose language matches your documents.

The method is deterministic for identical extracted text, lists and software. It counts text matches, including those within longer words, without interpreting context or negation. Results support language exploration, not verification of ESG claims or performance. Image-only scans require separate OCR before analysis.

## Rights and dependencies
Developed by Salvatore Urbano with AI assistance. No general open-source license is granted for this code; contact the author for reuse permission. Third-party components and word lists retain their own rights.

[PyMuPDF licensing information](https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright)

Contact: neurovaultxr@gmail.com · https://neurovaultxr.com
