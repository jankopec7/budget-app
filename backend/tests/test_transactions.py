import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models.user import User
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['JWT_SECRET_KEY'] = 'test-secret'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(email='tests@example.com')
            user.set_password('testpass')

            db.session.add(user)
            db.session.commit()
        yield client

def test_add_transaction(client):
    with app.app_context():
        user = User.query.filter_by(email='tests@example.com').first()
        token = create_access_token(identity=user.email)

    payload = {
        "amount": 100.0,
        "category": "Test",
        "description": "Test transaction",
        "date": "2024-06-01",
        "type": "income"
    }

    response = client.post(
        "/transactions",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 201
    assert b"Transaction added successfully" in response.data

