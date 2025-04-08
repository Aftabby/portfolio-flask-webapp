# app/__init__.py
# This file initializes the Flask application and registers the blueprints for different routes.
# It serves as the entry point for the application.

from flask import Flask, request, redirect, render_template


def create_app():
    app = Flask(__name__)

    # % Redirect non-www to www globally for all routes
    @app.before_request
    def redirect_non_www():
        if request.host == "aftabby.com":
            return redirect(
                request.url.replace("aftabby.com", "www.aftabby.com"), code=301
            )

    # % For Home Page
    from app.home.routes import (
        home_bp,
    )  # Import and register Blueprints for home page from routes.py file in app/home folder

    app.register_blueprint(home_bp)  # Register the home blueprint

    # % For Shared Assets
    from app.shared import shared_bp

    app.register_blueprint(shared_bp)

    # % For all the projects - Imports the blueprints list for all projects from projects/__init__.py file and register by iterating over them
    from app.projects import project_blueprints

    for blueprint in project_blueprints:
        app.register_blueprint(blueprint)

    # % For 404 Error Page
    # Custom error handler for 404 errors
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    return app


""" #@ Explanation:
    1. Why register shared_bp in app/__init__.py?
        Even though you might not use any specific routes from shared_bp, registering the blueprint does a few important things:
        Template & Static File Lookup: It makes the shared blueprint's template and static folders available to Flask's lookup mechanism. This means that when you reference a file (for example, using url_for('shared.static', filename='...') or extending a template), Flask knows where to find them.
        Namespacing: It assigns a namespace (in this case, 'shared') to your shared assets. This helps avoid conflicts with similarly named files in other blueprints.
"""
