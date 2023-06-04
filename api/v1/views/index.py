#!/usr/bin/python3
"""import app views"""

from api.v1.views import app_views
from flask import jsonify

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    """routes to present page status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    """endpoint that retrieves the number of each objects by type"""
    countDict = {}
    for cls in classes:
    countDict[cls] = storage.count(classes[cls])
    return jsonify(countDict)

