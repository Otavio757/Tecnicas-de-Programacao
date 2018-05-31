class Weather:
    city = ""
    
    #Índices: 0 = Temperatura; 1 = Direção do vento; 2 = Velocidade do vento; 3 = Umidade; 4 = Condição; 5 = Pressão; 6 = Ícone; 7 = Sensação térmica; 8 = Data e hora
    weather = ""
    
    #Índices: 0 = Data (EUA); 1 = Data (BR); 2 = Umidade; 3 = Probabilidade de chuva e nível de precipitação; 4 = Vento; 5 = Nível ultravioleta
    #         6 = Sensação térmica; 7  = Ícone; 8 = Texto da previsão; 9 = Texto da previsão por período do dia;  10 = Temperaturas mínimas e máximas
    forecast = ""
    
    #Cada elemento da lista conterá uma sublista com os índices abaixo:
    #Índices: 0 = Data; 1 = Hora; 2 = Nível de precipitação; 3 = Velocidade do vento; 4 = Temperatura
    weatherPerHour = []
    
    weatherPropertiesDictionary = {}
    forecastPropertiesDictionary = {}
    
    weatherPropertiesList = []
    forecastPropertiesList = []

    def __init__(self, initAsfake=False):
        if initAsfake:
            load_fake_values("Gravataí", 1000)
        else:
            pass
    
    def load_fake_values(self, cityName, cityId):
        self.cityName = cityName
        self.cityId = cityId
        
        self.weatherPropertiesDictionary["temperatura"] = 0
        self.weatherPropertiesDictionary["direcao do vento"] = 1
        self.weatherPropertiesDictionary["direção do vento"] = 1
        self.weatherPropertiesDictionary["velocidade do vento"] = 2
        self.weatherPropertiesDictionary["umidade"] = 3
        self.weatherPropertiesDictionary["condicao"] = 4
        self.weatherPropertiesDictionary["condição"] = 4
        self.weatherPropertiesDictionary["pressao"] = 5
        self.weatherPropertiesDictionary["pressão"] = 5
        self.weatherPropertiesDictionary["icone"] = 6
        self.weatherPropertiesDictionary["ícone"] = 6
        self.weatherPropertiesDictionary["sensacao termica"] = 7
        self.weatherPropertiesDictionary["sensação térmica"] = 7
        self.weatherPropertiesDictionary["data e hora"] = 8
        
        self.forecastPropertiesDictionary["data eua"] = 0
        self.forecastPropertiesDictionary["data"] = 1
        self.forecastPropertiesDictionary["umidade"] = 2
        self.forecastPropertiesDictionary["probabilidade de chuva"] = 3
        self.forecastPropertiesDictionary["chuva"] = 3
        self.forecastPropertiesDictionary["nivel de precipitacao"] = 3
        self.forecastPropertiesDictionary["nível de precipitação"] = 3
        self.forecastPropertiesDictionary["precipitação"] = 3
        self.forecastPropertiesDictionary["precipitacao"] = 3
        self.forecastPropertiesDictionary["vento"] = 4
        self.forecastPropertiesDictionary["nivel ultravioleta"] = 5
        self.forecastPropertiesDictionary["nível ultravioleta"] = 5
        self.forecastPropertiesDictionary["ultravioleta"] = 5
        self.forecastPropertiesDictionary["sensacao termica"] = 6
        self.forecastPropertiesDictionary["sensação térmica"] = 6
        self.forecastPropertiesDictionary["icone"] = 7
        self.forecastPropertiesDictionary["ícone"] = 7
        self.forecastPropertiesDictionary["previsao geral"] = 8
        self.forecastPropertiesDictionary["previsão geral"] = 8
        self.forecastPropertiesDictionary["previsao por periodo"] = 9
        self.forecastPropertiesDictionary["previsão por período"] = 9
        self.forecastPropertiesDictionary["temperatura"] = 10
        self.forecastPropertiesDictionary["temperaturas"] = 10
        
        self.weatherPropertiesList = ["Temperatura (ºC): ", "Direção do Vento (km/h): ", "Velocidade do Vento (km/h): ", "Umidade (%): ", "Condição: ", "Pressão (hPa): ", "Ícone: ",
                                      "Sensação Térmica (ºC):", "Data e Hora: "]
        
        self.forecastPropertiesList = ["Data (Estados Unidos): ", "Data: ", "UMIDADE (%)\n", "CHUVA\n", "VENTO\n", "NÍVEL ULTRAVIOLETA\n", "SENSAÇÃO TÉRMICA (ºC)\n", "ÍCONE\n", 
                                       "PREVISÃO GERAL\n", "PREVISÃO POR PERÍODO\n", "TEMPERATURA (ºC)\n"]