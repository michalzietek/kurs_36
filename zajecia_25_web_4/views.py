from flask import render_template, Blueprint
from flask.views import MethodView


my_blueprint = Blueprint("my_blueprint", __name__)

class UsersView(MethodView):
    def get(self):
        return render_template("index.html")

    def post(self):
        return "Stworzyliśmy posta"

    def put(self):
        return "Aktualizujemy dane"



my_blueprint.add_url_rule("/my_class", view_func=UsersView().as_view("UsersView"), methods=["GET", "POST", "PUT"])
