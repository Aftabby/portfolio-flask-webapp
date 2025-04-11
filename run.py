## run.py is for the local development server.
# For production, use a WSGI server like Gunicorn or uWSGI (wsgi.py).

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    #! REMOVE THE DEBUG=True IN PRODUCTION
    #! USE A PRODUCTION SERVER LIKE GUNICORN OR UWSGI (BEST PRACTICE)
