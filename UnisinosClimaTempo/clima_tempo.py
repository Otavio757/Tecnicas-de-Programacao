import requests
import csv
from _operator import pos

class Weather:

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
        