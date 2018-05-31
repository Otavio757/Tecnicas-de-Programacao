#from . import ClimaTempoResponse, ClimaTempoHistoryInfo, ClimaTempoCurrentInfo, ClimaTempoForecastDaysInfo, ClimaTempoForecastHoursInfo
import unidecode
from UnisinosClimaTempo.WebClient import WebClient
from UnisinosClimaTempo.ClimaTempoResponse import ClimaTempoResponse, ClimaTempoHistoryInfo, ClimaTempoCurrentInfo, ClimaTempoForecastDaysInfo, ClimaTempoForecastHoursInfo

class ClimaTempoService:

    token = "d4fb1038cd0a705e7e82f2b2aeb0f2f5"
    uri_base = "http://apiadvisor.climatempo.com.br/api/v1/[METHOD]/locale/"

    def __init__(self, isDebug=False):
        self.cities = {}
        self.web_client = WebClient(isDebug)
        self.load_cities_ids()

    def load_cities_ids(self):
        file = open("UnisinosClimaTempo/CitysAndIDs.txt", "r")
        key = file.readline()
        while (key != ""):
            key = key[:-1]  # Remove o \n da String
            key = unidecode.unidecode(key).lower()
            value = file.readline()
            value = value[:-1]
            self.cities[key] = value
            key = file.readline()

    def build_url(self, method, cityName, unit="", fromDate=""):
        cityId = self.cities[unidecode.unidecode(cityName).lower()]
        url = self.uri_base.replace("[METHOD]", method) + cityId
        url += not unit == "" and "/" + unit or ""
        url += "?token=" + self.token
        url += not fromDate == "" and "&from=" + fromDate or ""
        return url

    def get_current_weather(self, cityName):
        response = self.web_client.Invoke(self.build_url("weather", cityName, unit="current"))
        return ClimaTempoResponse(response, ClimaTempoCurrentInfo)

    def get_weather_per_hour(self, cityName):
        response = self.web_client.Invoke(self.build_url("forecast", cityName, unit="hours/72"))
        return ClimaTempoResponse(response, ClimaTempoForecastHoursInfo)

    def get_weather_per_days(self, cityName):
        response = self.web_client.Invoke(self.build_url("forecast", cityName, unit="days/15")) #always 15 days - fucking shitting api
        return ClimaTempoResponse(response, ClimaTempoForecastDaysInfo)
        
    def get_weather_history(self, cityName):
        response = self.web_client.Invoke(self.build_url("history", cityName, fromDate=""))
        return ClimaTempoResponse(response, ClimaTempoHistoryInfo)
      
if __name__ == "__main__":
    service = ClimaTempoService(True)
    weathers = service.get_current_weather("Gravataí")
    for weather in weathers.info:
        print(weather.date)

##response = self.web_client.generate_example(self.build_url("forecast", cityName, "hours/72"), "hours_example")