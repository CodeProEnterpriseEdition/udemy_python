import random

# number = random.randint(1, 21)
# print(number)

for number in range(1, 21):
    if number == 4 or number == 13:
        print(f"{number} is unlucky")
    elif number % 2 == 0:
        print(f"{number} is event")
    elif number % 2 == 1:
        print(f"{number} is odd")

# for item in range(1, 20):
#     print(item)
jotain = True
while (jotain):
    testi = int(input())
    if testi > 6:
        jotain = False
