import json


class FileHandler:
    def __init__(self, state_file):
        self.state_file = state_file
        self.bookstore, self.saldo = self.load_state_file()

    def load_state_file(self):
        with open(self.state_file) as file:
            temporary_data = json.loads(file.read())
            return temporary_data.get("bookstore"), temporary_data.get("saldo")

    def save_state_to_file(self, bookstore, saldo):
        self.bookstore = bookstore
        self.saldo = saldo
        with open(self.state_file, mode="w") as file:
            file.write(json.dumps({
                "saldo": self.saldo,
                "bookstore": self.bookstore
            }))

file_handler = FileHandler("state.json")


def save_state(file_handler, bookstore, saldo):
    file_handler.save_state_to_file(bookstore, saldo)
