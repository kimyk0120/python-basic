class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized")

    def sayHell(self):
        print("Hello " + self.name)


m = Man("test")
m.sayHell()