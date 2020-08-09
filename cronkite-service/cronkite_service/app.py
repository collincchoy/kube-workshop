from enum import Enum

from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

from cronkite_service.predict import load_model


app = FastAPI()
model = load_model()


@app.get("/")
async def healthz():
    return {"status": "up"}


class TicketClass(int, Enum):
    upper = 1
    middle = 2
    lower = 3


class Sex(str, Enum):
    male = "male"
    female = "female"


class Passenger(BaseModel):
    ticket_class: TicketClass  # Proxy for socio-economic status
    sex: Sex
    num_siblings: int  # brother, sister, stepbrother, stepsister
    with_spouse: bool  # husband, wife (mistresses and fiancés were ignored)
    num_parents: int
    num_children: int


class PassengerSurvivalPrediction(BaseModel):
    class GuessOption(str, Enum):
        survived = "Survived"
        not_survived = "Did Not Survive"

    guess: GuessOption
    certainty: float


@app.post("/passenger-survival/predict", response_model=PassengerSurvivalPrediction)
async def predict_survival(passenger: Passenger):
    passenger_df = pd.DataFrame(
        [
            {
                "pclass": passenger.ticket_class.value,
                "SibSp": passenger.num_siblings + int(passenger.with_spouse),
                "ParCh": passenger.num_parents + passenger.num_children,
                "sex_female": 1 if passenger.sex == Sex.female else 0,
                "sex_male": 1 if passenger.sex == Sex.male else 0,
            }
        ]
    )
    predictions = model.predict_proba(passenger_df)
    _, survival_proba = predictions[0]  # Only 1 passenger. Discard 0 probability.
    return {
        "guess": PassengerSurvivalPrediction.GuessOption.survived
        if round(survival_proba)
        else PassengerSurvivalPrediction.GuessOption.not_survived,
        "certainty": survival_proba,
    }
