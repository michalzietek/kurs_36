# from file_handler import file_handler, save_state
#
def get_state():
    return {
        "saldo": db.session.query(Saldo).first().amount,
        "ksiegozbior": db.session.query(Book).all()
    }

from models import db, Saldo, Book

def change_saldo(amount):
    saldo: Saldo = db.session.query(Saldo).first()
    if saldo + amount < 0:
        raise ValueError("Cannot set balance to negative number")
    saldo.amount += amount
    db.session.add(saldo)
    db.session.commit()

def borrow_book(isbn_number):
    saldo: Saldo = db.session.query(Saldo).first()
    bookstore: list[Book] = db.session.query(Book).all()
    for book in bookstore:
        if book.isbn_number == isbn_number:
            if book.quantity_on_stock <= 0:
                raise ValueError("The book is already rented")

            book.quantity_on_stock -= 1
            saldo.amount += 10.0
            db.session.add(book)

    db.session.add(saldo)
    db.session.commit()


def buy_book(book_form):
    isbn = book_form.get("isbn_number")
    author = book_form.get("author")
    title = book_form.get("title")
    quantity = int(book_form.get("quantity"))
    quantity_on_stock = int(book_form.get("quantity"))
    price = float(book_form.get("price"))

    saldo: Saldo = db.session.query(Saldo).first()

    book = Book(isbn_number = isbn,
                author=author,
                title=title,
                quantity=quantity,
                quantity_on_stock=quantity_on_stock,
                price=price)


    total_value = quantity * price
    saldo.amount -= total_value
    db.session.add(book)
    db.session.add(saldo)
    db.session.commit()


