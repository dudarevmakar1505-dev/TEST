print('ghbdsn')
import random

h = random.randint(1,60)

print("Вгадай число від 1 до 60")

while True:
    print_number = int(input("Введіть число: "))

    if print_number == h:
        print("Ви вгадали")
        break
    else:
        print("Ви не вгадали: ")
