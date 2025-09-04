from abc import ABC, abstractmethod

class Plywajace(ABC):
    @abstractmethod
    def plywaj(self):
        pass

class Latajace(ABC):
    @abstractmethod
    def lataj(self):
        pass

class Ssak(ABC):
    @abstractmethod
    def rozmnoz_sie(self):
        pass

class Gad(ABC):
    @abstractmethod
    def zloz_jaja(self):
        pass


class Wieloryb(Plywajace, Ssak):
    def plywaj(self):
        print("plywam")

    def rozmnoz_sie(self):
        print("rozmnazam się")

class Zolw(Plywajace, Gad):
    def zloz_jaja(self):
        pass

    def plywaj(self):
        pass