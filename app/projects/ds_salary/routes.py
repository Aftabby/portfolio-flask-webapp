from flask import Blueprint, render_template
from app.projects.ds_salary.utils import *

ds_salary_bp = Blueprint(
    "ds_salary",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/ds-salary",
    static_url_path="/ds_salary/static",
)


@ds_salary_bp.route("/", methods=["GET"])
def index():
    sample_df = load_sample()
    sample_html = sample_df.to_html(index=False)

    context = {
        "sample_table": sample_html,
        "columns": sample_df.shape[1],
        "rows": 742,
        "graph_json": graph(),
    }

    return render_template("project1.html", context=context)
