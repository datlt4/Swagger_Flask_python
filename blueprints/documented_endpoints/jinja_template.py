# blueprints/documented_endpoints/jinja_template.py
from flask import request, render_template, make_response
from flask_restx import Namespace, Resource, reqparse

ns = Namespace(
    "jinja_template",
    "Jinja Template page. Note that this is a html page and not a REST API endpoint",
)

parser = reqparse.RequestParser()
parser.add_argument("top", type=str, help="Top text")
parser.add_argument("bottom", type=str, help="Bottom text")


@ns.route("")
class JinjaTemplate(Resource):
    @ns.response(200, "Render jinja template")
    @ns.response(500, "Internal Server error")
    @ns.expect(parser)
    def get(self):
        """Render jinja template page"""

        top = request.args.get("top") if "top" in request.args else ""
        bottom = request.args.get("bottom") if "bottom" in request.args else ""

        return make_response(
            render_template("example.html", top=top, bottom=bottom), 200
        )
