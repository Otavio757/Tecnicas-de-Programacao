import json
from datetime import datetime

class ConcepaByDateParser:
    def __init__(self, date, text):
        self.text = text
        self.date = date

    def ToCsv(self):
        loaded = json.loads(self.text)['results']
        dayOfWeek = self.date.isoweekday()
        normalized_date = ConcepaByDateParser.NormalizeDate(self.date)
        sb=""
        for item in loaded:
            sb+= f"{normalized_date};{item['hora']};{item['fluxo']};{item['total']};{dayOfWeek}\n"
        return sb

    @staticmethod
    def NormalizeDate(date):
        return date.strftime("%d/%m/%Y") if isinstance(date, datetime) else date
