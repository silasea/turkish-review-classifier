"""API tests for the prediction and history endpoints."""

import config


# --- /predict: valid input (FR-01, FR-02, FR-03, FR-05) ---------------------


def test_predict_returns_a_sentiment_class(client):
    """T07 - a valid Turkish review returns one of the three classes."""
    response = client.post(
        "/predict", json={"text": "Ürün çok kaliteli ve hızlı teslim edildi."}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] in config.SENTIMENT_CLASSES


def test_predict_reports_the_model_and_the_storage_status(client):
    """T08 - the response names the active model and confirms storage."""
    response = client.post("/predict", json={"text": "Ürün gayet iyi."})
    body = response.json()

    assert body["model_name"] == "fake-model"
    assert body["stored"] is True


def test_predict_ignores_surrounding_whitespace(client):
    """T09 - leading and trailing spaces are stripped before storage."""
    client.post("/predict", json={"text": "   Ürün iyi.   "})

    assert client.get("/history").json()["results"][0]["review_text"] == "Ürün iyi."


# --- /predict: invalid input (FR-04, NFR-03) --------------------------------


def test_predict_rejects_empty_text(client):
    """T10 - empty input returns HTTP 422."""
    response = client.post("/predict", json={"text": ""})

    assert response.status_code == 422


def test_predict_rejects_whitespace_only_text(client):
    """T11 - whitespace-only input returns HTTP 422."""
    response = client.post("/predict", json={"text": "     "})

    assert response.status_code == 422


def test_predict_rejects_a_missing_text_field(client):
    """T12 - a request body without the text field returns HTTP 422."""
    response = client.post("/predict", json={})

    assert response.status_code == 422


def test_invalid_input_is_not_stored(client):
    """T13 - a rejected request leaves no record behind."""
    client.post("/predict", json={"text": "   "})

    assert client.get("/history").json()["results"] == []


# --- /predict: boundary values ----------------------------------------------


def test_predict_accepts_text_at_the_maximum_length(client):
    """T14 - input of exactly MAX_REVIEW_LENGTH characters is accepted."""
    response = client.post(
        "/predict", json={"text": "a" * config.MAX_REVIEW_LENGTH}
    )

    assert response.status_code == 200


def test_predict_rejects_text_one_character_over_the_maximum(client):
    """T15 - input one character above the limit returns HTTP 422."""
    response = client.post(
        "/predict", json={"text": "a" * (config.MAX_REVIEW_LENGTH + 1)}
    )

    assert response.status_code == 422


# --- /history (FR-06) --------------------------------------------------------


def test_history_is_empty_before_any_prediction(client):
    """T16 - a fresh database returns no records."""
    response = client.get("/history")

    assert response.status_code == 200
    assert response.json()["results"] == []


def test_history_returns_a_stored_prediction(client):
    """T17 - a prediction made through the API appears in the history."""
    client.post("/predict", json={"text": "Ürün çok iyi."})

    results = client.get("/history").json()["results"]

    assert len(results) == 1
    assert results[0]["review_text"] == "Ürün çok iyi."
    assert results[0]["predicted_class"] in config.SENTIMENT_CLASSES


def test_history_limit_bounds_the_number_of_records(client):
    """T18 - the limit parameter is applied."""
    for index in range(4):
        client.post("/predict", json={"text": f"Yorum {index}"})

    assert len(client.get("/history?limit=2").json()["results"]) == 2


def test_history_rejects_a_limit_below_the_minimum(client):
    """T19 - limit=0 returns HTTP 422."""
    assert client.get("/history?limit=0").status_code == 422


def test_history_rejects_a_limit_above_the_maximum(client):
    """T20 - limit=101 returns HTTP 422."""
    assert client.get("/history?limit=101").status_code == 422


def test_history_accepts_the_boundary_limits(client):
    """T21 - limit=1 and limit=100 are both valid."""
    assert client.get("/history?limit=1").status_code == 200
    assert client.get("/history?limit=100").status_code == 200
