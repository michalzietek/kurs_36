import json

class WeatherForecast:
    def __init__(self, file_path):
        self.file_path = file_path
        self.weather_data = self.load_data()

    def load_data(self):
        with open(self.file_path) as file:
            return json.load(file)

    def write_weather_data(self):
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(self.weather_data))

    def __getitem__(self, item):
        city, date = item
        # city = item[0]
        # date = item[1]
        return self.weather_data[city][date]

    def __setitem__(self, key, value):
        city, date = key
        if city not in self.weather_data:
            self.weather_data[city] = {}
        self.weather_data[city][date] = value


weather_forecast = WeatherForecast('example_2.json')
print(weather_forecast["Poznan", "2025-08-21"])

weather_forecast["Poznan", "2025-08-20"] = "Nie pada"
weather_forecast["Warszawa", "2025-08-20"] = "Nie pada"

weather_forecast.write_weather_data()


moj_slownik = {
    ("Poznan", "2025-08-21"): "Nie pada",
}