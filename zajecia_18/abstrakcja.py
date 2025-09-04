# import math
import abc
#
#
# class FiguraGeometryczna(abc.ABC):
#
#     @abc.abstractmethod
#     def oblicz_pole(self):
#         return None
#
#     @abc.abstractmethod
#     def oblicz_obwod(self):
#         return None
#
# def oblicz_obwod_zaawansowanej_figury(figury: list[FiguraGeometryczna]) -> float:
#     obwod = 0
#     for figura in figury:
#         obwod += figura.oblicz_obwod()
#     return obwod
#
# def oblicz_pole_zaawansowanej_figury(figury: list[FiguraGeometryczna]) -> float:
#     pole = 0
#     for figura in figury:
#         pole += figura.oblicz_pole()
#     return pole
#
# class Trojkat(FiguraGeometryczna):
#     def __init__(self, podstawa, wysokosc):
#         self.podstawa = podstawa
#         self.wysokosc = wysokosc
#
#     def oblicz_pole(self):
#         return (self.podstawa * self.wysokosc)/2
#
#     def oblicz_obwod(self):
#         return self.podstawa + 2 * ((self.podstawa * 0.5) ** 2 + self.wysokosc ** 2) ** 0.5
#
# class Kwadrat(FiguraGeometryczna):
#     def __init__(self, bok):
#         self.bok = bok
#
#     def oblicz_obwod(self):
#         return 4 * self.bok
#
#     def oblicz_pole(self):
#         return self.bok ** 2
#
# class Okrag(FiguraGeometryczna):
#     def __init__(self, promien):
#         self.promien = promien
#
#     def oblicz_pole(self):
#         return math.pi * self.promien ** 2
#
#     def oblicz_obwod(self):
#         return 2 * math.pi * self.promien
#
#
# class Romb(FiguraGeometryczna):
#     pass
#
# # figura1 = FiguraGeometryczna()
# # figura2 = FiguraGeometryczna()
# # figura3 = FiguraGeometryczna()
# romb = Romb()
# print(oblicz_pole_zaawansowanej_figury([figura1, figura2, figura3]))


class Payment(abc.ABC):
    def __init__(self, amount):
        self.amount = amount

    @abc.abstractmethod
    def send_wire(self):
        return None

    def add_amount_to_temporary_bank_account(self):
        print("Adding amount to temporary bank account to secure the transaction.")

class BLIK(Payment):
    def send_wire(self):
        print("Robimy przelew")

    def generate_code(self):
        print("wygeneruj kod")


class Order:
    def __init__(self, number, payment):
        self.number = number
        self.payment = payment

    def complete(self):
        self.payment.send_wire()

blik = BLIK(123)
order = Order("1123", blik)
order.complete()
blik.add_amount_to_temporary_bank_account()