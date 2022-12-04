import os
import socket

from flask_restful import Resource
from flask import jsonify, request


class Root(Resource):
    def get(self):
        return_json = {
            "status": 200,
            "HostName": socket.gethostname()
        }
        return jsonify(return_json)