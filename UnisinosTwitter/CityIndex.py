import os

class CityIndex:

    filepath = "UnisinosDatasets\\cities.txt"

    def __init__(self):
        self.cities = [] #cities list  <----------
        if(os.path.exists(self.filepath)):
            with open(self.filepath, "r") as f:
                for id in f.readlines():
                    self.cities.append(id.replace("\n", ""))

    def get_candidates(self, combinations):
        candidates = []
        for combination in combinations:
            if combination in self.cities:
                candidates.append(combination)
        return candidates
    
    def get_all_cities(self):
        return self.cities

if __name__ == "__main__":
    index = CityIndex()
    a = index.get_candidates(["porto alegre"])
    print(a)