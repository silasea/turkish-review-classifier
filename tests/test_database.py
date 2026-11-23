"""Unit tests for the SQLite storage layer (FR-06)."""

import config
import database


def test_save_result_stores_the_review_and_its_class(temp_database):
    """T01 - a saved result can be read back with the same values."""
    assert database.save_result("Ürün çok kaliteli.", "Positive") is True

    results = database.get_recent_results()

    assert len(results) == 1
    assert results[0]["review_text"] == "Ürün çok kaliteli."
    assert results[0]["predicted_class"] == "Positive"
    assert results[0]["timestamp"] is not None


def test_get_recent_results_returns_the_newest_record_first(temp_database):
    """T02 - history is ordered from newest to oldest."""
    database.save_result("Birinci yorum.", "Positive")
    database.save_result("İkinci yorum.", "Negative")

    texts = [row["review_text"] for row in database.get_recent_results()]

    assert texts == ["İkinci yorum.", "Birinci yorum."]


def test_get_recent_results_respects_the_requested_limit(temp_database):
    """T03 - the limit argument bounds the number of returned records."""
    for index in range(5):
        database.save_result(f"Yorum {index}", "Neutral")

    assert len(database.get_recent_results(limit=3)) == 3


def test_get_recent_results_is_empty_for_a_new_database(temp_database):
    """T04 - a database with no records returns an empty list."""
    assert database.get_recent_results() == []


def test_save_result_reports_failure_instead_of_raising(temp_database, monkeypatch):
    """T05 - an unwritable database path returns False rather than an exception.

    This is the behaviour FR-06 relies on: storage is secondary to answering
    the user, so a storage failure must not interrupt a prediction.
    """
    monkeypatch.setattr(
        config, "DATABASE_PATH", temp_database.parent / "missing-folder" / "x.db"
    )

    assert database.save_result("Yorum.", "Positive") is False


def test_quotation_marks_in_review_text_are_stored_literally(temp_database):
    """T06 - text containing SQL syntax is stored as data, not executed."""
    review = "Ürün 'iyi' ama kargo kötü; DROP TABLE analysis_results;"

    assert database.save_result(review, "Neutral") is True
    assert database.get_recent_results()[0]["review_text"] == review
