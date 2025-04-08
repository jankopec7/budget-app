from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicjalizacja aplikacji i bazy danych
app = Flask(__name__)
CORS(app)

# Konfiguracja bazy danych (PostgreSQL, ale można użyć SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jk:xkop@localhost/budget_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modele
from models.transaction import Transaction

@app.route('/')
def home():
    return jsonify({"message": "Fintracker backend is live!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tworzy tabele w bazie danych, jeśli jeszcze nie istnieją
    app.run(debug=True)
