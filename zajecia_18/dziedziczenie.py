class Pierwotne:
    def przywitaj_sie(self):
        print("Jestem stworzeniem pierwotnym!!!")

class Zwierze(Pierwotne):
    def __init__(self, imie):
        self.imie = imie

    # def przywitaj_sie(self):
    #     print("Przedstawiam się!!!")
    #     print("Witaj w zoo w Nowym Yorku!")
    #     print(f"Jestem {self.imie}")


class Ssak:
    def __init__(self, imie):
        self.imie = imie

    def przywitaj_sie(self):
        print("Jestem ssakiem!!")

    def daj_mleko(self):
        print("Daję mleko!!!")


class Lew(Ssak, Zwierze):

    # def przywitaj_sie(self):
    #     print("Jestem królem dżungli!!!")

    def daj_glos(self):
        print("Rawrrrrr")

class Pingwin(Zwierze):

    def daj_glos(self):
        print("Pi pi pi")

lew = Lew("Alex")

pingwin = Pingwin("Kowalski")

lew.przywitaj_sie()
# pingwin.przywitaj_sie()
lew.daj_mleko()