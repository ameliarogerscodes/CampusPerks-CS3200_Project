########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

users = Blueprint('users', __name__)

@users.route('/prediction/<var01>/<var02>', methods=['GET'])
def predict_value(var01, var02):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')

    returnVal = predict(var01, var02)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response




# Get all users from the DB
@users.route('/users', methods=['GET'])
def get_users():
    current_app.logger.info('users_routes.py: GET /users')
    cursor = db.get_db().cursor()
    cursor.execute('select username, firstName, lastName,\
        password, college, email, phoneNo, birthdate, age, discountsUsed, clubId from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get customer detail for customer with particular userID
@users.route('/users/<username>', methods=['GET'])
def get_user(username):
    current_app.logger.info('GET /users/<username> route')
    cursor = db.get_db().cursor()
    cursor.execute('select username, firstName, lastName,\
        password, college, email, phoneNo, birthdate, age, discountsUsed, clubId where id = {0}'.format(username))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@users.route('/users', methods=['POST'])
def add_new_user():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    username = the_data['username']
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    password = the_data['password']
    college = the_data['college']
    email = the_data['email']
    phoneNo = the_data['phoneNo']
    birthdate = the_data['birthdate']
    age = the_data['age']
    discountsUsed = the_data['discountsUsed']
    clubId = the_data['clubId']

    # Constructing the query
    query = 'insert into products (username, firstName, lastName, password, college, email, phoneNo, birthdate, age, disocuntsUsed, ' \
    'clubId) values ("'
    query += username + '", "'
    query += firstName + '", "'
    query += lastName + '", '
    query += password + '", '
    query += college + '", '
    query += email + '", '
    query += str(phoneNo) + '", '
    query += birthdate + '", '
    query += str(age) + '", '
    query += str(discountsUsed) + '", '
    query += str(clubId) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@users.route('/users', methods=['PUT'])
def update_user():
    current_app.logger.info('PUT /users route')
    user_info = request.json
    # current_app.logger.info(cust_info)
    username = user_info['username']
    firstName = user_info['firstName']
    lastName = user_info['lastName']
    password = user_info['password']
    college = user_info['college']
    email = user_info['email']
    phoneNo = user_info['phoneNo']
    birthdate = user_info['birthdate']
    age = user_info['age']
    discountsUsed = user_info['disocuntsUsed']
    clubId = user_info['clubId']

    query = 'UPDATE users SET firstName = %s, lastName = %s, password = %s,' \
    ' college = %s, email = %s, phoneNo = %s, birthdate = %s, age = %d, discountsUsed = %d,' \
    ' clubId = %d where username = %s'
    data = (firstName, lastName, password, college, email, phoneNo, birthdate, age, discountsUsed, clubId, username)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'user updated!'