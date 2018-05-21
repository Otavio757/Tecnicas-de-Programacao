from clima_tempo import Weather, citiesDictionary, loadCitiesIDs
from datetime import date
from twitter_api import single_query_twitter, reply_tweet, tweetsIDs

#Dicionário com as palavras-chave que serão verificadas no tweet do usuário
keyWords = {}
numbers = {}
weekDays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

def start():
    loadCitiesIDs()
    generateKeyWordsAndNumbers()
    tweets = getTweets()
    
    for i in range(0, len(tweets.tweets)):
        tweet = tweets.tweets[i]
        text = getTweetText(tweet)
        
        city = checkCity(text)
        w = Weather(city)
        
        day = checkDay(text)
        
        try:
            day = int(day)
            forecast = w.getForecastOneDay(day)
            allProperties = w.getAllPropertiesForecastOneDay(forecast)
            tweet = "#Tweet2Time " + w.getPropertyForecastByIndexOneDay(8, forecast)
            reply_tweet(tweetsIDs[i], tweet)
            print(allProperties)
        
        except ValueError:
            todayNumber = date.today().weekday() + 1
            
            if (todayNumber > 6):
                todayNumber = 0
                
            split = day.split(":")
            lastDay = int(split[1])
            forecast = w.getForecastIntervalOfDays(1, lastDay)
            
            allProperties = "----- " + weekDays[todayNumber].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[0])
            tweet = "#Tweet2Time\n" + weekDays[todayNumber] + ": " + w.getPropertyForecastByIndexOneDay(8, forecast[0])
            cont = todayNumber + 1
            
            for j in range(1, len(forecast)):
                if(cont > 6):
                    cont = 0
                    
                allProperties += "\n\n----- " + weekDays[cont].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[j])
                tweet += "\n" + weekDays[cont] + ": " + w.getPropertyForecastByIndexOneDay(8, forecast[j])
                cont += 1
            
            reply_tweet(tweetsIDs[i], tweet)
            print(allProperties)
        
def generateKeyWordsAndNumbers():
    todayNumber = date.today().weekday()
    
    keyWords["hoje"] = 0
    keyWords["amanhã"] = 1
    cont = 0
    
    for i in range(todayNumber, 7):
        today = weekDays[i].lower()
        keyWords[today] = cont
        cont += 1
    
    if (cont < 7):
        todayNumber = 0
        
        while (cont < 7):
            today = weekDays[todayNumber]
            keyWords[today] = cont
            cont += 1
            todayNumber += 1
    
    numbers["dois"] = "2"
    numbers["três"] = "3"
    numbers["quatro"] = "4"
    numbers["cinco"] = "5"
    numbers["seis"] = "6"
    numbers["sete"] = "7"

def getTweets():
    tweets = single_query_twitter("#Tweet2Time")
    
    if (len(tweets.tweets) == 0):
        tweets = single_query_twitter("#TweetToTime")

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
        for weekDay in weekDays:
            weekDay = weekDay.lower()
            if (weekDay in text):
                return keyWords[weekDay]
        
        #Se chegou até aqui é porque o usuário não digitou um dia de semana válido
        return -1
                    
def checkDaysInterval(text):
    textWithoutSpace = text.replace(" ", "")
    numDays = textWithoutSpace.split("próximos")[1]
    numDays = numDays.split("dias")[0]
    
    #Teste para ver se o número foi escrito por extenso
    try:
        int(numDays)
    
    except:
        numDays = numbers[numDays]
    
    return "1:" + numDays

#Com a atualização deste método, não é mais necessário explicitar a palavra cidade e nem seguir as outras regras
def checkCity(text):
    for key in citiesDictionary:
        if (key in text):
            return key
    
    #Se chegou até aqui a cidade não foi especificada ou é inválida
    return ""


start()