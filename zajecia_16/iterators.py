from os import get_exec_path
from typing import Iterable, Iterator

lista_uczniow = ["Jan", "Anna", "Piotr", "Kazimierz"]

# print(type(lista_uczniow))
# # for item in lista_uczniow:
# #     print(item)
#
# print(isinstance(lista_uczniow, Iterable))
# print(isinstance(lista_uczniow, Iterator))
#
# iterator = iter(lista_uczniow)
#
# # iterator_v2 = iter(20) <- tak nie można, 20 nie jest iterowalne
# print(isinstance(iterator, Iterator))


# wiek = int(input("Podaj mi swój wiek"))
# print(type(wiek))

# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.iterator = iter(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.iterator)
#
#
# my_iterator = MyIterator(lista_uczniow)
#
# print(isinstance(my_iterator, Iterator))
#
# for imie in my_iterator:
#     print(imie)
#
# print(next(my_iterator))
# print(next(my_iterator))
# print(my_iterator.data)


# def go_through_lista_uczniow(lista_uczniow):
#     for item in lista_uczniow:
#         yield item
#
#
# generator = go_through_lista_uczniow(lista_uczniow)
#
# print(isinstance(generator, Iterator))

lista_uczniow = ["Jan", "Anna", "Piotr", "Kazimierz"]

class MyIterator2:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result

iterator_v2 = MyIterator2(lista_uczniow)
print(next(iterator_v2))
print(next(iterator_v2))
print(next(iterator_v2))
print(next(iterator_v2))
print(next(iterator_v2))