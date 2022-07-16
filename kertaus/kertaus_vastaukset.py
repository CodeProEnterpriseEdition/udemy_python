
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
# tehtävä 1


# tehtävä 1


# tehtävä 1
