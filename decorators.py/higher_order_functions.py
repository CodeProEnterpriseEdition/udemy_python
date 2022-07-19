# We can pass funcs as args to other funcs

def sum(n, func):
	total = 0
	for num in range(1,n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x


print(sum(3,cube))
print(sum(3,square))
# ----------------------------------------------
from random import choice
# We can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())
