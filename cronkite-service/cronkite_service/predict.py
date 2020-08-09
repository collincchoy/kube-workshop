import pickle

import sklearn

from cronkite_service.train import OUTPUT_LOCATION


def load_model() -> sklearn.ensemble.RandomForestClassifier:
    with open(OUTPUT_LOCATION, "rb") as pickled_model_file:
        return pickle.load(pickled_model_file)
