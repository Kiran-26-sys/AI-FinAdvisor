AI-FinAdvisor 💰

AI-FinAdvisor is a web-based application that helps users analyze their bank statements.
Users can upload PDF/DOCX bank statements, and the app extracts transactions, categorizes them, shows summaries, provides AI-based financial advice, and visualizes spending using charts.

🚀 Features Implemented (so far)

✅ Upload PDF/DOCX bank statements

✅ Extract transactions (date, description, amount, category)

✅ Auto-categorization of transactions (Food, Rent, Bills, etc.)

✅ JSON results displayed neatly in frontend

✅ Transaction list in UI

✅ Spending summary with AI-generated advice

✅ Pie chart visualization of spending by category using Recharts

✅ Basic project structure with Flask backend + React frontend

🛠️ Tech Stack

Backend: Python, Flask, pdfplumber, python-docx

Frontend: React.js, Recharts

Environment: Virtualenv (Python), npm (Node.js)

📂 Project Structure
AI-FinAdvisor/
 ├─ backend/                # Flask backend
 │   ├─ app.py              # Main backend app
 │   ├─ venv/               # Python virtual environment (not pushed to git)
 │   └─ sample_statements/  # Example PDFs/DOCX files
 │
 ├─ frontend/               # React frontend
 │   ├─ src/
 │   │   ├─ App.js          # Main React component
 │   │   └─ ...
 │   └─ package.json
 │
 └─ README.md               # This file

⚙️ Setup Instructions
1. Clone the repository
git clone <repo-link>
cd AI-FinAdvisor

2. Backend Setup (Flask + Python)
cd backend

# Create virtual environment
python -m venv venv

# Activate venv
# Windows (PowerShell)
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install flask flask-cors pdfplumber python-docx

Run backend:
python app.py


Backend will start on: http://127.0.0.1:5000

3. Frontend Setup (React + Node.js)
cd frontend

# Install dependencies
npm install

Run frontend:
npm start


Frontend will start on: http://localhost:3000

✅ Usage

Start backend (Flask server).

Start frontend (React app).

Upload a PDF/DOCX bank statement.

View extracted transactions, summary, AI advice, and spending visualization chart.

🔮 Next Steps (Planned Features)

Email-based OTP authentication for secure login

Calculator module for quick financial calculations

Support for multiple months + trend analysis

Deployment on cloud (Netlify/Vercel for frontend, Railway/Heroku for backend)
