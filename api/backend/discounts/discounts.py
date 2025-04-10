# Get all discounts from the DB

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict



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
