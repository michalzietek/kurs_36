from file_handler import file_handler, save_state

def get_state():
    return {
        "saldo": file_handler.saldo,
        "ksiegozbior": file_handler.bookstore
    }

def change_saldo(amount):
    saldo = file_handler.saldo
    if saldo + amount < 0:
        raise ValueError("Cannot set balance to negative number")
    saldo += amount
    save_state(file_handler, file_handler.bookstore, saldo)

def borrow_book(isbn_number):
    saldo = file_handler.saldo
    for book in  file_handler.bookstore:
        if book.get("isbn_number") == isbn_number:
            if book.get("quantity_on_stock") <= 0:
                raise ValueError("The book is already rented")

            book["quantity_on_stock"] -= 1
            saldo += 10.0

    save_state(file_handler, file_handler.bookstore, saldo)

def buy_book(book_form):
    isbn = book_form.get("isbn_number")
    author = book_form.get("author")
    title = book_form.get("title")
    quantity = int(book_form.get("quantity"))
    quantity_on_stock = int(book_form.get("quantity"))
    price = float(book_form.get("price"))

    file_handler.bookstore.append({
        "isbn_number": isbn,
        "author": author,
        "title": title,
        "quantity": quantity,
        "quantity_on_stock": quantity_on_stock,
        "price": price
    })

    total_value = quantity * price

    file_handler.saldo -= total_value

    save_state(file_handler, file_handler.bookstore, file_handler.saldo)
