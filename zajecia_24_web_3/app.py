from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {
        "name": "Michal",
        "surname": "Zietkowski",
        "email": "michalzietkowski@gmail.com"
    },
    {
        "name": "Adam",
        "surname": "Malysz",
        "email": "adam_malysz@gmail.com"
    }
]

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/hello")
@app.route("/hello/<name>")
def hello_endpoint(name=None):
    return render_template("hello.html", imie=name)

@app.route("/list_users/", methods=["GET", "POST"])
def list_users():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        users.append({
            "name": name,
            "surname": surname,
            "email": email
        })
    return render_template("users.html", users=users, superuser={"suername": "SUPERMAN"})

if __name__ == "__main__":
    app.run(debug=True)