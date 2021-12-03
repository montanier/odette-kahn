from flask import request, jsonify

from odette_kahn import app
from odette_kahn.model.predict import predict_from_name, predict_from_properties


@app.route('/wine', methods=['GET'])
def get_quality_of_name():
    name = request.get_json()['name']
    return jsonify(predict_from_name(name))


@app.route('/prediction', methods=['GET'])
def get_prediction():
    properties = request.get_json()
    return jsonify(predict_from_properties(properties))
