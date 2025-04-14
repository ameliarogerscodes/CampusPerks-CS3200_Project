########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict


discounts = Blueprint('discounts', __name__)

# Get all discounts from the DB
@discounts.route('/discounts', methods=['GET'])
def get_discounts():
    current_app.logger.info('GET /discounts route')
    cursor = db.get_db().cursor()

    query = '''
        SELECT discountId, storeId, code, percentOff, item, startDate,
               endDate, ageRestricted, minPurchase, bdayDiscount
        FROM discount
    '''
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


# add a new discount to the DB
@discounts.route('/discounts', methods=['POST'])
def add_discount():
    current_app.logger.info('POST /discounts route')
    data = request.get_json()

    required_fields = ['storeId', 'code', 'percentOff', 'item', 'startDate',
                       'endDate', 'ageRestricted', 'minPurchase', 'bdayDiscount']


    if not all(field in data for field in required_fields):
        return make_response(jsonify({'error': 'Missing required fields'}), 400)

    try:

        query = '''
            INSERT INTO discount (storeId, code, percentOff, item, startDate,
                                  endDate, ageRestricted, minPurchase, bdayDiscount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            data['storeId'],
            data['code'],
            data['percentOff'],
            data['item'],
            data['startDate'],
            data['endDate'],
            data['ageRestricted'],
            data['minPurchase'],
            data['bdayDiscount']
        )


        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        return make_response(jsonify({'message': 'Discount added successfully'}), 201)

    except Exception as e:
        current_app.logger.error(f"Error inserting discount: {e}")
        return make_response(jsonify({'error': 'Failed to add discount'}), 500)


# get a single discount by id
@discounts.route('/discounts/<discountId>', methods=['GET'])
def get_discount_by_id(discountId):
    current_app.logger.info('GET /discounts/<discountId> route')
    cursor = db.get_db().cursor()

    query = '''
        SELECT discountId, storeId, code, percentOff, item, startDate,
               endDate, ageRestricted, minPurchase, bdayDiscount
        FROM discount
        WHERE discountId = %s
    '''
    cursor.execute(query, (discountId,))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# update a discount by ID
@discounts.route('/discounts/<int: discountId>', methods=['PUT'])
def get_discount_by_id(discountId):
    current_app.logger.info('PUT /discounts/<discountId> route')
    data = request.get_json()
    query = '''
        UPDATE discount SET percentOff = %s, endDate = %s
        WHERE discountId = %s
    '''
    values = (
        data['percentOff'], 
        data['endDate'],
        discountId
    )
    cursor = db.get_db().cursor()
    cursor.exceute(query,values)
    db.get_db().commit()
    return 'discount updated succesfully'

# delete a discount by ID 
@discounts.route('/discounts/<int: discountId>', methods=['DELETE'])
def delete_discount(discountId):
    current_app.logger.info('DELETE /discounts/<discountId> route')
    query = '''
        DELETE FROM discount WHERE discountId = %s
    '''
    cursor = db.get_db().cursor()
    cursor.exceute(query, (discountId,))
    db.get_db().commit()
    return 'discount deleted succesfully'

    
