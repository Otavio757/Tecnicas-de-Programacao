import urllib.request

def get_hours():
    
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/',
    }
    params = (
        ('id', '317^'),
        ('data', '09/04/2018'),
    )
    print("RESPOSTA")
    print(response)
    req = urllib.request.Request(
        "http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getHoras/",
        data=params, 
        headers
    )
    f = urllib.request.urlopen(req)
    print(f.read().decode('utf-8'))
    return (f.read().decode('utf-8'))

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://fluxorodovia.triunfoconcepa.com.br/fluxorodoviasite/Home/getHoras/?id=317^&data=09/04/2018', headers=headers)
