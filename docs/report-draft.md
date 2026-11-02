## 1. Introduction

E-commerce platforms generate substantial amounts of textual customer feedback through product reviews. Analyzing this information can help businesses understand customer satisfaction, evaluate product quality, and identify recurring issues. Natural Language Processing (NLP) provides techniques for automatically processing and classifying such text. This project focuses on developing a Turkish customer review classification service that combines machine learning, an API, automated testing, and containerization.

## 2. Problem Statement

Manually analyzing large volumes of customer reviews requires considerable time and effort. Manual classification can also be inconsistent, making it difficult to identify patterns across thousands of reviews. Consequently, businesses may overlook important complaints or fail to recognize changes in customer sentiment. An automated system is needed to classify Turkish customer reviews consistently and efficiently.

## 3. Motivation

Customer feedback is an important source of information for improving products and services. Efficient review analysis can help businesses recognize customer concerns and make more informed decisions. From a software engineering perspective, this project also provides an opportunity to develop an end-to-end NLP application that combines model training, API development, testing, and reproducible deployment.

## 4. Project Objective

The primary objective is to develop a working NLP service that classifies Turkish e-commerce reviews by sentiment. The project will establish a TF-IDF and Logistic Regression baseline and compare it with a fine-tuned Turkish language encoder. The models will be evaluated using appropriate classification metrics. The selected model will then be integrated into a FastAPI service with a simple user interface, automated tests, and Docker-based packaging.

## 5. Preliminary Scope

The project will include data preprocessing, baseline model development using TF-IDF and Logistic Regression, fine-tuning a Turkish language encoder, model evaluation, REST API development with FastAPI, a simple user interface, automated testing with pytest, and Docker-based containerization. SQLite will be used for storing sentiment analysis results.

The initial version will focus exclusively on Turkish customer reviews and sentiment classification. User authentication, account management, multilingual support, and cloud deployment are outside the initial scope and may be considered in future work.

## 6. Dataset

The project will use the MüşteriYorumları dataset, which contains approximately 103,000 Turkish e-commerce reviews from Hepsiburada and Trendyol with ratings from one to five stars. The dataset will be examined to assess its structure, label distribution, and data quality. Star ratings will be mapped to three sentiment classes: ratings of 1-2 as Negative, 3 as Neutral, and 4-5 as Positive. This mapping will be verified during dataset inspection by examining representative reviews from each rating level.

## 7. Requirements Analysis

The primary user of this project is a customer experience team member working for an e-commerce business. This user needs to analyze customer reviews to understand customer sentiment and identify negative feedback. Manually reading and classifying large numbers of reviews can be time-consuming and make it difficult to identify negative comments efficiently.

The proposed system will provide a Turkish customer review sentiment classification service. Its main objective is to predict the sentiment class of a Turkish review and return the result to the user. The first prototype will focus on three essential capabilities: accepting review text, classifying the text using a machine learning model, and displaying the predicted sentiment. A simple and functional interface may be included to demonstrate this workflow. More advanced interface design, bulk review uploads, and analysis history will be postponed until the core classification process works reliably. The dataset will be finalized after its suitability and data quality have been evaluated.

## 8. Project Scope

### In Scope

- Accepting Turkish customer reviews as text input.
- Classifying reviews into Positive, Neutral, or Negative sentiment classes.
- Displaying predictions through a FastAPI-based REST API and a simple user interface.
- Comparing a TF-IDF and Logistic Regression baseline with a fine-tuned Turkish language model.
- Evaluating model performance using classification metrics, including macro-F1.
- Storing analysis results in an SQLite database.
- Testing and packaging the application using pytest and Docker.

### Out of Scope

- User authentication and account management.
- Multilingual sentiment classification.
- Bulk review uploads and advanced review analytics.
- Cloud deployment in the initial version.

## 9. Functional Requirements

| ID    | Requirement statement                                                                                           | Priority |
| ----- | --------------------------------------------------------------------------------------------------------------- | -------- |
| FR-01 | The system shall accept a Turkish customer review as text input.                                                | Must     |
| FR-02 | The system shall classify an input review into one of three sentiment classes: Positive, Neutral, or Negative.  | Must     |
| FR-03 | The system shall display the predicted sentiment class to the user.                                             | Must     |
| FR-04 | The system shall reject empty or whitespace-only review input and display a clear validation message.           | Must     |
| FR-05 | The system shall expose the sentiment classification functionality through a REST API implemented with FastAPI. | Must     |
| FR-06 | The system shall store each analysis result in an SQLite database for later retrieval.                          | Should   |

