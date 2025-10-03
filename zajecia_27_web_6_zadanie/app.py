from flask import Flask
from routes import my_blueprint
from database import db
from models import Book, Saldo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ksiegozbior.db"
db.init_app(app)
app.register_blueprint(my_blueprint)

with app.app_context():
    db.create_all()
    saldo_exists = db.session.query(Saldo).first()
    if not saldo_exists:
        saldo = Saldo(amount=10000.00)
        db.session.add(saldo)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)