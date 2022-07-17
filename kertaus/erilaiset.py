lst = [1, 2, 3]
dictionary1 = {'eka': 1, 'toka': 2, 'kolmas': 3}
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}

print(lst)
print(dictionary1)
print(tuple1)
print(set1)

      # input   function logic
lambda  x:      x+5
      # function logic          input list
map     (lambda x: x+5,         lst)
      # function logic          input list
filter  (lambda n: n>0,         lst)

# list comprehensions
# output      for loop          conditional for every number
lst_comp = [number       for number in lst if number >2]
print(lst_comp)

# dict comprehensions
# output      for loop          conditional for every number
dict_comp = {key: value   for key, value in dictionary1.items() if value >2}
print(dict_comp)