## 10. Non-Functional Requirements

| ID     | Quality                | Requirement                                                                                                                                                                        | How to verify                                                                                                             |
| ------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| NFR-01 | Performance            | The system shall return a sentiment prediction within 2 seconds for a single review of up to 500 characters, excluding initial model loading, on the specified development laptop. | Measure response time across 30 individual requests and check whether each prediction meets the target.                   |
| NFR-02 | Classification quality | The selected model shall achieve a macro-F1 score of at least 0.75 on a held-out test set containing all three sentiment classes.                                                  | Evaluate the trained model on a test set that was not used for training or model selection, and calculate macro-F1.       |
| NFR-03 | Input validation       | The system shall return an appropriate validation error for empty or whitespace-only input without attempting sentiment classification.                                            | Submit empty and whitespace-only inputs through the API and verify the error response and that no prediction is produced. |

## 11. Constraints and Assumptions

### Constraints

**CON-01 — Development Time:** The project must be developed within the nine-week graduation project schedule. Therefore, development will prioritize a working prototype and essential functionality over advanced features.

**CON-02 — Computational Resources:** Model training and fine-tuning will be limited by the available hardware and computational resources. Free cloud GPU services may be used when available, but their availability and usage limits cannot be guaranteed.

### Assumptions

**ASM-01 — Dataset Label Quality:** The selected dataset is assumed to contain sufficiently reliable review ratings for deriving Positive, Neutral, and Negative sentiment labels. This assumption will be examined by inspecting the dataset, its rating distribution, and representative reviews before finalizing the label mapping.

## 12. Use Cases

### US-01: Classify a Customer Review

As a customer experience team member, I want to submit a Turkish customer review and see its predicted sentiment class, so that I can identify the general sentiment expressed in the review.

**Related Requirements:** FR-01, FR-02, FR-03

**Acceptance Criteria**

1. Given a valid Turkish customer review, when the user submits the review, then the system shall classify it as Positive, Neutral, or Negative.
2. Given that the classification process has completed, when the system returns the prediction, then the predicted sentiment class shall be displayed to the user.

### US-02: Handle Empty Review Input

As a customer experience team member, I want to receive a clear validation message when I submit an empty review, so that I can correct my input before requesting a sentiment prediction.

**Related Requirements:** FR-04, NFR-03

**Acceptance Criteria**

1. Given an empty or whitespace-only review, when the user submits it, then the system shall reject the input and display a clear validation message.
2. Given an empty or whitespace-only review, when the API receives the request, then it shall return an appropriate validation error without generating a sentiment prediction.

## 13. Development Plan

| Week   | Planned Deliverable                                                                                                                                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Week 3 | Design the system architecture and document two Architecture Decision Records (ADRs): one explaining the choice of SQLite and the other explaining the selection of BERTurk and the use of a common model interface.                                                       |
| Week 4 | Develop an end-to-end baseline using TF-IDF and Logistic Regression. Load and preprocess the dataset, train the baseline model, and create a basic FastAPI service. Integrate the baseline model into the API and demonstrate sentiment prediction through an API request. |
| Week 5 | Fine-tune BERTurk for three-class Turkish sentiment classification. Integrate it into the existing FastAPI service by replacing the baseline model behind the same prediction interface. Verify that the API continues to work with the new model.                         |
| Week 6 | Implement automated tests using pytest and prepare a comparison table for the baseline and BERTurk models using macro-F1, accuracy, precision, and recall. Evaluate both models on the same held-out test set.                                                             |
| Week 7 | Containerize the application using Docker, maintain a requirements.txt file, and verify that the application runs successfully in a clean environment using documented setup instructions.                                                                                 |
| Week 8 | Complete the graduation project report and improve the GitHub README with the project overview, features, scope, technology stack, installation instructions, usage examples, and evaluation results.                                                                      |
| Week 9 | Prepare and deliver the final project demonstration, showing the end-to-end application workflow, sentiment predictions, model evaluation results, and key engineering decisions.                                                                                          |

## 14. Methodology

### Modeling Approach

