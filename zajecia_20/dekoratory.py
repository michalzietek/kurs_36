from pyexpat.errors import messages


def przywitaj_sie(imie):
    print(f"Hello {imie}")

def powiedz_kim_jestes():
    przywitaj_sie("Michal")
    print("Jestem programistą")
    print("Pochodzę ze Stargardu")
    return "To będzie nasza funkcja"

def zaloguj_sie():
    print("loguje sie do systemu bankowego")

# funkcja_1 = powiedz_kim_jestes
# funkcja_1()
#
# powiedz_kim_jestes()

def powiedz_kim_jestes_v2():
    def przywitaj_sie_v2():
        print("helloł!!!")


    print("Witaj nieznajomy!!")


    przywitaj_sie_v2()
    print("Jesteśmy zgubieni!!!")


# powiedz_kim_jestes_v2()
#
#
# def wykonaj_przelew():
#     print("Witaj w naszym banku")
#     zaloguj_sie()
#     print("wykonujemy przelew!!")
#
# def pusc_blika():
#     print("Witaj w naszym banku")
#     zaloguj_sie()
#     print("puszczamy blika!!")
#
# wykonaj_przelew()
#
# pusc_blika()


def dekorator_nr_1(func):
    def wrapper(*args, **kwargs):
        print("Jestesmy przed funkcją!")
        func(*args, **kwargs)
        print("Jestesmy po wykonaniu funkcji")
    return wrapper


@dekorator_nr_1
def przywitaj_sie_z_dekoratorem(imie):
    print(f"Helloł {imie}")


przywitaj_sie_z_dekoratorem("Michal")


def sprawdz_czy_uzytkownik_jest_zalogowany(func):
    def wrapper(*args, **kwargs):
        print("Sprawdza dane użytkownika")
        func(*args, **kwargs)
        print("Wylogowujemy się z systemu")
    return wrapper

@sprawdz_czy_uzytkownik_jest_zalogowany
def zrob_przelew(kwota):
    print("robie przelew")