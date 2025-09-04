import math

class FiguraGeometryczna:
    def oblicz_pole(self):
        return None

    def oblicz_obwod(self):
        return None

def oblicz_obwod_zaawansowanej_figury(figury: list[FiguraGeometryczna]) -> float:
    obwod = 0
    for figura in figury:
        obwod += figura.oblicz_obwod()
    return obwod

def oblicz_pole_zaawansowanej_figury(figury: list[FiguraGeometryczna]) -> float:
    pole = 0
    for figura in figury:
        pole += figura.oblicz_pole()
    return pole

class Trojkat(FiguraGeometryczna):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return (self.podstawa * self.wysokosc)/2

    def oblicz_obwod(self):
        return self.podstawa + 2 * ((self.podstawa * 0.5) ** 2 + self.wysokosc ** 2) ** 0.5

class Kwadrat(FiguraGeometryczna):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_obwod(self):
        return 4 * self.bok

    def oblicz_pole(self):
        return self.bok ** 2

class Okrag(FiguraGeometryczna):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * self.promien ** 2

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien

trojkat = Trojkat(2, 2)
kwadrat = Kwadrat(10)
okrag = Okrag(25)

print(oblicz_pole_zaawansowanej_figury([trojkat, kwadrat, okrag]))


class Payment:
    def send_wire(self):
        return None

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

payment = Payment()
order = Order("1123", payment)