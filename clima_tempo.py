import requests

def getCityID(name):
    file = open("CitysAndIDs.txt", "r")
    line = file.readline()

    while (line != ""):
        line = line[:-1] #Remove o \n da String
        
        if(line == name):
            line = file.readline()
            line = line[:-1] #Remove o \n da String
            idCity = int(line)
            return idCity
    
        else:
            file.readline()
            line = file.readline()
    
    #Se chegou até aqui, a cidade não existe
    return -1

def getCurrentWeather(idCity):
    idCity = str(idCity)
    url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + idCity + "/current?token=674c09fdf63da66d938c5eb2d0860e72"
    request = requests.get(url)
    content = request.content
    content = content.decode("utf-8")
    dataWeather = content.split('"data":{')
    weather = dataWeather[1].split(",")
    #Índices: 0 = Temperatura; 1 = Direção do vento; 2 = Velocidade do vento; 3 = Umidade; 4 = Condição; 5 = Pressão; 6 = Ícone; 7 = Sensação térmica; 8 = Data e hora
    return weather

    #Índices: 0 = Temperatura; 1 = Direção do vento; 2 = Velocidade do vento; 3 = Umidade; 4 = Condição; 5 = Pressão; 6 = Ícone; 7 = Sensação térmica; 8 = Data e hora
def getPropertyWeather(weather, index):
    dataProperty = weather[index]
    propertyWeather = dataProperty.split(":")[1]
    
    #Verifica se existem aspas, se sim as retira
    if (propertyWeather[0] == '"'):
        propertyWeather = propertyWeather[1: -1]
    
    return propertyWeather

#Teste: obter a temperatura atual de São Leopoldo
idC = getCityID("São Leopoldo")
weather = getCurrentWeather(idC)
print(getPropertyWeather(weather, 0))




    

