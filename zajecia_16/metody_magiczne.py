class User:
    def __init__(self, name, surname, age, additnional_info):
        self.name = name
        self.surname = surname
        self.age = age
        self.additional_info = additnional_info

    def przywitaj_sie(self):
        """Metoda przywita użytkownika"""
        print(f"Witaj, {self.name} {self.surname}!")

    def __str__(self):
        """Zwraca reprezentację użytkownika jako string"""
        return f"{self.name} {self.surname}"

    def __repr__(self):
        """Zwraca reprezentację użytkownika jako string do debugowania"""
        return f"User(name={self.name}, surname={self.surname})"

    def __int__(self):
        """Zwraca wiek użytkownika jako int"""
        return self.age

    def __float__(self):
        """Zwraca wiek użytkownika jako float"""
        return float(self.age)

    def __len__(self):
        """Zwraca długość imienia użytkownika"""
        return len(self.name)

    def __getitem__(self, key):
        """Zwraca dodatkową informację użytkownika na podstawie klucza"""
        return self.additional_info[key]

    def __setitem__(self, key, value):
        self.additional_info[key] = value


user = User("Janek", "Kowalski", 30, {"hobby": "programowanie", "miasto": "Warszawa"})
print(user)

print(int(user))
print(float(user))

print(len(user))


print(user.additional_info["hobby"])

print(user["hobby"])  # Użycie metody __getitem__

user["jezyk_programowania"] = "Python"  # Użycie metody __setitem__

print(user.additional_info)

wiek = 18

# def przywitaj_sie(imie):
#     """Funkcja przywita użytkownika"""
#     print(f"Witaj, {imie}!")
#
# przywitaj_sie(user.name)
