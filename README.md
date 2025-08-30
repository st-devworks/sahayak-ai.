# Sahayak AI – Full Project (Flask Backend + Simple Web UI)

This bundle contains a **Python Flask backend** plus a **simple browser UI** to chat with Sahayak AI.
No separate frontend build tools are required — just run Flask and open your browser.

---

## 🧰 Tech
- Backend: Python 3.9+ • Flask • Flask-CORS • python-dotenv • openai (SDK v1)
- UI: Plain HTML + JavaScript (served by Flask)

---

## ⚙️ Setup (Windows/Mac/Linux)

1) Unzip the archive and open a terminal in the `backend` folder.

2) Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3) Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4) Configure your OpenAI API key:
   - Copy `.env.example` to `.env`
   - Put your key in it:
     ```env
     OPENAI_API_KEY=sk-...your_key...
     ```

5) Run the server:
   ```bash
   python app.py
   ```

6) Open your browser at:
   - http://127.0.0.1:5000  (Home UI)
   - The API endpoint is POST http://127.0.0.1:5000/api/ask

---

## 🚦 API Quick Test (without UI)
Use curl or Postman:
```bash
curl -X POST http://127.0.0.1:5000/api/ask              -H "Content-Type: application/json"              -d '{"query":"Hello Sahayak!"}'
```

---

## 📁 Structure
```
backend/
├─ app.py
├─ requirements.txt
├─ .env.example
├─ templates/
│  └─ index.html
└─ static/
   └─ style.css
```

---

## ✨ Notes
- The UI is intentionally minimal; you can later replace it with React/Next/Vite and still call `/api/ask`.
- If you hit rate limits or errors, check your API key and console logs.
