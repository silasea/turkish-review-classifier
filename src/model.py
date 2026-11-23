"""Model layer: provides a common predict(text) interface for all models."""

import joblib

import config


class ModelLoadError(Exception):
    """Raised when a model cannot be loaded from disk."""


class BaselineModel:
    """TF-IDF + Logistic Regression sentiment classifier."""

    name = "baseline-tfidf-logreg"

    def __init__(self):
        if not config.MODEL_PATH.exists():
            raise ModelLoadError(
                f"Model file not found at {config.MODEL_PATH}. "
                "Run notebooks/baseline.ipynb to train and save the model."
            )
        self.pipeline = joblib.load(config.MODEL_PATH)

    def predict(self, text: str) -> str:
        return self.pipeline.predict([text])[0]