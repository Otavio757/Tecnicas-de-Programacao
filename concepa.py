import json
import urllib.request
from datetime import datetime
from datetime import timedelta
from concepa_dataset_builder import *

# 301 - Santo Antonio da Patrulha(Capital/Litoral)
# 219 - Santo Antonio da Patrulha(Litoral/Capital)
# 302 - Gravataí(Capital/Litoral)
# 202 - Gravataí(Litoral/Capital)
# 203 - Eldorado do Sul(Capital/Interior)
# 317 - Eldorado do Sul(Interior/Capital)

# headers = {
#         'Pragma': 'no-cache',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#         'Content-Type': 'application/json; charset=utf-8',
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Cache-Control': 'no-cache',
#         'X-Requested-With': 'XMLHttpRequest',
#         'Connection': 'keep-alive',
#         'Referer': 'http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/',
#     }

class ConcepaByDateParser:
    def __init__(self, date, text):
        self.text = text
        self.date = date
    def ToCsv(self):
        loaded = json.loads(self.text)['results']
        dayOfWeek = self.date.isoweekday()
        normalized_date = NormalizeDate(self.date)
        sb=""
        for item in loaded:
            sb+= f"{normalized_date};{item['hora']};{item['fluxo']};{item['total']};{dayOfWeek}\r\n"
        return sb

class ConcepaSummary:
    def __init__(self, to6am, to12h, to18h, to24h):
        self.to6am = to6am
        self.to12h = to12h
        self.to18h = to18h
        self.to24h = to24h

    def __str__(self):
        return f"INFO:\r\nUnitl 6AM crossed {self.to6am} cars\r\nUntil 12H {self.to12h}\r\nUntil 18H {self.to18h}\r\nIn the whole day {self.to24h}"

def NormalizeDate(date):
    return date.strftime("%d/%m/%Y") if isinstance(date, datetime) else date

def GetByDate(pathId, date):
    normalized_date = NormalizeDate(date)
    response = urllib.request.urlopen(urllib.request.Request(
        url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getData/?id={pathId}&data={normalized_date}",
        data=None,
        # headers=headers
    )).read().decode('utf-8')

    return ConcepaByDateParser(date, response)


def GetByMinute(pathId, date, startHour):
    response = urllib.request.urlopen(urllib.request.Request(
        url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getDataMinutos/?id={pathId}&data={date}&hora={startHour}",
        data=None,
        # headers=headers
    )).read().decode('utf-8')

    return response

def GetCounters(pathId, date):
    response = urllib.request.urlopen(urllib.request.Request(
        url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getHoras/?id={pathId}&data={date}",
        data=None,
        # headers=headers
    )).read().decode('utf-8')

    concepa = json.loads(response)['results'][0]

    return ConcepaSummary(concepa['int1'], concepa['int4'], concepa['int2'], concepa['int3'])
    # return (f.read().decode('utf-8'))