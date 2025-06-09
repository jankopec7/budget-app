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
    Add a new transaction
    ---
    tags:
      - Transactions
    security:
      - Bearer: []
    parameters:
      - in: body
        name: transaction
        required: true
        schema:
          type: object
          required:
            - amount
            - category
            - date
            - type
          properties:
            amount:
              type: number
              example: 100.50
            category:
              type: string
              example: Groceries
            description:
              type: string
              example: Bought food for the week
            date:
              type: string
              format: date
              example: 2024-06-01
            type:
              type: string
              enum: [income, expense]
              example: expense
    responses:
      201:
        description: Transaction added successfully
      400:
        description: Invalid input or type
      404:
        description: User not found
    """
    data = request.get_json()
    print(">>> OTRZYMANE DANE:", data)
    print(">>> AMOUNT PRZED RZUTOWANIEM:", data.get('amount'))
    print(">>> DATA PRZED PARSOWANIEM:", data.get('date'))
    # Walidacja wymaganych pól
    required_fields = ['amount', 'category', 'date', 'type']
    missing_fields = [f for f in required_fields if not data.get(f)]

    if missing_fields:
      return jsonify({"error": f"Missing or empty fields: {', '.join(missing_fields)}"}), 400

    if float(data.get('amount', 0)) == 0:
      return jsonify({"error": "Amount cannot be zero"}), 400
    
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # ✅ Rzutowanie kwoty do float
    try:
        amount = float(data['amount'])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid amount format"}), 400

    if data.get('type') == 'expense':
        amount = -abs(amount)
    elif data.get('type') == 'income':
        amount = abs(amount)
    else:
        return jsonify({"error": "Invalid transaction type"}), 400

    try:
        # ✅ Obsługa dwóch formatów daty
        raw_date = data['date']
        try:
            parsed_date = datetime.strptime(raw_date, '%Y-%m-%d')
        except ValueError:
            parsed_date = datetime.strptime(raw_date, '%d.%m.%Y')

        new_transaction = Transaction(
            amount=amount,
            category=data['category'],
            description=data.get('description'),
            date=parsed_date,
            user_id=user.id
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction added successfully!"}), 201
    except Exception as e:
        import traceback
        traceback.print_exc()  # <- wypisze błąd w terminalu!
        print("BŁĄD:", str(e))  # <- dodatkowy log
        return jsonify({"error": str(e)}), 400


@transaction_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    """
    Get all transactions for the current user
    ---
    tags:
      - Transactions
    security:
      - Bearer: []
    responses:
      200:
        description: List of user transactions
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              amount:
                type: number
                example: 59.99
              category:
                type: string
                example: Utilities
              description:
                type: string
                example: Paid electricity bill
              date:
                type: string
                format: date
                example: 2024-06-05
              type:
                type: string
                enum: [income, expense]
                example: expense
      404:
        description: User not found
    """
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    transactions = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.date.desc()).all()

    result = [{
        'id': t.id,
        'amount': abs(t.amount),
        'category': t.category,
        'description': t.description,
        'date': t.date.strftime('%Y-%m-%d'),
        'type': 'income' if t.amount >= 0 else 'expense'
    } for t in transactions]

    return jsonify(result)
