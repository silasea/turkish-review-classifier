import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "baseline.joblib"

class BaselineModel:
    """TF-IDF + Logistic Regression sentiment classifier."""

    def __init__(self):
        self.pipeline = joblib.load(MODEL_PATH)

    def predict(self, text: str) -> str:
        return self.pipeline.predict([text])[0]