import pytest
from index import app
from flask import json


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


def test_words_counter_two_words(client, headers):
    response = client.post("/counter/words", data=json.dumps({
        "message": "One Two",
    }), headers=headers)
    data = json.loads(response.data)
    assert data["result"] == 2
    assert response.status_code == 200


def test_words_counter_one_word(client, headers):
    response = client.post("/counter/words", data=json.dumps({
        "message": "One",
    }), headers=headers)
    data = json.loads(response.data)
    assert data["result"] == 1
    assert response.status_code == 200


def test_words_counter_no_text(client, headers):
    response = client.post("/counter/words", data=json.dumps({
        "message": "",
    }), headers=headers)
    data = json.loads(response.data)
    assert data["error"] == "At least one word is required."
    assert response.status_code == 400
