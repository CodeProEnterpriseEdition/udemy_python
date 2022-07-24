
# tehtävä 0, luominen/syntaxi
print("----------------luominen/syntaxi-----------------")
list_1 = [1, 2, 3]
tuple_1 = (1, 2, 3)
dict_1 = {"name": "jeppe", "email": "hemuli@hem.fi", "koti": True}
dict_1 = dict(first=1, second=2, third=3)
set_1 = {1, 2, 3}
print("the type is: ", type(list_1), list_1)
print("the type is: ", type(tuple_1), tuple_1)
print("the type is: ", type(dict_1), dict_1)
print("the type is: ", type(set_1), set_1)
# tehtävä 1, comprehensions
print("----------------comprehensions-----------------")
list_2 = [3, 4, 5, 6]
answer = [num for num in list_1 if num in list_2]
print("list comprehension", answer)

set_comprehension = {x**2 for x in set_1}
print("set comprehension ",  set_comprehension)

squared_numbers = {key: value ** 2 for key, value in dict_1.items()}
print("dict_comprehensins", squared_numbers)

print(set(list_1) | set(list_2))
# vain yhteiset arvot
print(set(list_1) & set(list_2))
# tehtävä 2


# tehtävä 3 Mitä eroa on functiolla ja methodilla
"""
- methodi on instanssin functio
- functio taas on builtIn functio tai käyttäjän luoma riippumaton
functio
"""


# tehtävä 4 Käytä lambdaa filter function kanssa.
b = list(range(11))
print(list(filter(lambda n: n % 2 == 0, b)))

# tehtävä 5 Käytä max() functiossa key:tä. Esim. lista sanoista ja niistä pisin.

names = ("Arya", "Samson", "Dore", "Tim", "ollicander")
print(min(names, key=len))

# tehtävä 6 Tee lambda, joka palauttaa pienimmän ja isoimman iterablesta
lst = [1, 2, 3, 4, 5]
nums = [99, 25, 30, -7]
name = 'alcatraz'


def extremes(iterable): return (min(iterable), max(iterable))


print(extremes(lst))
print(extremes(nums))
print(extremes(name))


# tehtävä 7 Käytä slicea kolme kertaa
name = 'alcatraz'
print(name[::-1])  # reverse
print(name[:3])  # lopettaa kolmanteen merkkiin
print(name[3:])  # aloittaa kolmannen merkin kohdalta


# tehtävä 8 Tee functio, joka palauttaa max_magnituden listasta
max_lst1 = [300, 20, -900]
max_lst2 = [10, 11, 12]
max_lst3 = [-5, -1-89]


def max_magnitude(lst):
    return max(lst, key=lambda n: abs(n))


print(max_magnitude(max_lst1))
print(max_magnitude(max_lst2))
print(max_magnitude(max_lst3))

# tehtävä 9 Käytä zippiä yhdistämään kaksi listaa
names = ['paavola', 'pekka', 'maija', 'maja']
scores = [123, 22, 51]
names_scores = (dict(zip(names, scores)))


# tehtävä 10 Käytä try except (else, finally) rakennetta functiossa

def divide(num1, num2):
    try:
        results = num1//num2
    except TypeError:
        return "Give int or float"
    except ZeroDivisionError:
        return "don't divide with zero"
    else:
        return results
    finally:
        print("good work")


print(divide(1, 2))
print(divide(1, "peruna"))

# tehtävä 11 Tee functio, joka ottaa listan ja muuttujan.
# Palauttaa True jos muuttuja on listassa ja False jos ei ole.


def onko(*args):
    if 3 in args:
        return True
    return False


print(onko(1, 2, 3, 4, 5))
print(onko(1, 2, 4, 5))
# tehtävä 12 Mihin Super() viittaa ja
# miten mro = method resolution order saadaan selville
"""Super viittaa parent luokkaan.
    print(ClassName.mro()) , missä ClassName on luokka
    ClassName.__mro__
    ClassName.mro()
    help(ClassName)
"""

# tehtävä 13 Mitä properties on kätevä?
"""Properties voit luoda gettereitä ja settereitä
    @property
    def age(self):
        return self._age

"""
# tehtävä 14 Millä kannattaa lukea tiedostoja
"""
from csv import reader
tai
from csv import DictReader
samat kirjoitukselle
"""
# tehtävä 15 Millä hyppäät ensimmäisen rivin yli csv tiedostossa
"""
    next(csv_reader)
"""


# tehtävä 15 Miten saat emailin tai url:n tekstistä regex:llä
#            Yhtenä vastauksena tai useammassa osassa
url = "https?://[A-Za-z.-]+\.[A-Za-z]+"
url = "(https?://)([A-Za-z.-]+\.[A-Za-z]+)"

# tehtävä 15
# tehtävä 15
