#!/usr/bin/python3
"""States module"""
from flask import Flask
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage on teardown """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 page not found """
    return {'error': 'Not found'}, 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
