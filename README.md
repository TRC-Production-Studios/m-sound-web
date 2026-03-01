# M Sound Solutions – Flask Website

## Projekt starten

```bash
pip install -r requirements.txt
python app.py
```
Dann im Browser: http://127.0.0.1:5000

---

## Produkte bearbeiten

Öffne `data/products.py` und editiere die `PRODUCTS`-Liste.

Jedes Produkt hat folgende Felder:

```python
{
    "id":                "eindeutige-id",          # URL-slug, keine Leerzeichen
    "title":             "Produktname",
    "description":       "Langer Text...",
    "short_description": "Kurze Zusammenfassung",
    "price":             "999 €",
    "tags":              ["live", "profi"],         # für Filter im Shop
    "images": [
        "https://...",                              # erstes Bild = Hauptbild
        "https://...",                              # weitere Bilder (optional)
    ],
    "specs": {                                      # technische Daten (optional)
        "Leistung": "1000W",
        "Gewicht":  "12 kg",
    }
}
```

---

## YouTube-Video ändern

In `app.py` findest du:
```python
YOUTUBE_VIDEO_ID = "dQw4w9WgXcQ"   # ← YouTube-ID hier eintragen
```

Die ID ist der Teil in der YouTube-URL nach `v=`:  
`https://www.youtube.com/watch?v=` **`dQw4w9WgXcQ`**

---

## Team & FAQ anpassen

Ebenfalls in `app.py`:
- `TEAM` – Teammitglieder (Name, Rolle, Bio, Avatar-Kürzel)
- `FAQ` – Fragen & Antworten

---

## Struktur

```
msound/
├── app.py               ← Flask-App, Routen, Team, FAQ, Video-ID
├── requirements.txt
├── data/
│   └── products.py      ← Alle Produkte hier bearbeiten!
├── templates/
│   ├── base.html        ← Navigation + Footer (einmalig)
│   ├── index.html       ← Startseite
│   ├── shop.html        ← Shop-Übersicht
│   ├── product_detail.html ← Produktdetailseite
│   ├── datenschutz.html
│   └── impressum.html
└── static/
    └── images/
        └── logo.png
```
