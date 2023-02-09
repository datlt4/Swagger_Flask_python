# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restx import Api
from .hello_world import ns as hello_world_ns
from .entities import ns as entities_ns
from .jinja_template import ns as jinja_template_ns

blueprint = Blueprint("documented_api", __name__, url_prefix="/documented_api")

api_extension = Api(
    blueprint,
    title="Flask RESTplus Demo",
    version="1.0",
    description="Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation",
    doc="/doc",
)

api_extension.add_namespace(hello_world_ns)
api_extension.add_namespace(entities_ns)
api_extension.add_namespace(jinja_template_ns)
