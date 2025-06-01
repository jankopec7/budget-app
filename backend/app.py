from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from models import db
from models.user import User
from models.transaction import Transaction
from routes.auth_routes import auth_bp
from routes.transaction_routes import transaction_bp

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jk:xkop@localhost/budget_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'tajny_klucz'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)

@app.route('/')
def home():
    return jsonify({"message": "Fintracker backend is live!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')



