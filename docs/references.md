## ACADEMIC REFERENCES

1. Altinok, D. (2025). Introducing TrGLUE and SentiTurca: A Comprehensive Benchmark for Turkish General Language Understanding and Sentiment Analysis. arXiv:2512.22100. https://arxiv.org/abs/2512.22100

   This paper introduces benchmarks for evaluating Turkish language models on natural language understanding and sentiment analysis tasks. I learned that these benchmarks can help researchers compare different models using standardized evaluation methods. I can use this study to guide my model evaluation and investigate whether its published results are comparable to my own experiments.

2. İncidelen, M., & Aydoğan, M. (2025). Sentiment Analysis in Turkish Using Language Models: A Comparative Study. European Journal of Technique, 15(1), 68–74. https://doi.org/10.36222/ejt.1592448

   This study compares several language models fine-tuned on 150,000 Turkish e-commerce reviews from the TRSAv1 dataset. It reports performance metrics such as accuracy and F1-score, providing a useful reference for selecting a Turkish language model and comparing it with my TF-IDF and Logistic Regression baseline.

3. Arzu, M., & Aydoğan, M. (2023). Comparative Analysis of Transformers Based Architectures for Turkish Sentiment Classification. Journal of Computer Science, IDAP-2023, 1-6. https://doi.org/10.53070/bbd.1350405

   I learned that Transformer-based models can effectively classify Turkish customer reviews into positive, neutral, and negative categories. I will use this study to understand how BERTurk-based architectures perform in Turkish sentiment classification and to support my model selection and evaluation process.

## TECHNICAL REFERENCES

4. Hugging Face. Transformers Documentation. https://huggingface.co/docs/transformers (Accessed: October 2026)

   This documentation explains how to load pretrained language models, fine-tune them for text classification, and evaluate their predictions. I will use it to implement and evaluate the fine-tuned Turkish encoder in my customer review analysis service.

5. Ramírez, S. FastAPI Documentation. https://fastapi.tiangolo.com/ (Accessed: October 2026)

   This documentation explains how to build APIs, validate input data, and test application endpoints. I will use it to develop the API that receives customer reviews, sends them to the sentiment analysis model, and returns the prediction to the user.

6. scikit-learn. scikit-learn: Machine Learning in Python. https://scikit-learn.org/stable/ (Accessed: November 2026)

   I learned that scikit-learn provides tools for text feature extraction, machine learning model training, and model evaluation. I will use this library to build my TF-IDF and Logistic Regression baseline model and evaluate its performance using metrics such as accuracy and F1-score.
