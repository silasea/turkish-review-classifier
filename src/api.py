"""FastAPI service exposing Turkish review sentiment classification."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import config
import database
from model import load_active_model

app = FastAPI(title="Turkish Review Classifier")

# The model is loaded once at startup, not per request (NFR-01)
model = load_active_model()


@app.on_event("startup")
def startup():
    database.init_database()


class ReviewRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    sentiment: str
    model_name: str
    stored: bool


@app.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest):
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