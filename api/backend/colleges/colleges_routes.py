# ########################################################
# Colleges blueprint of endpoints
# ########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

colleges = Blueprint('colleges', __name__)

# get all colleges
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
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    json_data = []
    for row in results:
        json_data.append(dict(zip(row_headers, row)))
    response = make_response(jsonify(json_data))
    response.status_code = 200
    return response

# get a specfic college, by id

@colleges.route('/colleges/<int:collegeId>', methods=['GET'])
def get_college(collegeId):
    current_app.logger.info('GET /colleges/<int:collegeId> route')
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
        WHERE collegeId = %s
    '''
    cursor.execute(query, (collegeId,))
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    response = make_response(jsonify(json_data))
    response.status_code = 200
    return response

# add a new college
@colleges.route('/colleges', methods=['POST'])
def add_college():
    current_app.logger.info('POST /colleges route')
    the_data = request.json
    name = the_data['name']
    locationStreet = the_data['locationStreet']
    locationCity = the_data['locationCity']
    locationState = the_data['locationState']
    locationCountry = the_data['locationCountry']
    locationZipCode = the_data['locationZipCode']
    noOfStores = the_data['noOfStores']
    noOfUsers = the_data['noOfUsers']
    domain = the_data['domain']

    query = '''
        INSERT INTO college (name, locationStreet, locationCity, locationState, locationCountry,
                             locationZipCode, noOfStores, noOfUsers, domain)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    data = (name, locationStreet, locationCity, locationState, locationCountry, locationZipCode, noOfStores, noOfUsers, domain)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response("college added successfully")
    response.status_code = 201
    return response


# update a college
@colleges.route('/colleges', methods=['PUT'])
def update_college():
    current_app.logger.info('PUT /colleges route')
    the_data = request.json
    collegeId = the_data['collegeId']
    name = the_data['name']
    locationStreet = the_data['locationStreet']
    locationCity = the_data['locationCity']
    locationState = the_data['locationState']
    locationCountry = the_data['locationCountry']
    locationZipCode = the_data['locationZipCode']
    noOfStores = the_data['noOfStores']
    noOfUsers = the_data['noOfUsers']
    domain = the_data['domain']

    query = '''
        UPDATE college
        SET name = %s,
            locationStreet = %s,
            locationCity = %s,
            locationState = %s,
            locationCountry = %s,
            locationZipCode = %s,
            noOfStores = %s,
            noOfUsers = %s,
            domain = %s
        WHERE collegeId = %s
    '''
    data = (collegeId, name, locationStreet, locationCity, locationState, locationCountry, locationZipCode, noOfStores, noOfUsers, domain)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response("college updated successfully")
    response.status_code = 200
    return response

# delete a college by ID
@colleges.route('/colleges/<int:collegeId>', methods=['DELETE'])
def delete_college(collegeId):
    current_app.logger.info('DELETE /colleges/<int:collegeId> route')

    query = '''
        DELETE FROM college WHERE collegeId = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (collegeId, ))
    db.get_db().commit()
    response = make_response("college deleted successfully")
    response.status_code = 200
    return response