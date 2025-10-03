from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zajecia_27_web_6.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(100))

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    user = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)


# Pseudokod
# class M2MExample(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     model_1 = db.Column(db.Integer, db.ForeignKey("model1.id"))
#     model_2 = db.Column(db.Integer, db.ForeignKey("model2.id"))

with app.app_context():
    db.create_all()

    ### TWORZENIE UŻYTKOWNIKA
    # user = User(username="admin1", password="123", email="myemail@gmail.com")
    # db.session.add(user)
    # db.session.commit()

    ### ODPYTYWANIE O UŻYTKOWNIKA
    # users = db.session.query(User).all()
    users = User.query.all()
    user_1 = User.query.first()

    ### UPDATE
    # user_admin_1 = User.query.filter_by(username="admin1").first()
    # user_admin_1.email = "nowy_email@gmail.com"
    # db.session.add(user_admin_1)
    # db.session.commit()

    ### DELETE
    # db.session.delete(user_admin_1)
    # db.session.commit()



if __name__ == "__main__":
    app.run(debug=True)