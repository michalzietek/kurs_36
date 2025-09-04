from abc import ABC, abstractmethod

class Ptak:
    def lataj(self):
        return "Lecę!"

class Golab(Ptak):
    def zjedz_cos(self):
        print("Jem ziarna")

class Sikorka(Ptak):
    def daj_glos(self):
        print("pipipipipipi")

class Strus(Ptak):
    def schowaj_glowe(self):
        print("Chowam głowę w ziemię!")

class Ptak2(ABC):
    @abstractmethod
    def zloz_jajo(self):
        pass

class LatajacyPtak(Ptak2):
    @abstractmethod
    def lataj(self):
        pass

class NielatajacyPtak(Ptak2):
    @abstractmethod
    def biegaj(self):
        pass

class Strusv2(NielatajacyPtak):

    def biegaj(self):
        print("biegam szybko")

    def zloz_jajo(self):
        print("skladam jajo strusie")

class Wrobel(LatajacyPtak):
    def lataj(self):
        print("Ja latam!")

    def zloz_jajo(self):
        print("Skladam male jajko wrobla!")