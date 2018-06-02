import importlib

class DependenceResolver:
    def __init__(self, isDebug):
        if isDebug:
            self.instances = {    
                "twitter": "UnisinosTwitter.TwitterService.TwitterServiceFake",
                "weather": "UnisinosClimaTempo.ClimaTempoService.ClimaTempoServiceFake",
                "city_extractor": "UnisinosTwitter.CitiesExtractor.CitiesExtractor",
                "days_extractor": "UnisinosClimaTempo.DaysExtractor.DaysExtractor",
                "tweeter_index": "UnisinosTwitter.TweetRepliedIndex.TweetRepliedIndex"
            }
        else:
            self.instances = {    
            "twitter": "UnisinosTwitter.TwitterService.TwitterService",
            "weather": "UnisinosClimaTempo.ClimaTempoService.ClimaTempoService",
            "city_extractor": "UnisinosTwitter.CitiesExtractor.CitiesExtractor",
            "days_extractor": "UnisinosClimaTempo.DaysExtractor.DaysExtractor",
            "tweeter_index": "UnisinosTwitter.TweetRepliedIndex.TweetRepliedIndex"
        }

    def Resolve(self, instanceof):
        module_name, class_name = self.instances[instanceof].rsplit(".", 1)
        MyClass = getattr(importlib.import_module(module_name), class_name)
        instance = MyClass()
        return instance