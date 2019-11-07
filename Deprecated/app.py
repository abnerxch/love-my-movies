"""
I use manage.py as the main py file
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is a Flask'

if __name__ == "__main__":
    debug=False
    app.run(host="0.0.0.0",debug=debug)