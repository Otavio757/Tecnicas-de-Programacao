import unidecode

class PropertiesExtractor:
    def __init__(self):
        self.properties = {
            "umidade": "humidity",
            "chuva": "rain",
            "precipitacao": "rain",
            "vento": "wind"
            }
    
    def get_requested_property(self, text):
        text = unidecode.unidecode(text).lower()
        for prop in self.properties:
            if prop in text:
                return self.properties[prop]
        return ""
    