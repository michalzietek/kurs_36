from typing import TypedDict


def count_word_letters(word: str) -> int | None:
    if word == "Michał":
        return len(word)


print(count_word_letters("Michał"))
print(count_word_letters("Michałaasfsgdgfsd"))
#
print(count_word_letters(20))

# count_word_letters()


# class Abstrakcja:
#     def __init__(self, word):
#         self.word = word
#
#     def __len__(self):
#         return len(self.word)
#
#
# abstrakcja = Abstrakcja("Słowo")
#
#
# print(count_word_letters(abstrakcja))

wiek: int = 20

# print(type(wiek))
#
# wiek = "dwadziescia"
#
# print(type(wiek))


class Uczen(TypedDict):
    name: str
    surname: str


lista_uczniow: list[Uczen] = [
    {"name": "Michal", "surname": "Ziętkowski"},
    {"name": "Adam", "surname": "Małysz"},
]
