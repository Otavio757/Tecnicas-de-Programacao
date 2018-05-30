from datetime import date
from num2words import num2words

class DaysExtractor:
    daysOfWeek = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

    def get_day(self, text):
                
        if ("próximos" in text):
            return self.get_interval_of_days(text)
        
        elif("hoje" in text):
            return 0
        
        elif("amanhã" in text or "amanha" in text):
            return 1
        
        else:
            for weekDay in self.daysOfWeek:
                if (weekDay in text):
                    return keyWords[weekDay]
            
            #Se chegou até aqui é porque o usuário não digitou um dia de semana válido
            return -1

    def get_interval_of_days(self, text):
        textWithoutSpace = text.replace(" ", "")
        numDays = textWithoutSpace.split("próximos")[1]
        numDays = numDays.split("dias")[0]
        
        #Teste para ver se o número foi escrito por extenso
        try:
            int(numDays)
        
        except:
            numDays = self.numbers[numDays]
        
        return "1:" + numDays

    def get_interval_of_days_by_regex(self, text):
        import re
        regex = r"(proximos)[\s]*(?P<days>[\w]+)?([\s])"
        matches = list(re.finditer(regex, text, re.MULTILINE))
        
        #matches = re.findall(regex, text)
        days = matches["days"]
        print(days)
        # for matchNum, match in enumerate(matches):
        #     matchNum = matchNum + 1
            
        #     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
        #     for groupNum in range(0, len(match.groups())):
        #         groupNum = groupNum + 1
                
        #         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    def load_ordinal_numbers(self):
        self.numbers = []
        for day in range(1, 7):
            self.numbers.append(num2words(42, lang='pt_BR'))

if __name__ == "__main__":
    extractor = DaysExtractor()
    extractor.get_interval_of_days_by_regex("quero saber a previsão para os proximos tres dias em gravatai")