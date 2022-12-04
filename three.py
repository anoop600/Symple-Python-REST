from flask_restful import Resource
from flask import jsonify, request


class Three(Resource):
    def get(self):
        return_json = {
            "status": 200,
            "msg": "three"
        }
        return jsonify(return_json)