The project will follow a simple-to-complex modeling approach. First, a TF-IDF and Logistic Regression model will be developed as a baseline, followed by a fine-tuned BERTurk model. Both models will be accessed through a common interface in the Model Layer, allowing the model to be replaced without changing the API. Their performance will be evaluated using the same test set to ensure a fair comparison.

### Justification

This approach is suitable for a one-person project with a nine-week timeline and limited GPU resources. The TF-IDF and Logistic Regression baseline can be implemented quickly and does not require a GPU, making it possible to build a working system early. The more complex BERTurk model can then be developed as the next step. Even if fine-tuning takes longer than expected, the project will still have a functional baseline system.

## 15. System Architecture

![System architecture](design/architecture.png)

**Figure 3.1:** Proposed system architecture showing the main components and the flow of a review from input to prediction.

Figure 3.1 presents the proposed architecture. The User Interface sends the review text to the FastAPI REST API, where input validation checks whether the text is empty or contains only whitespace. Valid text is forwarded to the Model Layer, which produces a sentiment prediction through the common predict(text) interface. The prediction is returned to the API, which stores the result in the SQLite database and returns the predicted class to the User Interface. If validation fails, a validation error is returned to the user and the Model Layer is not called.

### 15.1 Component Responsibilities

| Component        | Responsibility / main input                                                                                                                                                         | Output / connection                                                                                                                                                              |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User Interface   | Allows the user to enter a Turkish customer review.                                                                                                                                 | Sends the review text to the FastAPI REST API and displays the predicted sentiment or validation error returned by the API.                                                      |
| FastAPI REST API | Receives review text from the User Interface and manages the classification request. Includes input validation to reject empty or whitespace-only text.                             | Sends valid text to the Model Layer; receives the predicted sentiment; stores the analysis result in SQLite; returns the prediction or a validation error to the User Interface. |
| Model Layer      | Processes valid Turkish review text using the selected sentiment classification model. Provides a common predict(text) interface for both TF-IDF + Logistic Regression and BERTurk. | Produces a predicted sentiment class (Positive, Neutral, or Negative) and sends it back to the FastAPI REST API.                                                                 |
| SQLite Database  | Stores analysis results received from the FastAPI REST API, including the review text, predicted sentiment class, and timestamp.                                                    | Stores the analysis records for later retrieval by the application.                                                                                                              |

### System Boundaries

The entire system will run locally on a single machine during development and demonstration. The User Interface, FastAPI REST API, Model Layer, and SQLite Database will operate within this local environment. The main external dependency is the pre-trained language model downloaded from Hugging Face; its availability and hosting are outside the project's direct control. Once downloaded, the model will run locally during application execution.

### 15.2 End-to-End Execution Scenario

| Step | Component                          | Input, operation, and output                                                                                                                      |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | User Interface                     | The user enters a Turkish customer review and submits it to the FastAPI REST API.                                                                 |
| 2    | FastAPI REST API                   | Receives the review text through the /predict endpoint and forwards it to input validation.                                                       |
| 3    | Input Validation (within FastAPI)  | Checks whether the review is empty or contains only whitespace. If valid, forwards the text to the Model Layer.                                   |
| 4    | Model Layer                        | Processes the review using the selected classification model through the common predict(text) interface and returns a sentiment class to the API. |
| 5    | FastAPI REST API / SQLite Database | Receives the predicted sentiment and stores the review text, predicted class, and timestamp in SQLite.                                            |
| 6    | FastAPI REST API / User Interface  | Returns the prediction as an API response. The User Interface displays the predicted sentiment to the user.                                       |

### Example API Endpoint

**Endpoint:** `POST /predict`

Request body:

```json
{
  "text": "Ürün çok kaliteli ve hızlı teslim edildi."
}
```

Successful response (HTTP 200 OK):

```json
{
  "sentiment": "Positive"
}
```

The `sentiment` field can contain one of three values: Positive, Neutral, or Negative.

### Error Scenario: Empty Review Input

If the user submits an empty review or a review containing only whitespace, the FastAPI input validation mechanism rejects the request before it reaches the Model Layer.

Example request:

```json
{
  "text": "   "
}
```

Error response (HTTP 422 Unprocessable Entity):

```json
{
  "detail": "Review text cannot be empty."
}
```

In this scenario the Model Layer is not called, no sentiment prediction is generated, no analysis result is stored in SQLite, and the validation error is returned to the User Interface and displayed to the user.
