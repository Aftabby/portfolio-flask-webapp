from flask import Blueprint, render_template
from app.projects.sleep_disorder.utils import *

sleep_disorder_bp = Blueprint(
    "sleep_disorder",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/sleep-disorder",
    static_url_path="/sleep_disorder/static",
)


@sleep_disorder_bp.route("/", methods=["GET"])
def index():
    context = {
        "sample_table": load_sample().head().to_html(index=False),
        "graph_json": graph(),
    }

    return render_template("project2.html", context=context)
