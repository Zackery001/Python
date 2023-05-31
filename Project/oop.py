class Fruit:
    def __init__(self):
        print("Hello from Fruit class.")

class Banana(Fruit):
    def intro(self):
        print("Hello from Banana Class, I inherited class Fruit")

class Mango(Fruit):
        def intro(self):
            print("Hello from Mango Class, I inherited class Fruit")

banana = Banana()
banana.intro()

mango = Mango()
mango.intro()