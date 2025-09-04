import csv
import pickle
from abc import abstractmethod, ABC

class FileHandler(ABC):
    def __init__(self, input_file, output_file, transformations):
        self.input_file = input_file
        self.output_file = output_file
        self.transformations = transformations
        self.data = None

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            operation = transformation_list[0]
            axis = transformation_list[1]
            index = int(transformation_list[2])
            value = int(transformation_list[3])
            if operation == "add":
                if axis == "row":
                    self.add_row(index, value)
                elif axis == "col":
                    self.add_col(index, value)
            elif operation == "mult":
                if axis == "row":
                    self.mult_row(index, value)
                elif axis == "col":
                    self.mult_col(index, value)

    def add_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] += value

    def add_col(self, index, value):
        for row in self.data:
            row[index] += value

    def mult_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] *= value

    def mult_col(self, index, value):
        for row in self.data:
            row[index] *= value


class CSVFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            matrix = []
            for row in reader:
                temp_row = []
                for number in row:
                    temp_row.append(int(number))
                matrix.append(temp_row)
        self.data = matrix

    def save_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class PickleFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data =  pickle.load(file)

    def save_file(self):
        with open(self.output_file, mode="wb") as file:
            file.write(pickle.dumps(self.data))