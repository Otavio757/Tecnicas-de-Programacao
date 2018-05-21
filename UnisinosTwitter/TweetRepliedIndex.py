import os.path

class TweetRepliedIndex:
    filepath = "replied_tweets.txt"

    def __init__(self):
        if(os.path.exists(self.filepath)):
            with open(self.filepath, "w") as f:
                self.ids = f.readlines()

    def set_as_replied(self, id):
        self.ids.append(id)
        with open(self.filepath, "w") as f:
            f.write(id)

    def is_already_replied(self, id):
        return id in self.ids