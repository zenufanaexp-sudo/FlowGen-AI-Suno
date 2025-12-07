# This file exists to make gunicorn work with the Flask app
# Gunicorn looks for 'app.py' by default, but our main code is in 'main.py'
from main import app

if __name__ == '__main__':
    app.run()
