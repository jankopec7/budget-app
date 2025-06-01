from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Rejestracja nowego użytkownika
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: test@example.com
            password:
              type: string
              example: secret123
    responses:
      201:
        description: Rejestracja zakończona sukcesem
      400:
        description: Użytkownik już istnieje
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Registration successful"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Logowanie użytkownika
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: test@example.com
            password:
              type: string
              example: secret123
    responses:
      200:
        description: Zwraca token JWT
        schema:
          type: object
          properties:
            access_token:
              type: string
      401:
        description: Błędne dane logowania
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = create_access_token(identity=email)
        return jsonify({"access_token": token}), 200

    return jsonify({"msg": "Invalid credentials"}), 401
