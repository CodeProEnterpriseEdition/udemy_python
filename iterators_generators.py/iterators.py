
# iterator on jotain mikä palauttaa arvon kun sitä kutsutaan
# next() functiolla

# iterable palauttaa iterator:in kun iter():llä kutsutaan sitä

# next() on iterator, se palauttaa seuraavan elementin kunnes 
# tulee StopIteration error

name = "Oprah"
# next(name) # TypeError: 'str' object is not an iterator

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

print("---------")

# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)
		
def square(x):
	print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)

def gen1():

    yield "I am the bone of my sword"
    yield "Steel is my body and fire is my blood"
    yield "I have created over a thousand blades"

temp_gen1 = gen1()
print(  next(temp_gen1) )
print(  next(temp_gen1) )
print(  next(temp_gen1) )


print(list(range(99, -1, -1)))

