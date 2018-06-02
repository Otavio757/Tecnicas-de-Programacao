class TweetObject:
    def __init__(self, id, source, geo, text):
        self.id = id
        self.geo = geo
        self.text = text
        self.source = source

    def __str__(self): 
        return f"{self.source} - {self.geo} - {self.text}."
    
    def __repr__(self):
        return self.__str__()