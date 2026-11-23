"""FastAPI service exposing Turkish review sentiment classification."""

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

import config
import database
from model import load_active_model

# Holds the loaded model so that it is not rebuilt for every request (NFR-01).
_model = None


def get_model():
    """Return the active model, loading it only the first time it is needed.

    Endpoints receive the model through this function instead of reading a
    module-level variable. That keeps the loading decision in one place and
    allows the tests to supply a lightweight stand-in, so running the test
    suite does not load the 423 MB fine-tuned model.
    """
    global _model
    if _model is None:
        _model = load_active_model()
    return _model


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Prepare the database and load the model before the first request."""
    database.init_database()
    get_model()
    yield


app = FastAPI(title="Turkish Review Classifier", lifespan=lifespan)


class ReviewRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    sentiment: str
    model_name: str
    stored: bool


@app.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest, model=Depends(get_model)):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=422, detail="Review text cannot be empty.")

    if len(text) > config.MAX_REVIEW_LENGTH:
        raise HTTPException(
            status_code=422,
            detail=f"Review text exceeds {config.MAX_REVIEW_LENGTH} characters.",
        )

    sentiment = model.predict(text)
    stored = database.save_result(text, sentiment)

    return PredictionResponse(
        sentiment=sentiment,
        model_name=model.name,
        stored=stored,
    )


@app.get("/history")
def history(limit: int = 10):
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=422, detail="limit must be between 1 and 100.")
    return {"results": database.get_recent_results(limit)}