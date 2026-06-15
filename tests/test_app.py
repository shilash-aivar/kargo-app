from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthz():
    # TODO: add assertions
    pass


def test_info():
    # TODO: add assertions
    pass


def test_index():
    # TODO: add assertions
    pass
