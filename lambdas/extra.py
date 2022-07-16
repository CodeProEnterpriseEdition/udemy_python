

# https://www.youtube.com/watch?v=BcbVe1r2CYc
def func(x):
    return x+5

print(func(2))

func2 = lambda x: x+5

print(func2(2))
print()

a = list(range(1,11))
b = list(range(11))

print(a)
print(b)

newList = list(map(func2, a))
newList_lambda = list(map(lambda x: x+5, a))

print(newList)
print(newList_lambda)

print(list(filter(lambda n: n%2 ==0, b)))



