from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn_number = db.Column(db.String, unique=True)
    author = db.Column(db.Text)
    title = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    quantity_on_stock = db.Column(db.Integer)

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)