#!/usr/bin/python3
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns a JSON """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    """ Retrieves the number of each objects by type """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")}
                    )
