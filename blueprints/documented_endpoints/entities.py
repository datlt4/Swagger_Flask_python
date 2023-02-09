# blueprints/documented_endpoints/entities.py
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

ns = Namespace("entities", "Entities fake endpoints")

entity_model = ns.model(
    "Entity",
    {
        "id": fields.Integer(readonly=True, description="Entity Identifier"),
        "name": fields.String(required=True, description="Entity Name"),
    },
)

entity_list_model = ns.model(
    "EntityList",
    {
        "entities": fields.Nested(
            entity_model, description="List of entities", as_list=True
        ),
        "total_records": fields.Integer(description="Total number of entities"),
    },
)


entity_example = {"id": 1, "name": "Đặng Thị Huyền Trang"}


@ns.route("")
class EntitiesClass(Resource):
    @ns.marshal_list_with(entity_list_model)
    @ns.response(500, "e86e2 - Internal Server Error")
    def get(self):
        """List with all the entities"""
        return {
            "entities": [entity_example],
            "total_records": len([entity_example]),
        }

    @ns.response(400, "Entity with the given name already exists")
    @ns.response(500, "Internal Server error")
    @ns.expect(entity_model)
    @ns.marshal_with(entity_model, code=HTTPStatus.CREATED)
    def post(self):
        """Create a new entity"""
        if request.json["name"] == "Entity name":
            ns.abort(400, " e8731 - Entity with the given name already exists")

        return entity_example, 201


@ns.route("/<int:entity_id>")
class EntityClass(Resource):
    """Read, update and delete a specific entity"""

    @ns.response(404, "Entity not found")
    @ns.response(500, "Internal Server error")
    @ns.marshal_with(entity_model)
    def get(self, entity_id):
        """Get entity_example information"""

        return entity_example

    @ns.response(400, "Entity with the given name already exists")
    @ns.response(404, "Entity not found")
    @ns.response(500, "Internal Server error")
    @ns.expect(entity_model, validate=True)
    @ns.marshal_with(entity_model)
    def put(self, entity_id):
        """Update entity information"""

        if request.json["name"] == "Entity name":
            ns.abort(400, "Entity with the given name already exists")

        return entity_example

    @ns.response(204, "Request Success (No Content)")
    @ns.response(404, "Entity not found")
    @ns.response(500, "Internal Server error")
    def delete(self, entity_id):
        """Delete a specific entity"""

        return "", 204
