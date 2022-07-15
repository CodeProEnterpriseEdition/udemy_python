
print("-------------tuples---------------")
# Tuplea ei voi muuttaa
# Voi olla sama data useaan kertaan esim. (1,2,2,3)
# Tuple on nopeampi
# Tuplea voi käyttää dictionaryn avaimena
numbers = (1, 2, 3, 4)

print(numbers)
print(3 in numbers)

print(numbers[2])

# ---------------sets----------------
print("-------------sets---------------")

# Sets:ssä sama arvo voi olla vain kerran
# Sets:ssä arvot ovat epäjärjestyksessä
# Ei voida käyttää indeksiä hakemiseen


set1 = set({1, 2, 3})
print(set1)
set2 = {1, 2, 3}
print(set2)
print(2 in set2)

set2.add(6)
set2.add(6)

print(set2)
set2.discard(3)
print(set2)

# voit yhdistellä
print(set1 | set2)
print(set1 & set2)

set_comprehension = {x**2 for x in set1}
print(set_comprehension)
print("-----------------------")
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:

values = [10, 20, 30]

# Create a variable called static_values which is the result of the values variable converted to a tuple

static_values = tuple(values)

# 4 - Given the following variable

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
