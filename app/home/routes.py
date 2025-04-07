from flask import Blueprint, render_template

home_bp = Blueprint(
    "home",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/home/static",
    url_prefix="/",
)


@home_bp.route("/")
def home():
    return render_template(
        "index.html"
    )  # This will now look in 'home/templates/index.html'


"""
home_bp = Blueprint("home", __name__, template_folder="templates", url_prefix="/")

'home'	 -- This is the name of the blueprint. It's used internally (e.g. for url_for('home.some_view')).

__name__	--  Tells Flask where this blueprint is defined. It's used to resolve paths like for templates and static files.

template_folder='templates'	 --  This tells Flask: "Look inside this folder (relative to this Python file) for templates (like html files)." So Flask will look in app/home/templates/ if this is defined inside app/home/routes.py.

static_folder='static',  # ✅ This tells Flask where static files live. So if you have CSS or JS files, Flask will look in app/home/static/ for them.

static_url_path='/static', # ✅ Optional: URL prefix for static files. This means that if you have a file in app/home/static/style.css, it will be accessible at /static/style.css.

url_prefix='/'	  --  This says: “All routes in this blueprint will start with /.” So if you change it to '/home', the home route will be at /home/ instead of just /.
"""
