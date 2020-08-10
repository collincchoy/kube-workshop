import logging

from flask import Flask, request, render_template

from flask_web.cronkite import client


logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/healthz")
def health_check():
    return {"status": "up"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    logger.info(request.get_json())
    req = request.get_json()
    predict_params = {
        "sex": req.get("sex", "female"),  # sure
        "ticket_class": int(req.get("ticket_class", 2)),  # middle
        "with_spouse": req.get("with_spouse", False),
        "num_siblings": int(req.get("num_siblings", 0)),
        "num_parents": int(req.get("num_parents", 0)),
        "num_children": int(req.get("num_children", 0)),
    }

    return {"prediction": client.predict(**predict_params)}
