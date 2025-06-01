from flask import Blueprint, request, jsonify
from models import db
from models.transaction import Transaction
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/transactions', methods=['POST'])
@jwt_required()
def add_transaction():
    """
    Dodawanie nowej transakcji
    ---
    tags:
      - Transactions
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - amount
            - category
            - date
          properties:
            amount:
              type: number
              example: 250.75
            category:
              type: string
              example: Salary
            description:
              type: string
              example: Monthly paycheck
            date:
              type: string
              format: date
              example: 2024-06-01
    responses:
      201:
        description: Transakcja dodana pomyślnie
      400:
        description: Błąd dodawania transakcji
    """
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    new_transaction = Transaction(
        amount=data['amount'],
        category=data['category'],
        description=data.get('description'),
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        user_id=user.id
    )

    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully!"}), 201


@transaction_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    """
    Pobierz wszystkie transakcje użytkownika
    ---
    tags:
      - Transactions
    security:
      - Bearer: []
    responses:
      200:
        description: Lista transakcji
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              amount:
                type: number
              category:
                type: string
              description:
                type: string
              date:
                type: string
                format: date
              type:
                type: string
                enum: [income, expense]
    """
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    transactions = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.date.desc()).all()

    result = [{
        'id': t.id,
        'amount': t.amount,
        'category': t.category,
        'description': t.description,
        'date': t.date.strftime('%Y-%m-%d'),
        'type': 'income' if t.amount >= 0 else 'expense'
    } for t in transactions]

    return jsonify(result)
