# ########################################################
# Colleges blueprint of endpoints
# ########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

colleges = Blueprint('colleges', __name__)

@colleges.route('/colleges', methods=['GET'])
def get_all_colleges():
    cursor = db.get_db().cursor()
    query = '''
        SELECT 
            collegeId,
            name,
            locationStreet,
            locationCity,
            locationState,
            locationCountry,
            locationZipCode,
            noOfStores,
            noOfUsers,
            domain
        FROM college
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    response = make_response(results)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response