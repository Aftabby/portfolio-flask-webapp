from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, from Flask!"


@app.route("/sleep-disorder")
def sleep_disorder():
    context = {
        "sample_table": load_sample().head().to_html(index=False),
        "graph_json": graph(),
    }

    return render_template("project2.html", context=context)


if __name__ == "__main__":
    app.run(
        debug=True
    )  # ! IMPORTANT: Remove "debug=True" before deploying to production, though using wsgi.py for Gunicorn is the best practice.
