from flask import Blueprint, render_template
from app.projects.ecomm_delivery.utils import *

ecomm_delivery_bp = Blueprint(
    "ecomm_delivery",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/ecomm-delivery",
    static_url_path="/ecomm_delivery/static",
)


@ecomm_delivery_bp.route("/", methods=["GET"])
def index():
    context = {
        "sample_table": load_sample().head().to_html(index=False),
        "graph_json": graph(),
    }

    return render_template("project3.html", context=context)
