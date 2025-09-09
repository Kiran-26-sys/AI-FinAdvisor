from flask import Flask, request, jsonify
import pdfplumber, docx

app = Flask(__name__)
from flask_cors import CORS
CORS(app)


@app.route("/")
def home():
    return "Backend is running!"

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file.filename.endswith(".pdf"):
        text = extract_pdf(file)
    elif file.filename.endswith(".docx"):
        text = extract_docx(file)
    else:
        return jsonify({"error": "Unsupported format"})

    transactions = parse_transactions(text)
    analysis = analyze_transactions(transactions)

    return jsonify({"transactions": transactions, "analysis": analysis})

import re

def parse_transactions(text):
    """
    Extracts transactions from bank statement text.
    Returns a list of dictionaries: {date, description, amount, category}
    """
    transactions = []

    # Example pattern: 2025-08-01 | Grocery Store | -500
    pattern = r"(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*([+-]?\d+\.?\d*)"
    matches = re.findall(pattern, text)

    for match in matches:
        date, description, amount = match
        amount = float(amount)
        category = categorize(description)
        transactions.append({
            "date": date,
            "description": description,
            "amount": amount,
            "category": category
        })

    return transactions

def categorize(description):
    description = description.lower()
    if "grocery" in description or "food" in description:
        return "Food"
    elif "salary" in description or "credit" in description:
        return "Income"
    elif "shopping" in description or "amazon" in description:
        return "Shopping"
    elif "bill" in description or "electricity" in description:
        return "Bills"
    elif "uber" in description or "ola" in description:
        return "Travel"
    else:
        return "Other"

def analyze_transactions(transactions):
    summary = {}
    total_income = 0
    total_expense = 0

    for t in transactions:
        category = t["category"]
        summary[category] = summary.get(category, 0) + t["amount"]
        if t["amount"] > 0:
            total_income += t["amount"]
        else:
            total_expense += t["amount"]

    savings = total_income + total_expense  # expense is negative

    advice = []
    for category, amt in summary.items():
        if amt < 0 and abs(amt) > 0.5 * abs(savings):  # spending more than 50% of savings
            advice.append(f"High spending in {category}. Consider reducing it.")

    if savings > 0:
        advice.append(f"You saved ₹{savings:.2f} this month. Good job!")
    else:
        advice.append("You spent more than you earned this month. Consider saving more.")

    return {"summary": summary, "total_income": total_income, "total_expense": total_expense, "savings": savings, "advice": advice}

def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

if __name__ == "__main__":
    app.run(debug=True)
