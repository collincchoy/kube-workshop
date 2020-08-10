# Hi, my name is Walter

I'm reporting the fates of passengers aboard a disastrous cruise ship accident.
For more on this, stay tuned.

## Setup

Required:

- Python3.7+
- Poetry

### Install Dependencies

```
poetry install
```

### Train model

To handle incoming prediction requests in real-time, we should pre-train the ML model.
The following command will train a `sklearn.ensemble.RandomForestClassifier` using
the training data in `data/train_csv` from the Titanic (taken from [here](https://www.kaggle.com/c/titanic/data)).
That model gets pickled and saved to `data/rf_model.pkl`. The model is trained to predict survival on the features: ["Pclass", "Sex", "SibSp", "Parch"]

```
poetry run train_cronkite
```

### Serve the model

Run the webserver using `uvicorn`.

```
poetry run uvicorn cronkite_service.app:app
```

Now go to `localhost:8000/docs` or `localhost:8000/redoc` to view and test the service.
