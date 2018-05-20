from twitter_api import single_query_twitter
from clima_tempo import Weather
from datetime import date

#Dicionário com as palavras-chave que serão verificadas no tweet do usuário
keyWords = {}
weekDays = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

def start():
    generateKeyWords()
    tweets = getTweets()
    
    for tweet in tweets:
        text = getTweetText(tweet)
        
        city = checkCity(text)
        w = Weather(city)
        
        day = checkDay(text)
        
        try:
            day = int(day)
            forecast = w.getForecastOneDay(day)
            return w.getAllPropertiesForecastOneDay(forecast)
        
        except ValueError:
            todayNumber = date.today().weekday() + 1
            
            if (todayNumber > 6):
                todayNumber = 0
                
            split = day.split(":")
            lastDay = int(split[1])
            forecast = w.getForecastIntervalOfDays(1, lastDay)
            
            result = "----- " + weekDays[todayNumber].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[0])
            cont = todayNumber + 1
            
            for i in range(1, len(forecast)):
                if(cont > 6):
                    cont = 0
                    
                result += "\n\n----- " + weekDays[cont].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[i])
                cont += 1
            
            return result
        
def generateKeyWords():
    todayNumber = date.today().weekday()
    
    keyWords["hoje"] = 0
    keyWords["amanhã"] = 1
    cont = 0
    
    for i in range(todayNumber, 7):
        today = weekDays[i]
        keyWords[today] = cont
        cont += 1
    
    if (cont < 7):
        todayNumber = 0
        
        while (cont < 7):
            today = weekDays[todayNumber]
            keyWords[today] = cont
            cont += 1
            todayNumber += 1

def getTweets():
    tweets = single_query_twitter("#Tweet2Time").tweets
    
    if (len(tweets) == 0):
        tweets = single_query_twitter("#TweetToTime").tweets

    return tweets

def getTweetText(tweet):
    tweetString = str(tweet)
    text = tweetString.split(" - ")[2]
    
    return text

#Este método retorna um número ou intervalo de dias para calcular a previsão do tempo
def checkDay(text):
    text = text.lower()
    
    if ("próximos" in text):
        return checkDaysInterval(text)
    
    elif("hoje" in text):
        return 0
    
    elif("amanhã" in text):
        return 1
    
    else:
        try:
            for weekDay in weekDays:
                if (weekDay in text):
                    return keyWords[weekDay]
        
        #Se chegou até aqui é porque o usuário não digitou um dia de semana válido
        except:
            return -1
                    
def checkDaysInterval(text):
    textWithoutSpace = text.replace(" ", "")
    numDays = textWithoutSpace.split("próximos")[1]
    numDays = numDays.split("dias")[0]
    
    return "1:" + numDays

#Observação: para a cidade ser reconhecida corretamente, ela deverá estar no final da frase e com letra maiúscula em cada nome da cidade (por exemplo São Leopoldo) 
#com um ponto de interrogação no final. Além disso o usuário precisará escrever obrigatoriamente "cidade" ou "cidade de"
def checkCity(text):
    verification = "cidade"
    
    if (verification in text):
        if("cidade de" in text):
            verification = "cidade de"
        
        city = text.split(verification)[1]
        city = city.split("?")[0]
        city = city[1:]
        
        return city
    
    #Se chegou até aqui a cidade não foi especificada
    else:
        return ""
    

print(start())    