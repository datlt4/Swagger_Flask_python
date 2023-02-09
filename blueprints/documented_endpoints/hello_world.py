# blueprints/documented_endpoints/hello_world.py
from flask import request
from flask_restx import Namespace, Resource, fields

ns = Namespace("hello_world", "Getting Started enpoint")

hello_world_model = ns.model(
    "HelloWorld",
    {"message": fields.String(readonly=True, description="Hello world message")},
)


@ns.route("")
class HelloWorldClass(Resource):
    @ns.marshal_with(hello_world_model)
    @ns.response(500, "e40c9 - Internal Server Error")
    def get(self):
        """Hello world message endpoint"""
        return {"message": "Hello World!"}
