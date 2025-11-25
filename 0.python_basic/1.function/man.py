class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

m = Man("Tom")
m.hello()
print(type(m))
print(type(1))