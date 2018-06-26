import json

class ClimaTempoResponseFactory:
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
    
    def __str__(self):
        result = ""
        for i in self.info:
            result += str(i) + '\n'
        return result

class ClimaTempoCurrentInfo:
    def __init__(self, dic):
        self.__dict__ = dic
        self.available_properties = ["temperature", "wind_direction", "wind_velocity", "humidity", "condition", "pressure", "sensation"]

    def __getattr__ (self, attr):
        # if attr == "temperature": return self.temperature
        if attr == "vento": return "O vento na direção: %s, com vel. de: %sKmh" % (self.wind_direction, self.wind_velocity)
        elif attr == "pressao": return "A pressão de %s" % self.pressure
        elif attr == "umidade": return "A humidade de %s" % self.humidity
        elif attr == "condicao": return "Condição de %s" % self.condition.lower()
        elif attr == "temperatura": return "A temperatura max de %s" % self.temperature
        else: self.__dict__[attr]
    
    def __str__(self):
        return "(Agora a temperatura é de %s) " % (self.temperatura)

    def format_message(self, city, citied_properties):
        msg = "A atual em %s hoje é %s°C." % (city, self.temperatura)
        for citied_property in citied_properties:
            try:
                msg += " %s." % getattr(self, citied_property)
            except KeyError:
                msg += " Vc pediu por %s mas essa info ñ está disponivel :/" % citied_property
        return msg

class ClimaTempoForecastDaysInfo:
    # humidity [min, max]
    # rain [probability, precipitation]
    # wind [velocity_min, velocity_max, velocity_avg, gust_max, direction_degrees, direction]
    # uv [max]
    # thermal_sensation [min, max]
    # temperature [min, max]
    def __init__(self, dic):
        self.date = None
        self.temperature = None
        self.__dict__ = dic
        self.min_temperature = self.temperature['min']
        self.max_temperature = self.temperature['max']
    
    def __repr__(self):
        return "(na data: %s temp min de %s e max de %s) " % (self.date, self.min_temperature, self.max_temperature)
    
    def __getattr__ (self, attr):
        if attr == "data": return self.data
        elif attr == "temperatura": return "A temperatura max de %s" % self.temperature['max']
        elif attr == "precipitation": return self.rain['precipitation']
        elif attr == "vento": return "O vento na direção: %s, c/ vel. de: %skmh" % (self.wind['direction'], self.wind['velocity_avg'])
        elif attr == "pressao": return "A pressao de %s" % self.pressure
        elif attr == "condicao": return "A condição %s" % self.condition
        elif attr == "chuva": return "A probabilidade de chuva é %s" % self.rain['probability']
        elif attr == "umidade": return "A humidade min de %s e max %s" % (self.humidity['min'], self.humidity['max'])
        elif attr == "precipitacao": return "A precipitação de %s" % self.rain['precipitation']
        elif attr == "uv": return "UV max de %s" % self.uv['max']
        elif attr == "sensacao termica": return "A sensação min de %s e max %s" % (self.thermal_sensation['min'], self.thermal_sensation['max'])
        else: self.__dict__[attr]

    def format_message(self, city, citied_properties):
        msg = "A temp. para %s em %s será %s°C." % (city, self.date, self.temperatura)
        for citied_property in citied_properties:
            try:
                msg += " %s." % (getattr(self, citied_property))
            except KeyError:
                msg += " Vc pediu por %s mas essa info ñ está disponivel :/" % citied_property
        return msg

class ClimaTempoForecastHoursInfo:
    def __init__(self, dic):
        self.__dict__ = dic

    def __str__(self):
        raise NotImplementedError()

class ClimaTempoHistoryInfo:
    def __init__(self, dic):
        self.__dict__ = dic
    
    def __str__(self):
        raise NotImplementedError()