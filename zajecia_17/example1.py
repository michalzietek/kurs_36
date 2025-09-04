import json


class WeatherForecast:
    def __init__(self, file_path):
        self.file_path = file_path
        self.weather_data = self.load_data()

    def load_data(self):
        with open(self.file_path) as file:
            return json.load(file)

    def write_weather_data(self):
        with open(self.file_path, "w") as file:
            file.write(json.dumps(self.weather_data))

    def __getitem__(self, item):
        return self.weather_data[item]

    def __setitem__(self, key, value):
        self.weather_data[key] = value


weather_forecast = WeatherForecast("example_1.json")
print(weather_forecast["2025-08-07"])

weather_forecast["2025-08-21"] = "Nie pada"

weather_forecast.write_weather_data()
