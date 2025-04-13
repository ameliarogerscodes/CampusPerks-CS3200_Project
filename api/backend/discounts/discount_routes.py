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
