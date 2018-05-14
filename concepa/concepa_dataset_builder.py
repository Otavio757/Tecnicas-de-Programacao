import os
from datetime import datetime

class ConcepaDatasetBuilder:
    def __init__(self):
        self.f = None
        self.dataset_path = ""

    def __enter__(self):
        self.Backup()
        self.f = open(self.dataset_path, 'a')
        return self

    def Save(self, text):
        self.f.write(text)

    def Close(self):
        self.f.close()

    def Backup(self):
        if os.path.exists(self.dataset_path):
            os.rename(self.dataset_path,
                      self.dataset_path + "-" + str(datetime.now().timestamp()) + ".csv")

    # def __del__(self):
    #     self.f.Close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.Close()


class ByDateDatasetBuilder(ConcepaDatasetBuilder):
    def __init__(self):
        self.dataset_path = "datasets/bydate.csv"


class ByHourDatasetBuilder(ConcepaDatasetBuilder):
    def __init__(self):
        self.dataset_path = "datasets/byhour.csv"
