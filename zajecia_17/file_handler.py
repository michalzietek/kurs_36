import json


class CountriesSelector:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def write_data_to_file(self, new_data):
        self.data.append(new_data)
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data, indent=4))

    def lookup_for_country_in_data(self, country_name):
        for country in self.data:
            if country.get("full_name").lower() == country_name.lower():
                return country

    def __getitem__(self, item):
        for country in self.data:
            if country.get("full_name").lower() == item.lower():
                return country

    def __setitem__(self, key, value):
        self.data.append(value)

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for country in self.data:
            yield country.get("full_name"), country
