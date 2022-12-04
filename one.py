from flask_restful import Resource
from flask import jsonify, request

class One(Resource):
    def get(self):
        return_json = {
            "status": 200,
            "msg": "one"
        }
        return jsonify(return_json)