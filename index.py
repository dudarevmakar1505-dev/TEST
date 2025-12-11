class Person:
    name = "Макар"
    age = 10

    def introduce (self):
        print(F"Привіт мене звати {self.name}, мені  {self.age} років")

x = Person()
x.introduce()

