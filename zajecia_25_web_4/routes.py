from flask import render_template, Blueprint

nasz_blueprint = Blueprint("nasz_blueprint",__name__)

@nasz_blueprint.route("/")
def main():
    return render_template("index.html")