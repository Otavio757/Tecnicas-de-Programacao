import unidecode
from datetime import datetime
from num2words import num2words

class TooMuchDaysAhead(Exception):
    pass

class DaysInfo:
    def __init__(self, is_exactly, days_ahead):
        self.is_exactly = is_exactly
        self.days_ahead = days_ahead
        if(not self._validate()):
            raise TooMuchDaysAhead()

    def _validate(self):
        if self.days_ahead == 0:
            return True
        elif self.is_exactly:
            return self._calculate_days_difference() <= 5
        else:
            return self.days_ahead <= 5
    
    def _calculate_days_difference(self):
        today = datetime.today().weekday()

        if (self.days_ahead > today):
            return self.days_ahead - today
        else:
            return self.days_ahead + 7 - today

class DaysExtractor:
    
    #unicoded words
    daysOfWeek = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

    def get_days_ahead(self, day_index):
        current = datetime.today().weekday()
        if current > day_index:
            return 7 - current + day_index
        else:
            return day_index - current

    def get_raw_day(self, text):
        unidecoded_text = unidecode.unidecode(text).lower()

        if ("proximos" in unidecoded_text):
            #return self.get_interval_of_days(text)
            days = self._get_interval_of_days_by_regex(unidecoded_text)
            if days.isdigit():
                return DaysInfo(False, int(days))
            return DaysInfo(False, self._parse_word_to_number(days))
        
        elif("hoje" in unidecoded_text):
            return DaysInfo(True, 0)
        
        elif("amanha" in unidecoded_text):
            return DaysInfo(True, 1)
        
        else:
            for weekDay in self.daysOfWeek:
                if (weekDay in unidecoded_text):
                    return DaysInfo(True, self.get_days_ahead(self.daysOfWeek.index(weekDay)))

            return DaysInfo(True, 0) #hoje - user didnt informed, so we assumed today as a default

    def _get_interval_of_days(self, text):
        textWithoutSpace = text.replace(" ", "")
        numDays = textWithoutSpace.split("próximos")[1]
        numDays = numDays.split("dias")[0]
        
        #Teste para ver se o número foi escrito por extenso
        try:
            int(numDays)
        except:
            numDays = self.numbers[numDays]
        
        return "1:" + numDays

    def _get_interval_of_days_by_regex(self, text):
        import re
        regex = r"(proximos)[\s]*(?P<days>[\w]+)?([\s])"
        matches = list(re.finditer(regex, text, re.MULTILINE))
        if(len(matches) == 0):
            raise Exception("Proximos dias não encontrados.")
        return matches[0].groupdict()['days']
    
    def _load_ordinal_numbers(self):
        self.numbers = []
        for day in range(0, 15):
            self.numbers.append(num2words(day, lang='pt_BR'))
    
    def _parse_word_to_number(self, word):
        self._load_ordinal_numbers()
        return self.numbers.index(word)

if __name__ == "__main__":
    extractor = DaysExtractor()
    d = extractor._get_interval_of_days_by_regex("quero saber a previsão para os proximos tres dias em gravatai")
    print (d)