
from random import randint

number = 0
guess = randint(1,10)
print(guess)
while number != guess:
    print("arvaa numero")
    number = int(input())
