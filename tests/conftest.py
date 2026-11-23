"""Shared fixtures for the test suite."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Make the application modules in src/ importable from the tests.
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import config  # noqa: E402
import database  # noqa: E402
from api import app, get_model  # noqa: E402


class FakeModel:
    """Stand-in for a real classifier.

    The tests verify the API's behaviour: validation, storage and response
    format. They do not verify model accuracy, which is measured separately
    on the held-out test set. Using this stand-in keeps the suite fast and
    removes the need to load the 423 MB fine-tuned model.
    """

    name = "fake-model"

    def predict(self, text: str) -> str:
        return "Positive"


@pytest.fixture
def temp_database(tmp_path, monkeypatch):
    """Point the application at an empty database created for one test."""
    database_path = tmp_path / "test_analysis_results.db"
    monkeypatch.setattr(config, "DATABASE_PATH", database_path)
    database.init_database()
    return database_path


@pytest.fixture
def client(temp_database):
    """An API client backed by the temporary database and the fake model."""
    app.dependency_overrides[get_model] = lambda: FakeModel()
    yield TestClient(app)
    app.dependency_overrides.clear()
