from flask import Blueprint, render_template, request
from bookstore import  get_state, change_saldo, borrow_book, buy_book
my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        match form_type:
            case "change_balance":
                amount = float(request.form.get("amount"))
                change_saldo(amount)
            case "rent_book":
                isbn_number = request.form.get("isbn_number")
                borrow_book(isbn_number)
            case "add_book":
                form = request.form
                buy_book(form)
            case _:
                raise ValueError("We don't have such a form.")
    stan = get_state()
    return render_template("home_page.html", **stan)