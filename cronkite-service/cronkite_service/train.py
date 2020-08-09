from pathlib import Path
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


DATA_DIR = Path().parent / "data"
TRAINING_DATA = DATA_DIR / "train.csv"
OUTPUT_LOCATION = DATA_DIR / "rf_model.pkl"


def extract_features(passenger_df: pd.DataFrame) -> pd.DataFrame:
    feats = ["Pclass", "Sex", "SibSp", "Parch"]
    return pd.get_dummies(passenger_df[feats])


def train_and_save_model(**rfc_kwargs):
    train_df = pd.read_csv(TRAINING_DATA)

    train_X = extract_features(train_df)
    train_Y = train_df["Survived"]

    model = RandomForestClassifier(**rfc_kwargs)
    model.fit(train_X, train_Y)

    with open(OUTPUT_LOCATION, "wb") as f:
        pickle.dump(model, f)

    score = round(model.score(train_X, train_Y) * 100, 2)
    print(f"🎯 Accuracy score: {score}%")


if __name__ == "__main__":
    train_and_save_model(max_depth=5, random_state=1)
