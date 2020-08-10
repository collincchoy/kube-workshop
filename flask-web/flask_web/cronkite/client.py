import os
import logging

import requests


logger = logging.getLogger(__name__)


def predict(
    sex: str,
    ticket_class: int,
    with_spouse: bool,
    num_siblings: int,
    num_parents: int,
    num_children: int,
):
    logger.info("boop")
    resp = requests.post(
        os.path.join(os.getenv("CRONKITE_HOST"), "passenger-survival/predict"),
        json=dict(
            sex=sex,
            ticket_class=ticket_class,
            with_spouse=with_spouse,
            num_siblings=num_siblings,
            num_parents=num_parents,
            num_children=num_children,
        ),
    )
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        logger.exception("Error talking to Mr. Cronkite.")
        raise

    return resp.json()
