class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value
    def other(self):
        return 15

class Child(Parent):
    def get_value(self) -> int:
        try:
            raise Exception("excetion!")
            return 10
        except Exception as e:
            print (e)
        


obj = Child()
print(obj.get_value())
#print(obj.other())