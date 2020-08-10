from flask import Flask, request, render_template


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
    print(request.get_json())
    return {"prediction": {"guess": "Survived", "certainty": 0.8}}
