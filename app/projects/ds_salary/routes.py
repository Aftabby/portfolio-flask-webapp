from flask import Blueprint, render_template

ds_salary_bp = Blueprint(
    "ds_salary",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/ds-salary",
    static_url_path="/ds-salary/static",
)


@ds_salary_bp.route("/")
def index():
    return render_template("ds_salary_index.html")
