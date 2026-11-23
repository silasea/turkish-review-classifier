"""Central configuration for the review classification service."""

from pathlib import Path

# Project root (one level above src/)
BASE_DIR = Path(__file__).parent.parent

# Model and database locations
MODEL_PATH = BASE_DIR / "models" / "baseline.joblib"
DATABASE_PATH = BASE_DIR / "data" / "analysis_results.db"

# Sentiment classes produced by the models
SENTIMENT_CLASSES = ("Negative", "Neutral", "Positive")

# Input constraints
MAX_REVIEW_LENGTH = 5000