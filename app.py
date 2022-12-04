import os

from flask import Flask
from flask_restful import Api
from root import Root
from one import One
from two import Two
from three import Three


app = Flask(__name__)
api = Api(app)

api.add_resource(Root, "/")
api.add_resource(One, "/one")
api.add_resource(Two, "/two")
api.add_resource(Three,"/three")

port = os.environ.get("port")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)