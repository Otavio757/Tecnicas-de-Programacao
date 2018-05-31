import os
import requests

class WebClient:
    def __init__(self):
        pass
        
    def Invoke(self, url):
            return requests.get(url).content.decode("utf-8")

class WebClientFake():
    def Invoke(self, url):
        file_path = self.get_filename(url)
        if os.path.exists(file_path):
            file = open(file_path, "r")
            response = file.readline()
            file.close()
            return response
        else:
            real_web_client = WebClient()
            response = real_web_client.Invoke(url)
            file = open(file_path, "w")
            file.write(response)
            file.flush()
            file.close()
            return response
    
    def get_filename(self, url):
        if "current" in url: return "UnisinosClimaTempo/SavedResponses/current.txt"
        if "days/15" in url: return "UnisinosClimaTempo/SavedResponses/days.txt"
        if "hours/72" in url: return "UnisinosClimaTempo/SavedResponses/hours.txt"
        if "history" in url: return "UnisinosClimaTempo/SavedResponses/history.txt"
        return "UnisinosClimaTempo/SavedResponses/unknown.txt"