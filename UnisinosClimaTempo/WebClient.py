import requests

class WebClient:
    def __init__(self, isDebug=False):
        self.is_debug = isDebug

    def Invoke(self, url):
        if self.is_debug:
            #file = open("UnisinosClimaTempo/hours_example.txt", "r")
            file = open("UnisinosClimaTempo/response_example.txt", "r")
            response = file.readline()
            file.close()
            return response
        else:
            return requests.get(url).content.decode("utf-8")

    def generate_example(self, url, destination_filename):
        response = requests.get(url).content.decode("utf-8")
        file = open("UnisinosClimaTempo/"+destination_filename+".txt", "a")
        file.write(response)
        file.flush()
        file.close()
        return response