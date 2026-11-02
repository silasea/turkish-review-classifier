from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import BaselineModel

app = FastAPI(title="Turkish Review Classifier")

model = BaselineModel()

class ReviewRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    sentiment: str

@app.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest):
    if not request.text.strip():
        raise HTTPException(status_code=422, detail="Review text cannot be empty.")
    sentiment = model.predict(request.text)
    return PredictionResponse(sentiment=sentiment)