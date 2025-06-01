from flask import Blueprint, request, jsonify
from models.transaction import db, Transaction
from datetime import datetime

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    new_transaction = Transaction(
        amount=data['amount'],
        category=data['category'],
        description=data.get('description'),
        date=datetime.strptime(data['date'], '%Y-%m-%d')
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully!"}), 201

@transaction_bp.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    result = []
    for t in transactions:
        result.append({
            'id': t.id,
            'amount': t.amount,
            'category': t.category,
            'description': t.description,
            'date': t.date.strftime('%Y-%m-%d')
        })
    return jsonify(result)
