from flask import Blueprint, render_template
from datetime import datetime

index_blueprint = Blueprint("index", __name__)

@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/index", methods=["GET"])
def index():
    return render_template("index.html", now=datetime.now())
