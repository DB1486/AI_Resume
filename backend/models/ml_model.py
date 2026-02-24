import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("backend/data/train.csv")

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", LogisticRegression())
    ])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, "backend/models/classifier.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()