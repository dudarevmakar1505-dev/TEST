# def na (e,y):
#     return e +y
# print (na(34,67))


class Person:
    name = "Макар"
    age = 10
    def introduce(self):
        print(f"Привіт, мене звати {self.name} мені {self.age} років.")


g =Person()
g.introduce()