from flask import request, jsonify

from odette_kahn import app
from odette_kahn.model.predict import predict_from_name


@app.route('/wine', methods=['GET'])
def get_quality_of_name():
    name = request.get_json(force=True)['name']
    return jsonify(predict_from_name(name))
