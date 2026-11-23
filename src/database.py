"""SQLite storage for sentiment analysis results (FR-06)."""

import sqlite3
from datetime import datetime

import config


def init_database():
    """Create the database file and the analysis_results table if missing."""
    config.DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(config.DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                review_text TEXT NOT NULL,
                predicted_class TEXT NOT NULL,
                timestamp DATETIME NOT NULL
            )
            """
        )


def save_result(review_text: str, predicted_class: str) -> bool:
    """Store one analysis result. Returns False if storage fails."""
    try:
        with sqlite3.connect(config.DATABASE_PATH) as connection:
            connection.execute(
                "INSERT INTO analysis_results "
                "(review_text, predicted_class, timestamp) VALUES (?, ?, ?)",
                (review_text, predicted_class, datetime.now().isoformat()),
            )
        return True
    except sqlite3.Error:
        return False


def get_recent_results(limit: int = 10) -> list[dict]:
    """Return the most recent analysis results."""
    with sqlite3.connect(config.DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT id, review_text, predicted_class, timestamp "
            "FROM analysis_results ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]