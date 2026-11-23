# Turkish Customer Review Classification Service

## Project Description

E-commerce platforms receive thousands of customer reviews, making it difficult to manually read, analyze, and categorize all feedback efficiently. Customer reviews contain valuable information about customer satisfaction, product quality, and potential problems. However, analyzing large volumes of unstructured text manually is time-consuming, inconsistent, and difficult to scale. This project develops an automated Natural Language Processing (NLP) system to analyze Turkish customer reviews and identify their sentiment.

## Objective

The objective of this project is to develop a functional and reproducible NLP service that classifies Turkish e-commerce customer reviews by sentiment. The system will compare a baseline machine learning model (TF-IDF with Logistic Regression) against a fine-tuned Turkish language encoder, evaluate both using standard classification metrics, and expose the selected model through a tested REST API with a simple user interface. The application will be containerized with Docker to ensure reproducibility.

## Why Is This Problem Important?

Customer reviews influence purchasing decisions and provide businesses with direct feedback about their products and services. When companies cannot analyze this feedback efficiently, important complaints and recurring problems may go unnoticed. This can delay improvements, reduce customer satisfaction, and lead to business decisions based on incomplete information. An automated sentiment analysis system can help businesses process customer feedback more efficiently and identify general patterns in customer opinions.

## Target Users

The target users are e-commerce businesses, online retailers, customer experience teams, and product managers who need to analyze customer feedback efficiently. The service can help them identify positive and negative customer experiences, monitor customer satisfaction, and extract useful insights from large volumes of Turkish customer reviews. Developers may also use the API to integrate sentiment analysis capabilities into existing e-commerce applications.

## Technologies

| Technology                | Status  | Role                                                  |
| ------------------------- | ------- | ----------------------------------------------------- |
| Python 3.11               | In use  | Main development language                             |
| scikit-learn              | In use  | TF-IDF + Logistic Regression baseline                 |
| Hugging Face Transformers | In use  | BERTurk tokenizer and fine-tuned classification model |
| PyTorch                   | In use  | Fine-tuning and inference for the transformer model   |
| FastAPI + uvicorn         | In use  | REST API and interactive documentation                |
| SQLite                    | In use  | Local storage of analysis results                     |
| pytest                    | Planned | Automated tests (Week 6)                              |
| Docker                    | Planned | Containerization (Week 7)                             |

## Scope Limitations

The first version will not include user authentication or account management, multilingual support (only Turkish reviews are analyzed), or cloud deployment. These are planned as future work.

## Dataset

The project uses the MüşteriYorumları dataset (103K Turkish e-commerce
customer reviews from Hepsiburada and Trendyol, labeled 1-5 stars).
Star ratings are mapped to three sentiment classes: 1-2 as Negative,
3 as Neutral, and 4-5 as Positive.

## Features

Implemented:

- Sentiment classification of Turkish customer reviews into Positive, Neutral, and Negative
- REST API for submitting reviews and receiving predictions
- Input validation for empty, whitespace-only, and over-length reviews
- Storage of analysis results in SQLite, with a `/history` endpoint for retrieval
- Two interchangeable models behind a common `predict(text)` interface, selected through configuration

Planned:

- Automated tests with pytest
- Docker-based packaging
- A simple web user interface

## Model Performance

Both models were evaluated on the same held-out test set, which was not used during training or model selection.

| Model                           | Negative F1 | Neutral F1 | Positive F1 | Macro-F1  |
| ------------------------------- | ----------- | ---------- | ----------- | --------- |
| TF-IDF + Logistic Regression    | 0.781       | 0.562      | 0.864       | 0.736     |
| Fine-tuned BERTurk (**active**) | 0.838       | 0.630      | 0.898       | **0.778** |

Macro-F1 is used as the metric of record because the dataset is imbalanced: a plain accuracy score would be dominated by the majority Positive class. The fine-tuned model meets the project target of 0.75 macro-F1; the baseline does not. Neutral remains the weakest class for both models.

## Project Structure

```
docs/          Report draft and architecture design
evidence/      Screenshots documenting each development stage
notebooks/     baseline.ipynb, berturk_finetuning.ipynb
src/           api.py, model.py, database.py, config.py, explore_data.py
models/        Trained models (not tracked in Git)
data/          Dataset and SQLite database (not tracked in Git)
```

## Installation

```bash
git clone https://github.com/silasea/turkish-review-classifier.git
cd turkish-review-classifier
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Preparing a Model

Trained models are not stored in the repository because of their size. At least one of the two must be produced before the API will start.

**Baseline (CPU, a few minutes):** run all cells in `notebooks/baseline.ipynb`. This saves the trained pipeline to `models/baseline.joblib`.

**Fine-tuned BERTurk (requires a GPU):** run `notebooks/berturk_finetuning.ipynb` in a GPU environment such as Kaggle Notebooks. Download the exported model and extract it to `models/berturk-sentiment/`.

Select which model the API should use by setting `ACTIVE_MODEL` in `src/config.py`:

```python
ACTIVE_MODEL = "berturk"   # or "baseline"
```

Both models expose the same `predict(text)` interface, so switching between them requires no change to the API code.

## Running the Project

```bash
uvicorn api:app --reload --app-dir src
```

The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Usage

### Classify a review

`POST /predict`

```json
{
  "text": "Ürün çok kaliteli ve hızlı teslim edildi."
}
```

Response:

```json
{
  "sentiment": "Positive",
  "model_name": "berturk-finetuned",
  "stored": true
}
```

The `stored` field reports whether the result was written to the database. A storage failure does not prevent a prediction from being returned.

Empty, whitespace-only, or over-length input returns HTTP 422 and the model is not called:

```json
{
  "detail": "Review text cannot be empty."
}
```

### Retrieve stored results

`GET /history?limit=10`

```json
{
  "results": [
    {
      "id": 3,
      "review_text": "Ürün çok kaliteli ve hızlı teslim edildi.",
      "predicted_class": "Positive",
      "timestamp": "2026-11-23T14:12:05.441233"
    }
  ]
}
```

`limit` accepts values between 1 and 100 and defaults to 10.

## Current Status

Week 5 — Fine-tuned BERTurk integrated and active; analysis results stored in SQLite and retrievable through `/history`.

**Known limitations:** Neutral is the weakest class (test precision 0.529). There is no user interface; the API is used through its interactive documentation. No automated tests exist yet. Inference runs on CPU, which is adequate for single predictions but not for high request volumes.
