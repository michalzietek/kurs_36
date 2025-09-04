# try:
#     wiek = int(input("Podaj mi swoj wiek: "))
#     lista_uczniow = ["Michal", "Kasia", "Romek"]
#     print(lista_uczniow[3])
#     print(f"Twój wiek to: {wiek}")
# # except ValueError:
# #     print("Niestety wpisałeś zły wiek!!")
# # except IndexError:
# #     print("Twój uczeń nie jest na liście!")
# except (ValueError, IndexError):
#     print("Twój program nie działa prawidłowo!")
# # wiek = int(input("Podaj mi swój wiek: "))

try:
    file = open("moj_plik.txt")
    data = file.read()
except ValueError:
    print("Cos masz zle")
finally:
    print("To się zawsze wykona!!")
    file.close()
