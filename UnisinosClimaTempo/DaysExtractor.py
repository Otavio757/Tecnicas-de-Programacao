from datetime import datetime
from num2words import num2words

class DaysExtractor:
    daysOfWeek = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

    def get_days_ahead(self, day_index):
        current = datetime.today().weekday()
        if current > day_index:
            return 7 - current + day_index
        else:
            day_index - current

    def get_raw_day(self, text):
                
        if ("próximos" in text or "proximos" in text):
            #return self.get_interval_of_days(text)
            days = self.get_interval_of_days_by_regex(text)
            if days.isdigit():
                return int(days)
            return self.parse_word_to_number(days)
        
        elif("hoje" in text):
            return 0
        
        elif("amanhã" in text or "amanha" in text):
            return 1
        
        else:
            for weekDay in self.daysOfWeek:
                if (weekDay in text):
                    return self.get_days_ahead(self.daysOfWeek.index(weekDay))

            return 0 #hoje - user didnt informed, so we assumed today as a default

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
        if(len(matches) == 0):
            raise Exception("Proximos dias não encontrados.")
        return matches[0].groupdict()['days']
    
    def load_ordinal_numbers(self):
        self.numbers = []
        for day in range(0, 15):
            self.numbers.append(num2words(day, lang='pt_BR'))
    
    def parse_word_to_number(self, word):
        self.load_ordinal_numbers()
        return self.numbers.index(word)

if __name__ == "__main__":
    extractor = DaysExtractor()
    d = extractor.get_interval_of_days_by_regex("quero saber a previsão para os proximos tres dias em gravatai")
    print (d)