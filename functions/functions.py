
from random import random

global_variable = 10

def say_hi():
    print("Hi!")

def flip_coin():
    if random() > 0.5:
        return "heads"
    else:
        return "tails"

def exponentti(kerrottava, kerroin=2):
    return kerrottava ** kerroin

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

def speak2(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

def generate_evens():
    list = []
    for num in range(1, 50):
        if num % 2 == 0 :
            list.append(num)
    return list

def tulosta_global(numero):
    print(numero)
    # print(global_variable) Ei voi kutsua ennen kuin global_variable
    # on määritelty globaaliksi
    global global_variable 
    global_variable += numero
    print(global_variable)

say_hi()
print(flip_coin())
print(generate_evens())
print(exponentti(2))
print(exponentti(2,3))
print(speak2("sadf"))
print(speak2("dog"))
tulosta_global(3)
tulosta_global(3)
