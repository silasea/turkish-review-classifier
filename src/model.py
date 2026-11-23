"""Model layer: provides a common predict(text) interface for all models."""

import joblib
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

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


class BERTurkModel:
    """Fine-tuned BERTurk sentiment classifier."""

    name = "berturk-finetuned"
    MAX_LENGTH = 128

    def __init__(self):
        if not config.BERTURK_PATH.exists():
            raise ModelLoadError(
                f"Fine-tuned model not found at {config.BERTURK_PATH}. "
                "Train it with the Kaggle notebook and place the exported folder there."
            )
        self.tokenizer = AutoTokenizer.from_pretrained(config.BERTURK_PATH)
        self.model = AutoModelForSequenceClassification.from_pretrained(config.BERTURK_PATH)
        self.model.eval()

    @torch.no_grad()
    def predict(self, text: str) -> str:
        inputs = self.tokenizer(
            text,
            truncation=True,
            max_length=self.MAX_LENGTH,
            return_tensors="pt",
        )
        logits = self.model(**inputs).logits
        predicted_id = int(logits.argmax(dim=-1))
        return self.model.config.id2label[predicted_id]


def load_active_model():
    """Return the model selected by config.ACTIVE_MODEL."""
    if config.ACTIVE_MODEL == "berturk":
        return BERTurkModel()
    if config.ACTIVE_MODEL == "baseline":
        return BaselineModel()
    raise ModelLoadError(
        f"Unknown ACTIVE_MODEL '{config.ACTIVE_MODEL}'. Use 'baseline' or 'berturk'."
    )