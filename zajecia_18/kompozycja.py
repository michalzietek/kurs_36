class Samochod:
    def __init__(self, silnik, karoseria, opony, drzwi):
        self.silnik = silnik
        self.opony = opony
        self.karoseria = karoseria
        self.drzwi = drzwi

    def uruchom(self):
        print("Otworz drzwi")
        self.drzwi.otworz_drzwi()
        print("Uruchom silnik")
        self.silnik.wlacz_silnik()

    def wylacz(self):
        print("Wyłącz silnik")
        self.silnik.wylacz_silnik()
        print("Zamknij drzwi")
        self.drzwi.zamknij_drzwi()

class Silnik:
    def __init__(self, pojemnosc, moc):
        self.moc = moc
        self.pojemnosc = pojemnosc
        self.status = "wyłączony"

    def wlacz_silnik(self):
        self.status = "włączony"
        print("Silnik włączony")

    def wylacz_silnik(self):
        self.status = "wylaczony"

class Drzwi:
    def __init__(self, kolor):
        self.kolor = kolor
        self.status = "zamkniete"

    def otworz_drzwi(self):
        print("otwieram drzwi")

    def zamknij_drzwi(self):
        print("zamykam drzwi")

silnik_20_tdi = Silnik(pojemnosc="2.0", moc="150KM")
silnik_32_tfsi = Silnik(pojemnosc="3.2", moc="230KM")

drzwi_1 = Drzwi("niebieskie")
drzwi_2 = Drzwi("czarne")
drzwi_3 = Drzwi("niebieskie")
drzwi_4 = Drzwi("niebieskie")

samochod = Samochod(silnik_20_tdi, "niebieska", "zimowe", drzwi_1)
samochod_drozszy = Samochod(silnik_32_tfsi, "czarny", "letnie", drzwi_2)
samochod.uruchom()