# test_app.py

from flask_todo.app import app

def test_home_page():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200