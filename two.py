from flask import jsonify, request
from flask_restful import Resource


class Two(Resource):
    def get(self):
        return_json = {
            "status": 200,
            "msg": "two"
        }
        return jsonify(return_json)