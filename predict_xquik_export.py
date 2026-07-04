import argparse
import csv
import pickle
import sys
from pathlib import Path

from xquik_import import XquikImportError, load_xquik_texts


def load_artifact(path):
    try:
        import joblib
    except ModuleNotFoundError:
        with path.open("rb") as file:
            return pickle.load(file)
    return joblib.load(path)


def main():
    parser = argparse.ArgumentParser(
        description="Predict sentiment for tweets from a Xquik CSV, JSON, or JSONL export."
    )
    parser.add_argument("export", type=Path)
    parser.add_argument("--model", type=Path, default=Path("sentiment_model.pkl"))
    parser.add_argument("--vectorizer", type=Path, default=Path("tfidf_vectorizer.pkl"))
    args = parser.parse_args()

    try:
        with args.export.open("rb") as source:
            texts = load_xquik_texts(source)
    except XquikImportError as error:
        raise SystemExit(str(error)) from error

    model = load_artifact(args.model)
    vectorizer = load_artifact(args.vectorizer)
    features = vectorizer.transform(texts)
    predictions = model.predict(features)

    writer = csv.writer(sys.stdout)
    writer.writerow(["text", "sentiment"])
    writer.writerows(zip(texts, predictions))


if __name__ == "__main__":
    main()
