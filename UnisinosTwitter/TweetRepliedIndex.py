import os.path

class TweetRepliedIndex:
    filepath = "UnisinosTwitter/replied_tweets.txt"

    def __init__(self):
        self.ids = []
        if(os.path.exists(self.filepath)):
            with open(self.filepath, "r") as f:
                for id in f.readlines():
                    self.ids.append(id.replace("\n", ""))

    def set_as_replied(self, id):
        self.ids.append(id)
        with open(self.filepath, "a") as f:
            f.write(id + "\n")

    def is_already_replied(self, id):
        return str(id) in self.ids
