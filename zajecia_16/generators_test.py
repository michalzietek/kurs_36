import os
import psutil
import csv


def get_process_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)  # Convert bytes to MB


def read_file_to_list(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        return [row for row in csv_reader]


def read_file_to_generator(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            yield row


print(f"Memory usage before reading file: {get_process_memory_usage():.2f} MB")
data_list = read_file_to_list("Electric_Vehicle_Population_Data.csv")
print(f"Memory usage after reading file to list: {get_process_memory_usage():.2f} MB")
del data_list  # Free memory
print(f"Memory usage after deleting list: {get_process_memory_usage():.2f} MB")
data_generator = read_file_to_generator("Electric_Vehicle_Population_Data.csv")
for line in data_generator:
    pass  # Iterate through the generator to consume it
print(
    f"Memory usage after reading file to generator: {get_process_memory_usage():.2f} MB"
)
