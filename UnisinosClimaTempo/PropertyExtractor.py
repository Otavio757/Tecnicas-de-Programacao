from unidecode import unidecode
class PropertyExtractor:
    def __init__(self):
        self.properties = {    
            # "chuva": "UnisinosTwitter.TwitterService.TwitterServiceFake",
            "humidade": "data.humidity",
            "precipitacao": "UnisinosClimaTempo.ClimaTempoService.ClimaTempoServiceFake",
            "vento": "wind_direction",
            "vento": "wind_velocity",
            "condicao": "condition",
            "pressao": "pressure",
            "sensacao": "sensation",
            "uv": "uv.max"
        }
    
    def get_cited_properties(self, tweet_text):
        tweet_text = unidecode(tweet_text.lower())
        cited_properties = []
        for prop in self.properties:
            if(prop in tweet_text):
                cited_properties.append(prop)
        return cited_properties

if __name__ == "__main__":
    import pprint
    service = PropertyExtractor()
    props = service.get_cited_properties("quero saber a previsao do tempo e vento para gravatai e também como vai estar o uv.")
    pprint.pprint(props)