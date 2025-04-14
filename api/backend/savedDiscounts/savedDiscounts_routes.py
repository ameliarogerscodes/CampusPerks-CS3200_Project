########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

savedDiscounts = Blueprint('savedDiscounts', __name__)

@savedDiscounts.route('/prediction/<var01>/<var02>', methods=['GET'])
def predict_value(var01, var02):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')

    returnVal = predict(var01, var02)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

<<<<<<< HEAD
# get all saved discounts
=======


>>>>>>> 9966de2 (your commit message here)
@savedDiscounts.route('/savedDiscounts', methods=['GET'])
def get_customers():
    current_app.logger.info('savedDiscounts_routes.py: GET /savedDiscounts')
    cursor = db.get_db().cursor()
    cursor.execute('select id, company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

<<<<<<< HEAD
# Get used/saved discounts page by user 
@savedDiscounts.route('/savedDiscounts/<username>', methods=['GET'])
def get_used_discounts(username):
    current_app.logger.info('GET /savedDiscounts/<username> route')
    cursor = db.get_db().cursor()
    query = '''
        SELECT d.discountId, d.code, d.percentOff, d.item, d.startDate, d.endDate,
               s.name AS storeName, s.category, s.priceRange
        FROM discount_used du
        JOIN discount d ON du.discountId = d.discountId
        JOIN store s ON d.storeId = s.storeId
        WHERE du.username = %s
    '''
    cursor.execute(query, (username,))
    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    json_data = [dict(zip(row_headers, row)) for row in theData]
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get customer detail by userID
@savedDiscounts.route('/savedDiscounts/<username>', methods=['GET'])
def get_savedDiscounts_user(username):
    current_app.logger.info('GET /savedDiscounts/<username> route')
=======
@savedDiscounts.route('/savedDiscounts', methods=['PUT'])
def update_customer():
    current_app.logger.info('PUT /customers route')
    cust_info = request.json
    # current_app.logger.info(cust_info)
    cust_id = cust_info['id']
    first = cust_info['first_name']
    last = cust_info['last_name']
    company = cust_info['company']

    query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s where id = %s'
    data = (first, last, company, cust_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    current_app.logger.info('GET /customers/<userID> route')
>>>>>>> 9966de2 (your commit message here)
    cursor = db.get_db().cursor()
    cursor.execute('select id, first_name, last_name from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# save new discounts for a user
@savedDiscounts.route('/savedDiscounts/<username>', methods=['POST'])
def add_used_discounts():
    current_app.logger.info('POST /savedDiscounts/<username> route')
    the_data = request.json
    username = the_data['username']
    discountId = the_data['discountId']
    query = '''
        INSERT INTO discount_used (username, discountId)
        VALUES ('{username}', {discountId})
    '''
    cursor.execute(query, (username,))
    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    json_data = [dict(zip(row_headers, row)) for row in theData]
    the_response = make_response(jsonify('saved discount added'))
    the_response.status_code = 201
    return the_response

# remove a saved discount
@savedDiscounts.route('/savedDiscounts/<username>/int:disountId', methods=['DELETE'])
def delete_saved_discounts(username, discountId):
    current_app.logger.info('DELETE /savedDiscounts/<username>/<discountId> route')
    query = '''
        DELETE FROM discount_used
        WHERE username = %s AND discountId = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (username, discountId))
    db.get_db().commit()
    the_response = make_response(jsonify('saved discount deleted'))
    the_response.status_code = 200
    return the_response

# get most popular discounts 
@savedDiscounts.route('/savedDiscounts/popular', methods=['GET'])
def get_savedDiscounts_user(username):
    current_app.logger.info('GET /savedDiscounts/popular route')
    query = '''
        SELECT discountId, COUNT(*) AS saves
        FROM discount_used
        GROUP BY discountId
        ORDER BY saves DESC
        LIMIT 5
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# group saved discounts by category 
@savedDiscounts.route('/savedDiscounts/byCategory', methods=['GET'])
def get_saved_by_catgeory():
    current_app.logger.info('GET /savedDiscounts/popular route')
    query = '''
        SELECT s.category, COUNT(*) AS saves
        FROM discount_used du
        JOIN discount d ON du.discountId = d.discountId
        JOIN store s ON d.storeId = s.storeId
        GROUP BY s.category
        ORDER BY saves DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
