import requests
import csv
from _operator import pos

citiesDictionary = {}

def loadCitiesIDs():
    file = open("CitysAndIDs.txt", "r")
    key = file.readline()
    
    while (key != ""):
        key = key[:-1] #Remove o \n da String
        
        value = file.readline()
        value = value[:-1]
        
        citiesDictionary[key] = value
        
        key = file.readline()
        
        
#def getCityID(name):
#   file = open("CitysAndIDs.txt", "r")
#   line = file.readline()
 #   
#
#    while (line != ""):
 #       line = line[:-1] #Remove o \n da String
  #      
  #      if (line == name):
   #         line = file.readline()
    #        line = line[:-1] #Remove o \n da String
     #       idCity = int(line)
      #      return idCity
    #
     #   else:
      #      file.readline()
       #     line = file.readline()
    #
     #           #Se chegou até aqui, a cidade não existe
    #return -1     
    
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
    
    def __init__(self, cityName):
        self.city = citiesDictionary[cityName]
        #self.getCurrentWeather()
        self.getWeatherForecast()
        self.getWeatherPerHour()
        
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
    
    def getCurrentWeather(self):
        idCity = self.city
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + idCity + "/current?token=d4fb1038cd0a705e7e82f2b2aeb0f2f5"
        request = requests.get(url)
        content = request.content
        content = content.decode("utf-8")
        dataWeather = content.split('"data":{')
        self.weather = dataWeather[1].split(",")
    
    #Previsão de 7 dias, sendo que cada dia é uma posição do array
    def getWeatherForecast(self):
        idCity = self.city
        url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + idCity + "/days/15?token=d4fb1038cd0a705e7e82f2b2aeb0f2f5"
        request = requests.get(url)
        content = request.content
        content = content.decode("utf-8")
        dataForecast = content.split('"data":[{')
        self.forecast = dataForecast[1].split(',{')
    
    def getWeatherPerHour(self):
        idCity = self.city
        url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + idCity + "/hours/72?token=d4fb1038cd0a705e7e82f2b2aeb0f2f5"
        request = requests.get(url)
        content = request.content
        content = content.decode("utf-8")
        dataWeather = content.split('"data":[{')
        dataWeather = dataWeather[1].split(',{')
        
        for dw in dataWeather:
            dw = dw.replace('"', '')
            dw = dw.replace('{', '')
            dw = dw.replace('}', '')
            properties = dw.split(",")
            
            dateAndHour = properties[1].split("date_br:")[1]
            dateAndHour = dateAndHour.split(" ")
            date = dateAndHour[0]
            hour = dateAndHour[1]
            
            precipitation = properties[2]
            precipitation = precipitation.split(":")[2]
            
            velocityWind = properties[3]
            velocityWind = velocityWind.split(":")[2]
            
            temperature = properties[7]
            temperature = temperature.split(":")[2]
            
            result = [date, hour, precipitation, velocityWind, temperature]
            self.weatherPerHour.append(result)
    
    def getCsvWeatherPerHour(self):
        with open("WeatherPerHour.csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            
            for wph in self.weatherPerHour:
                writer.writerow(wph)
        
    def getPropertyWeatherByIndex(self, index):
        dataProperty = self.weather[index]
        propertyWeather = dataProperty.split(":")[1]
    
        #Verifica se existem aspas, se sim as retira
        if (propertyWeather[0] == '"'):
            propertyWeather = propertyWeather[1: -1]
        
        propertyWeather = self.weatherPropertiesList[index] + propertyWeather
    
        return propertyWeather
    
    def getPropertyWeatherByName(self, name):
        index = self.weatherPropertiesDictionary[name]
        return self.getPropertyWeatherByIndex(index)
    
    def getPropertyForecastByIndexOneDay(self, index, f):
        dataProperty = []
        start = 0
        
        for i in range(0, 2):
            end = f.find(",", start)
            dataProperty.append(f[start:end])
            start = end + 1
            
        for i in range(0, 5):
            end = f.find("}", start) + 1
            dataProperty.append(f[start:end])
            start = end + 1
        
        start = f.find("{", start) + 1
        end = f.find("}", start) + 1
        dataProperty.append(f[start:end])
        start = end + 1
        
        start = f.find("{", start) + 6
        end = f.find(",", start)
        dataProperty.append(f[start:end])
        start = end + 1
        
        start = f.find("phrase", start)
        end = f.find("}", start) + 1
        phrase = f[start:end].replace("\\u00", "")
        dataProperty.append(phrase)
        start = end + 1
        
        start = f.find("temperature", start)
        med = f.find("night", start)
        end = f.find("}", med) + 2
        dataProperty.append(f[start:end])
        
        propertyForecast = dataProperty[index]
        
        if (index == 8 or index == 0 or index == 1):
            propertyForecast = propertyForecast.replace('"', '')
            
        elif ("{" in propertyForecast):
            if (index != 10):
                propertyForecast = self.organizeProperty(propertyForecast)
            
            else:
                propertyForecast = self.organizeTemperatureProperty(propertyForecast)
        
        propertyForecast = self.translateProperty(propertyForecast, index)    
        #propertyForecast = self.forecastPropertiesList[index] + propertyForecast
        
        return propertyForecast
        
    def getPropertyForecastByIndex(self, index, forecast):
        resultProperty = []
        
        for f in forecast:
            propertyForecast = self.forecastPropertiesList[index] + self.getPropertyForecastByIndexOneDay(index, f)          
            resultProperty.append(propertyForecast)
    
        return resultProperty
    
    def getPropertyForecastByName(self, name):
        index = self.forecastPropertiesDictionary[name]
        return self.getPropertyForecastByIndex(index)
    
    def getAllPropertiesWeather(self):
        properties = self.weatherPropertiesList[0] + self.getPropertyWeatherByIndex(0)
        
        for i in range(1, 8):
            if (i != 6):
                properties += "\n" + self.weatherPropertiesList[i] + self.getPropertyWeatherByIndex(i)
        
        return properties
    
    def getAllPropertiesForecastOneDay(self, forecast):
        properties = self.forecastPropertiesList[2] + self.getPropertyForecastByIndexOneDay(2, forecast)
        
        for i in range(3, 11):
            if (i != 7):
                properties += "\n\n" + self.forecastPropertiesList[i] + self.getPropertyForecastByIndexOneDay(i, forecast)
            
        
        return properties
        
    #O dia pode ser de 0 a 6, sendo 0 o dia de hoje
    def getForecastOneDay(self, day):
        return self.forecast[day]
    
    def getForecastIntervalOfDays(self, firstDay, lastDay):
        resultForecast = []
        
        for i in range(firstDay, lastDay+1):
            resultForecast.append(self.forecast[i])
        
        return resultForecast
    
    #Melhora a exibição de propriedades que contém chaves e mais de um item
    def organizeProperty(self, p):
        text = p.split(":{")[1]
        text = text.replace("}", "")
        text = text.replace('"', '')
        
        if ("," in text):
            dataList = text.split(",")
            numElements = len(dataList)
            
            text = dataList[0]
            
            for i in range(1, numElements):
                text += "\n" + dataList[i]
        
        return text
    
    def organizeTemperatureProperty(self, p):
        p = p.replace('"', '')
        
        split = p.split(',morning:{')
        general = split[0].split(":{")[1]
        
        split = split[1].split("afternoon:{")
        morning = split[0]
        
        split = split[1].split("night:{")
        afternoon = split[0]
        
        night = split[1]
        
        morning = morning[: -2]
        afternoon = afternoon[: -2]
        night = night[: -2]
        
        general = general.split(",")
        morning = morning.split(",")
        afternoon = afternoon.split(",")
        night = night.split(",")
        
        result = "Dia Inteiro: " + general[0].replace("min:", "Mínima ") + " e " + general[1].replace("max:", "Máxima ") + "\n" + "Manhã: " + morning[0].replace("min:", "Mínima ") + " e " + morning[1].replace("max:", "Máxima ") + "\n" + "Tarde: " + afternoon[0].replace("min:", "Mínima ") + " e " + afternoon[1].replace("max:", "Máxima ") + "\n" + "Noite: " + night[0].replace("min:", "Mínima ") + " e " + night[1].replace("max:", "Máxima ") + "\n"
        
        return result
    
    #O índice 0 é a data dos EUA e o 8 não precisa de tradução
    def translateProperty(self, p, indexProperty):
        if (indexProperty == 1):
            p = p.replace("date_br:", "")
            
        elif (indexProperty == 2):
            p = p.replace("min:", "Mínima: ")
            p = p.replace("max:", "Máxima: ")
        
        elif (indexProperty == 3):
            p = p.replace("probability:", "Probabilidade (%): ")
            p = p.replace("precipitation:", "Nível de Precipitação (mm): ")
        
        elif (indexProperty == 4):
            p = p.replace("velocity_min:", "Velocidade Mínima (km/h): ")
            p = p.replace("velocity_max:", "Velocidade Máxima (km/h): ")
            p = p.replace("velocity_avg:", "Velocidade Média (km/h): ")
            p = p.replace("gust_max:", "Rajada Máxima (km/h): ")
            p = p.replace("direction_degrees:", "Direção (graus): ")
            p = p.replace("direction:", "Direção (ponto cardeal): ")
        
        elif (indexProperty == 5):
            p = p.replace("max:", "Índice Máximo: ")
        
        elif (indexProperty == 6):
            p = p.replace("min:", "Mínima: ")
            p = p.replace("max:", "Máxima: ")

        elif (indexProperty == 9):
            p = p.replace("reduced:", "Geral: ")
            p = p.replace("morning:", "Manhã: ")
            p = p.replace("afternoon:", "Tarde: ")
            p = p.replace("night:", "Noite: ")
            p = p.replace("dawn:", "Madrugada: ")
        
        else: 
            p = p.replace("", "")
            
        return p       

#loadCitiesIDs()
#w = Weather("Montenegro")
#w.getCsvWeatherPerHour()
#print(w.weatherPerHour)
        