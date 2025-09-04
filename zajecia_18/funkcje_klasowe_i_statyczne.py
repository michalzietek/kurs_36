class Programista:

    kraj = "Polska"

    def __init__(self, imie, nazwisko, jezyk_programowania, firma):
        self.imie = imie
        self.nazwisko = nazwisko
        self.jezyk_programowania = jezyk_programowania
        self.firma = "moja firma krzak"

    def zmien_jezyk_programowania(self, nowy_jezyk):
        self.jezyk_programowania = nowy_jezyk

    @classmethod
    def zmien_kraj_programistow(cls, nowy_kraj):
        cls.kraj = nowy_kraj

    @staticmethod
    def oblicz_pole_trojkata( podstawa, wysokosc):
        return (podstawa * wysokosc)/2


programista_adam = Programista("Adam", "Małysz", "python", "moja firma krzak")
programista_mariusz = Programista("Mariusz", "Pudzianowski", "java", "moja firma krzak")
#
# print(programista_mariusz.firma)
# print(programista_adam.firma)
#
# print(id(programista_adam.firma))
# print(id(programista_mariusz.firma))
#
# programista_mariusz.firma = "Nowa firma wielkiego inwestora"

print(programista_adam.kraj)
print(programista_mariusz.kraj)

print(id(programista_mariusz.kraj))
print(id(programista_adam.kraj))

Programista.kraj = "Słowacja"

Programista.zmien_kraj_programistow("Albania")

print(programista_mariusz.kraj)
print(programista_adam.kraj)

print(id(programista_mariusz.kraj))
print(id(programista_adam.kraj))

# print(programista_mariusz.firma)
# print(programista_adam.firma)
#
# print(id(programista_mariusz.firma))