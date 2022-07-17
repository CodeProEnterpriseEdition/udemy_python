# https://docs.python.org/3/py-modindex.html
# importtaa kaikki ja anna sille uusi nimi
# import random as omg_so_random
# importtaa tiettyjä moduuleja
# from random import choice, shuffle
import keyword
from random import choice as gimme_one
from random import shuffle


fruits = ["apple", "banana", "cherry", "durian"]
print(gimme_one(["apple", "banana", "cherry", "durian"]))
shuffle(fruits)
print(fruits)


def onko(*args):
    if 3 in args:
        return True
    return False


print(onko(1, 2, 3, 4, 5))
print(onko(1, 2, 4, 5))

print('-----')


def contains_keyword(*args):
    for word in args:
        if keyword.iskeyword(word):
            return True
    return False


print(contains_keyword("import"))
print(contains_keyword("print"))
print(contains_keyword("if"))

print("-----2-------")


def contains_keyword(*args):
    if (keyword.iskeyword(word) for word in args):
        return True
    return False


print(contains_keyword("import"))
print(contains_keyword("print"))
print(contains_keyword("if"))
