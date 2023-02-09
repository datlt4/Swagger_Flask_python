# main.py
from flask import Flask, Blueprint, redirect, request, url_for
from blueprints.basic_endpoints import blueprint as basic_endpoints
from blueprints.jinja_endpoint import blueprint as jinja_endpoint
from blueprints.documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config["RESTPLUS_MASK_SWAGGER"] = True

app.register_blueprint(basic_endpoints)
app.register_blueprint(jinja_endpoint)
app.register_blueprint(documented_endpoint)

blueprint = Blueprint("", __name__, url_prefix="/")


@blueprint.route("", methods=["GET"])
def root():
    if request.method == "GET":
        return redirect("/documented_api/doc")


app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
