===== StudyAI — Flask App Setup =====

FOLDER STRUCTURE:
  studyai/
  ├── app.py                  ← Main Flask app (run this)
  ├── requirements.txt        ← Python dependencies
  └── templates/
      ├── login.html
      ├── nav_macro.html
      ├── dashboard.html
      ├── calendar.html
      ├── progress.html
      └── download.html

HOW TO RUN:
  1. Install Python (3.8+)
  2. Open terminal in the studyai/ folder
  3. Run:  pip install flask
  4. Run:  python app.py
  5. Open browser: http://127.0.0.1:5000

ROUTES:
  /          → redirects to login
  /login     → Sign In page
  /register  → Register tab
  /dashboard → Dashboard (needs login)
  /calendar  → Calendar  (needs login)
  /progress  → Progress  (needs login)
  /download  → Downloads (needs login)
  /logout    → Clears session → login

NOTE: Users are stored in memory (restart = cleared).
      To persist users, add a database (SQLite/PostgreSQL).
