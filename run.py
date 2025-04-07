## run.py is for the local development server.
# For production, use a WSGI server like Gunicorn or uWSGI (wsgi.py).

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    #! REMOVE THE DEBUG=True IN PRODUCTION
    #! USE A PRODUCTION SERVER LIKE GUNICORN OR UWSGI


"""
$ FOR OTHER FILES - DELETE LATER

#app/projects/__init__.py
from flask import Blueprint
from app.projects.project1.routes import project1_bp
from app.projects.project2.routes import project2_bp

def register_project_blueprints(app):
    app.register_blueprint(project1_bp)
    app.register_blueprint(project2_bp)




# app/projects/project1/routes.py
project1_bp = Blueprint('project1', __name__, url_prefix='/projects/project1', template_folder='templates')

@project1_bp.route('/')
def project1_home():
    return render_template('project1/detail.html')
"""
