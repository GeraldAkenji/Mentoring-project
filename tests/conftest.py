import pytest
from app import app as FlaskApp


@pytest.fixture()
def app():
    yield FlaskApp


@pytest.fixture
def client(app):
    return app.test_client()