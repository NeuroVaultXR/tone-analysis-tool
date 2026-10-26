# Tone Analysis Tool
**Salvatore Urbano / NeuroVaultXR** · Python · Deterministic document analysis

[Italiano](#italiano) · [English](#english)

## Italiano
Strumento sviluppato con assistenza di ChatGPT per esplorare il linguaggio di bilanci e report di sostenibilità. Elabora localmente PDF con testo estraibile e restituisce conteggi per otto categorie.

### Installazione e uso
1. Installa Python 3.10 o successivo.
2. Scarica il repository, estrailo e apri un terminale nella cartella.
3. Esegui `python -m pip install -r requirements.txt`.
4. Aggiungi nella stessa cartella i tuoi vocabolari autorizzati: `Positive.txt`, `Negative.txt`, `Uncertainty.txt`, `Litigious.txt`, `Strong_Modal.txt`, `Weak_Modal.txt`, `Constraining.txt`, `Complexity.txt`. Formato UTF-8, una voce per riga.
5. Inserisci i PDF nella cartella `pdf`.
6. Dalla cartella del progetto esegui `python analizza_tutto.py`. I risultati appaiono nel terminale. Per una sola categoria usa il relativo script `analizza_*.py`.

### Metodo e limiti
La versione originale usa `str.count` sul testo convertito in minuscolo. Conta sottostringhe non sovrapposte per ciascuna voce, anche dentro altre parole; termini diversi possono contare parti della stessa parola. Non riconosce contesto, negazioni, ironia o significato. I risultati non sono conteggi di parole intere né un punteggio normalizzato.
L'estrazione PDF può alterare spazi e parole. Non è incluso un motore OCR: scansioni prive di testo richiedono una preparazione esterna. Le liste originali sono in inglese; non presumere validità su report italiani. Lo strumento non verifica performance ESG, veridicità o greenwashing.
A parità di testo estratto, vocabolari e versione del software, il conteggio è deterministico.

### Vocabolari e riproducibilità
La configurazione accademica dell'autore contiene 3.890 voci: Positive 347, Negative 2.345, Uncertainty 12, Litigious 903, Strong Modal 19, Weak Modal 27, Constraining 184, Complexity 53. Il totale conta voci nelle categorie, non necessariamente parole uniche.
Le liste furono fornite nel contesto di un corso universitario. Fonte/versione e autorizzazione alla redistribuzione non sono ancora confermate: **non sono incluse nel repository pubblico**. Non viene attribuita a Salvatore Urbano la paternità dei vocabolari.
Le categorie sono compatibili con la famiglia Loughran–McDonald, ma ciò non prova la provenienza di questi file: https://sraf.nd.edu/loughranmcdonald-master-dictionary/
Con liste differenti i risultati non riproducono necessariamente l'analisi originale.
Non inserire report riservati nel repository.

## English
A local Python tool, developed with ChatGPT assistance, for exploring the wording of financial and sustainability reports. Install dependencies with `python -m pip install -r requirements.txt`, add your authorized UTF-8 category lists at the repository root, place text-based PDFs in `pdf/`, then run `python analizza_tutto.py` from that directory.
The eight filenames and original category entry counts are listed above. Original academic word lists are not redistributed until their provenance and distribution conditions are confirmed.
The original algorithm sums case-insensitive substring counts, not whole-word counts. It does not understand context or negation, perform OCR, normalize scores or verify ESG claims. Identical extracted text, lists and software yield deterministic counts. Results depend on PDF text extraction and vocabulary selection.

## Rights and dependencies
Code presented by Salvatore Urbano, developed with AI assistance. No blanket open-source license is granted in this first publication; contact the author for reuse permission. Third-party components retain their own rights. PyMuPDF licensing: https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright

Contact: salvatore.urbano99@gmail.com · https://neurovaultxr.com
