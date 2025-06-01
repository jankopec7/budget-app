from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicjalizacja bazy danych (obiekt db do współdzielenia)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Konfiguracja bazy danych
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jk:xkop@db:5432/budget_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicjalizacja bazy z aplikacją
    db.init_app(app)

    # Import modeli (żeby SQLAlchemy je znał)
    from models.transaction import Transaction

    # Import i rejestracja blueprintów
    from routes.transaction_routes import transaction_bp
    app.register_blueprint(transaction_bp)

    @app.route('/')
    def home():
        return jsonify({"message": "Fintracker backend is live!"})

    # Tworzenie tabel przy pierwszym uruchomieniu (opcjonalnie)
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

