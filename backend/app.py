from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import Swagger
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

# Swagger konfiguracja
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # wszystkie endpointy
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"  # <- dokumentacja dostępna pod /docs
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Fintracker API",
        "description": "Dokumentacja API dla budżetowej aplikacji Fintracker",
        "version": "1.0.0",
    },
    "basePath": "/",
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Dodaj token jako: **Bearer &lt;JWT&gt;**"
        }
    }
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)
app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    identity = get_jwt_identity()
    return jsonify({"email": identity})

@app.route('/')
def home():
    return jsonify({"message": "Fintracker backend is live!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')



