## 1. Introduction

E-commerce platforms generate substantial amounts of textual customer feedback through product reviews. Analyzing this information can help businesses understand customer satisfaction, evaluate product quality, and identify recurring issues. Natural Language Processing (NLP) provides techniques for automatically processing and classifying such text. This project focuses on developing a Turkish customer review classification service that combines machine learning, an API, automated testing, and containerization.

## 2. Problem Statement

Manually analyzing large volumes of customer reviews requires considerable time and effort. Manual classification can also be inconsistent, making it difficult to identify patterns across thousands of reviews. Consequently, businesses may overlook important complaints or fail to recognize changes in customer sentiment. An automated system is needed to classify Turkish customer reviews consistently and efficiently.

## 3. Motivation

Customer feedback is an important source of information for improving products and services. Efficient review analysis can help businesses recognize customer concerns and make more informed decisions. From a software engineering perspective, this project also provides an opportunity to develop an end-to-end NLP application that combines model training, API development, testing, and reproducible deployment.

## 4. Project Objective

The primary objective is to develop a working NLP service that classifies Turkish e-commerce reviews by sentiment. The project will establish a TF-IDF and Logistic Regression baseline and compare it with a fine-tuned Turkish language encoder. The models will be evaluated using appropriate classification metrics. The selected model will then be integrated into a FastAPI service with a simple user interface, automated tests, and Docker-based packaging.

## 5. Preliminary Scope

The project will include data preprocessing, baseline model development using TF-IDF and Logistic Regression, fine-tuning a Turkish language encoder, model evaluation, REST API development with FastAPI, a simple user interface, automated testing with pytest, and Docker-based containerization. SQLite will be used for lightweight data storage if required by the final application design.

The initial version will focus exclusively on Turkish customer reviews and sentiment classification. User authentication, account management, multilingual support, and cloud deployment are outside the initial scope and may be considered in future work.

## 6. Dataset

The project will initially consider the MüşteriYorumları dataset, which is reported to contain Turkish e-commerce reviews with ratings from one to five stars. The dataset will be examined to assess its structure, label distribution, data quality, and suitability for sentiment classification. The final dataset may be selected or adjusted based on this initial evaluation. The mapping between star ratings and sentiment classes will be determined during preprocessing.
