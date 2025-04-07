from flask import Blueprint

shared_bp = Blueprint(
    "shared",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/shared/static",
    url_prefix="/shared",
)
