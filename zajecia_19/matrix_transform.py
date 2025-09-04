'''
**Zadanie: Transformacja Macierzy**
Napisz program, który przetworzy plik CSV zawierający tablicę liczb i zastosuje serię transformacji określonych przez użytkownika. Program powinien odczytać plik wejściowy, zastosować zadane transformacje, a następnie zapisać go do wskazanego pliku wyjściowego.
Uruchomienie programu przez terminal:
python matrix_transform.py <plik_wejsciowy> <plik_wyjsciowy> <transformacja_1> <transformacja_2> ... <transformacja_n>
- <plik_wejsciowy> - nazwa pliku, z którego odczytane zostaną dane, np. data.csv
- <plik_wyjsciowy> - nazwa pliku, do którego zostanie zapisany wynik, np. result.csv
- <transformacja_x> - Transformacja w postaci "operacja, parametry" - operacja może być np. 'add', 'mult', 'div', a parametry będą określały wartości do zastosowania transformacji (np. dla 'add' będą to wartości dodane do każdej komórki w danej kolumnie lub wierszu).
Operacje transformacji:
- add,row,index,value - Dodaj wartość do każdego elementu w wierszu o zadanym indeksie.
- add,col,index,value - Dodaj wartość do każdego elementu w kolumnie o zadanym indeksie.
- mult,row,index,value - Pomnóż każdy element w wierszu przez wartość.
- mult,col,index,value - Pomnóż każdy element w kolumnie przez wartość.

[
    1, 2, 3
    4, 5, 6
    7, 8, 9
]

add, row,0,10

[
    11, 12, 13
    4, 5, 6
    7, 8, 9
]

mult, col,1,5

[
    11, 60, 13
    4, 25, 6
    7, 40, 9
]
'''
import sys
from file_handler import FileHandler, CSVFileHandler, PickleFileHandler

print(sys.argv)
arguments = sys.argv[1:]
print(arguments)
input_file = arguments[0]
output_file = arguments[1]
transformations = arguments[2:]
#
if input_file.endswith(".csv"):
    input_file_handler = CSVFileHandler(input_file, output_file, transformations)
elif input_file.endswith(".pkl"):
    input_file_handler = PickleFileHandler(input_file, output_file, transformations)

if output_file.endswith(".csv"):
    output_file_handler = CSVFileHandler(input_file, output_file, transformations)
elif output_file.endswith(".pkl"):
    output_file_handler = PickleFileHandler(input_file, output_file, transformations)

input_file_handler.read_file()
input_file_handler.do_transformations()
output_file_handler.data = input_file_handler.data
output_file_handler.save_file()

