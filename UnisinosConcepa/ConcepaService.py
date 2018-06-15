import json
import urllib.request
from datetime import timedelta
from ConcepaByDateParser import ConcepaByDateParser
from ConcepaSummary import ConcepaSummary

class ConcepaService:

    def GetByDate(self, pathId, date):
        normalized_date = ConcepaByDateParser.NormalizeDate(date)
        response = urllib.request.urlopen(urllib.request.Request(
            url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getData/?id={pathId}&data={normalized_date}",
            data=None,
            # headers=headers
        )).read().decode('utf-8')

        return ConcepaByDateParser(date, response)


    def GetByMinute(self, pathId, date, startHour):
        response = urllib.request.urlopen(urllib.request.Request(
            url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getDataMinutos/?id={pathId}&data={date}&hora={startHour}",
            data=None,
            # headers=headers
        )).read().decode('utf-8')

        return response

    def GetCounters(self, pathId, date):
        response = urllib.request.urlopen(urllib.request.Request(
            url=f"http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getHoras/?id={pathId}&data={date}",
            data=None,
            # headers=headers
        )).read().decode('utf-8')

        concepa = json.loads(response)['results'][0]

        return ConcepaSummary(concepa['int1'], concepa['int4'], concepa['int2'], concepa['int3'])
        # return (f.read().decode('utf-8'))



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
