import json

class ClimaTempoResponse:
    def __init__(self, raw_json, internal_type):
        self.info = []
        data = json.loads(raw_json)['data']
        if isinstance(data, list):
            for item in data:
                self.info.append(internal_type(item))
        else:
            self.info.append(internal_type(data))

    def __getattr__ (self, attr):
        try:
            return self.data[attr]
        except KeyError:
            return 'UNIBOT NOT FOUND ATTRIBUTE'

class ClimaTempoCurrentInfo:
    def __init__(self, dic):
        self.__dict__ = dic

    def __getattr__ (self, attr):
        try:
            if attr == "temperature": return self.temperature['temperature']
            if attr == "precipitation": return self.rain['precipitation']

            return self.data[attr]
        except KeyError:
            return 'UNIBOT NOT FOUND ATTRIBUTE'

class ClimaTempoForecastDaysInfo:
    def __init__(self, dic):
        self.date = None
        self.temperature = None
        self.__dict__ = dic
        self.min_temperature = self.temperature['min']
        self.max_temperature = self.temperature['max']
    
    def Format(self):
        return "(na data: %s temp min de %s e max de %s) " % (self.date, self.temperature['min'], self.temperature['max'])

class ClimaTempoForecastHoursInfo:
    def __init__(self, dic):
        self.__dict__ = dic

class ClimaTempoHistoryInfo:
    def __init__(self, dic):
        self.__dict__ = dic