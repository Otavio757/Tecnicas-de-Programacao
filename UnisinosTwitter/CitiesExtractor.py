__version__ = '0.1'
__author__ = 'Thiago Lopes'
__status__ = "Development"

#https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o

import sys
import math
from geotext import GeoText
from UnisinosTwitter.CityIndex import CityIndex

class CitiesExtractor:
    """ usaremos esta classe para extrair as cidades de dentro do texto to tweet"""
    def Extract(self, text):
        pass

    def GetPosition(self, tweet):
        return tweet["coordinates"]
    
    def GetWords(self, text):
        return text.split(" ")
    
    def GetCandidates(self, words):
        import itertools
        reponses=[]
        factorial = math.factorial(len(words))
        for i in range(len(words)+1):
            for c in itertools.combinations(words, i):
                cc = ' '.join(c)
                if len(cc) <= factorial:
                    #print (cc)
                    reponses.append(cc)
        return reponses

    def GetCities(self, text):
        #tokens = self.GetWords(text)
        tokens = self.TokenizeByWords(text)
        combinations = self.GetCandidates(tokens)
        #candidates = GeoText(combinations).cities
        index = CityIndex()
        candidates = index.get_candidates(combinations)
        candidates.sort(key=len, reverse=True)
        return candidates

    def RemoveStopWords(self, text):
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        stop_words = set(stopwords.words("portuguese"))
        #Em portugues está cortando coisas importantes, como: "são" de são leopoldo, bem como as preposições "em" e "para"
        #words = word_tokenize("Eu sou o sr. Thiago. Estou em esteio e quero ir para gravataí", language='portuguese')
        words = word_tokenize(text)
        filtered = [w for w in words if not w in stop_words]
        print(filtered)

    def TokenizeByWords(self, text):
        from nltk import tokenize
        tokens = tokenize.word_tokenize(text, language='portuguese')   
        return tokens

    def RemoveAccents(self, accented_string):
        import unidecode
        unaccented_string = unidecode.unidecode(accented_string)
        return unaccented_string

    def BuildCitiesDataset(self):
        import unidecode
        baseCities = []
        with open("UnisinosDatasets\\cities_base.txt", "r") as f:
            baseCities = f.readlines()
        
        cities = []
        for city in baseCities:
            stripedCity = city.strip().lower()
            cities.append(stripedCity)
            unaccented = unidecode.unidecode(stripedCity)
            if not stripedCity == unaccented:
                cities.append(unaccented)

        with open("UnisinosDatasets\\cities.txt", "a") as f:
            f.writelines(map(lambda x: x + '\n', cities))

    def TryPredictCity(self, city):
        # from nltk.containers import Trie
        # t = Trie()
        pass

    def SimpleExtractor(self, text):
        """neste caso, testamos o indice de cidades contra o texto 
        e retornamos a lista de cidades encontradas.
        
        Porém, este método encontra falsos positivos como em:

        > "Estou em são leopoldo e vou para gravatai"
        >> ['gravatai', 'são leopoldo', 'gravata']
        """
        text = text.lower()
        index = CityIndex()
        found_cities = []
        for city in index.get_all_cities():
            if (city in text):
                found_cities.append(city)
        return found_cities

    def SimpleExtratorEnsured(self, text):
        text = text.lower()
        index = CityIndex()
        found_cities = []
        text_length = len(text)
        for city in index.get_all_cities():
            if (city in text):
                text_index = text.index(city)
                next_char_index = text_index + len(city)
                if(next_char_index < text_length): #se não for a ultima palavra, verifica se é match exato
                    next_char = text[text_index + len(city)]
                    if not next_char.isalpha(): #proximo char depois do match não pode ser um alfa (gravatai vs. gravata)
                        found_cities.append(city)
                else: 
                    found_cities.append(city) #caso seja a ultima palavra da frase, é match
        return found_cities

if __name__ == "__main__":
    # print(sys.path)
    extractor = CitiesExtractor()
    ##extractor.BuildCitiesDataset()
    #a = extractor.GetCities("Estou indo para sao leopoldo")
    #extractor.TryPredictCity("porto alegee")
    a = extractor.SimpleExtratorEnsured("Estou em são leopoldo e vou para gravatai")
    print(a)

    #print(a)