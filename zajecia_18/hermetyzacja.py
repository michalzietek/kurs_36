class Zolnierz:
    def __init__(self, imie, nazwisko, rodzaj_broni, dywizja):
        self.imie = imie
        self.nazwisko = nazwisko
        self._rodzaj_broni = rodzaj_broni
        self.__dywizja = dywizja

    def set_dywizja(self, nowa_dywizja):
        if nowa_dywizja not in ["1 dywizja spadochroniarska", "marynarka_wojenna"]:
            raise Exception("Nie chce być w tej dywizji")
        self.__dywizja = nowa_dywizja

    def get_dywizja(self):
        return self.__dywizja


zolnierz = Zolnierz("Michal", "Zietkowski", "pistolet", "12 Dywizja Zmechanizowana")
print(zolnierz._Zolnierz__dywizja)
print(zolnierz.get_dywizja())
zolnierz.set_dywizja("1 a")
print(zolnierz.get_dywizja())
