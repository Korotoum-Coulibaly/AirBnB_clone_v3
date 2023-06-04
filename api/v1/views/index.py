#!/usr/bin/python3
"""import app views"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """routes to present page status"""
    return jsonify({'status': 'OK'})
