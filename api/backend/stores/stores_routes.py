########################################################
# Stores blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

stores = Blueprint('stores', __name__)

(stores.route('/stores'))
def get_all_stores():
    cursor = db.get_db().cursor()
    the_query = '''
        SELECT storeId,
            name,
            locationStreet,
            locationCity,
            locationState,
            locationCountry,
            priceRange,
            noOfDiscounts,
            hoursOfOperations,
            category,
            phoneNo,
            website,
            starRating,
            delivery,
            ageRestricted,
            totalSales,
            noOfOrders,
            college
        FROM stores
    '''

    cursor.execute(the_query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response