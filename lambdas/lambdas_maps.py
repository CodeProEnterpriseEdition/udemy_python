def square(num): return num * num

print(square(9))

def square2(num): return num * num

def add_values(x, y): return x + y
# korottaa annetun luvun kolmanteen potenssiin
# cube = lambda num: num ** 3


print("-------maps-------")
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x*2, nums)
print(list(doubles))

people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)
