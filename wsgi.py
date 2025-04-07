# wsgi.py

from app import create_app

app = create_app()

# This exposes "app" to the WSGI server
