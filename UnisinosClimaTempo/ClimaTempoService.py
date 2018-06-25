import unidecode

class ClimaTempoService:

    token = "d4fb1038cd0a705e7e82f2b2aeb0f2f5"
    uri_base = "http://apiadvisor.climatempo.com.br/api/v1/[METHOD]/locale/"

    def __init__(self):
        self.cities = {}
        self.web_client = WebClient()
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
        url = self.build_url("weather", cityName, unit="current")
        response = self.web_client.Invoke(url)
        return ClimaTempoResponseFactory(response, ClimaTempoCurrentInfo)

    def get_weather_per_hour(self, cityName):
        response = self.web_client.Invoke(self.build_url("forecast", cityName, unit="hours/72"))
        return ClimaTempoResponseFactory(response, ClimaTempoForecastHoursInfo)

    def get_weather_per_days(self, cityName, exact_day = -1, days_ahead = -1):
        response = self.web_client.Invoke(self.build_url("forecast", cityName, unit="days/15")) #always 15 days - fucking shitting api
        response = ClimaTempoResponseFactory(response, ClimaTempoForecastDaysInfo)
        if not exact_day == -1:
            response.info = [response.info[exact_day]]
        elif not days_ahead == -1:
            response.info = response.info[0:days_ahead]
        return response
        
    def get_weather_history(self, cityName):
        response = self.web_client.Invoke(self.build_url("history", cityName, fromDate=""))
        return ClimaTempoResponseFactory(response, ClimaTempoHistoryInfo)

class ClimaTempoServiceFake(ClimaTempoService):
    def __init__(self):
        self.cities = {}
        self.web_client = WebClientFake()
        self.load_cities_ids()

if __name__ == "__main__":
    from WebClient import WebClient, WebClientFake
    from ClimaTempoResponse import ClimaTempoResponseFactory, ClimaTempoHistoryInfo, ClimaTempoCurrentInfo, ClimaTempoForecastDaysInfo, ClimaTempoForecastHoursInfo
    service = ClimaTempoServiceFake()
    # weathers = service.get_current_weather("Gravataí")
    weathers = service.get_weather_per_days("Gravataí", days_ahead = 5)
    for weather in weathers.info:
        print(weather.precipitacao)
else:
    from UnisinosClimaTempo.WebClient import WebClient, WebClientFake
    from UnisinosClimaTempo.ClimaTempoResponse import ClimaTempoResponseFactory, ClimaTempoHistoryInfo, ClimaTempoCurrentInfo, ClimaTempoForecastDaysInfo, ClimaTempoForecastHoursInfo
##response = self.web_client.generate_example(self.build_url("forecast", cityName, "hours/72"), "hours_example")
