class Fruit:
    def __init__(self):
        print("Hello from Fruit class.")

class Banana(Fruit):
    def intro(self):
        print("Hello from Banana Class, I inherited class Fruit")

fruit = Banana()
fruit.intro()