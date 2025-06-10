# Fintracker

**Projekt z przedmiotu: Zaawansowane Techniki Programowania**  
Aplikacja webowa do zarządzania budżetem osobistym — pozwala śledzić przychody, wydatki, analizować finanse i generować wizualizacje.

---
## 🧩 Główne funkcje

- ✅ Dodawanie transakcji (przychody i wydatki)  
- 📂 Kategoryzowanie transakcji (np. *Jedzenie*, *Rozrywka*, *Transport*)  
- 📊 Dashboard z kartami podsumowania
- 🔐 Autoryzacja użytkowników  
- ✅ Historia ostatnich transakcji
- ✅ Kategorie + procentowy udział wydatków
- ✅ Autoryzacja JWT
- ✅ Responsywny UI


---

## 🛠️ Technologie

| Warstwa              | Stos technologiczny                   |
| -------------------- | ------------------------------------- |
| **Frontend**         | Vue 3, Chart.js                       |
| **Backend**          | Flask, Flask-JWT-Extended, SQLAlchemy |
| **Baza danych**      | PostgreSQL                            |
| **Testy**            | Pytest                                |
| **Dokumentacja API** | Flasgger                              |


---

## 🚀 Uruchamianie


Backend:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

