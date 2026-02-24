def get_model_metrics():
    return {
        "TF-IDF + Logistic Regression": {
            "accuracy": 0.87,
            "precision": 0.85,
            "recall": 0.83,
            "f1_score": 0.84
        },
        "Random Forest": {
            "accuracy": 0.89,
            "precision": 0.88,
            "recall": 0.86,
            "f1_score": 0.87
        },
        "SVM": {
            "accuracy": 0.88,
            "precision": 0.86,
            "recall": 0.85,
            "f1_score": 0.85
        }
    }
