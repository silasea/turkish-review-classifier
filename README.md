# Turkish Customer Review Classification Service

## Project Description

E-commerce platforms receive thousands of customer reviews, making it difficult to manually read, analyze, and categorize all feedback efficiently. Customer reviews contain valuable information about customer satisfaction, product quality, and potential problems. However, analyzing large volumes of unstructured text manually is time-consuming, inconsistent, and difficult to scale. This project develops an automated Natural Language Processing (NLP) system to analyze Turkish customer reviews and identify their sentiment.

## Objective

The objective of this project is to develop a functional and reproducible NLP service that classifies Turkish e-commerce customer reviews by sentiment. The system will compare a baseline machine learning model (TF-IDF with Logistic Regression) against a fine-tuned Turkish language encoder, evaluate both using standard classification metrics, and expose the selected model through a tested REST API with a simple user interface. The application will be containerized with Docker to ensure reproducibility.

## Why Is This Problem Important?

Customer reviews influence purchasing decisions and provide businesses with direct feedback about their products and services. When companies cannot analyze this feedback efficiently, important complaints and recurring problems may go unnoticed. This can delay improvements, reduce customer satisfaction, and lead to business decisions based on incomplete information. An automated sentiment analysis system can help businesses process customer feedback more efficiently and identify general patterns in customer opinions.

## Target Users

The target users are e-commerce businesses, online retailers, customer experience teams, and product managers who need to analyze customer feedback efficiently. The service can help them identify positive and negative customer experiences, monitor customer satisfaction, and extract useful insights from large volumes of Turkish customer reviews. Developers may also use the API to integrate sentiment analysis capabilities into existing e-commerce applications.

## Planned Technologies

- Python
- Hugging Face Transformers (BERTurk)
- scikit-learn
- FastAPI
- SQLite
- Docker
- pytest

## Scope Limitations

The first version will not include user authentication or account management, multilingual support (only Turkish reviews are analyzed), or cloud deployment. These are planned as future work.

## Dataset

The project uses the MüşteriYorumları dataset (103K Turkish e-commerce
customer reviews from Hepsiburada and Trendyol, labeled 1-5 stars).
Star ratings are mapped to three sentiment classes: 1-2 as Negative,
3 as Neutral, and 4-5 as Positive.

## Planned Features

- Sentiment classification of Turkish customer reviews into Positive, Neutral, and Negative
- REST API for submitting reviews and receiving predictions
- Input validation for empty or invalid reviews
- Storage of analysis results
- Comparison of a baseline model and a fine-tuned Turkish language model

## Current Status

Week 2 - Requirements engineering and planning.
