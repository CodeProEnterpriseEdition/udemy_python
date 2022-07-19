# decorators sisällyttää toisia functioita ja 
# lisää toiminnallisuuksia

from functools import wraps

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Colt.")

def rage():
	print("I HATE YOU!")

# we are decorating our function 
# with politeness!
greet = be_polite(greet)

polite_rage = be_polite(rage)
polite_rage()

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")

@be_polite
def rage():
	print("I HATE YOU!")

greet()
rage()

print("--------")

def calculate_twice(fn):
    @wraps(fn)
    def wrapper(*args):
        print(f"function name {fn.__name__}")
        print(f"function doc {fn.__doc__}")
        return fn(*args)
    return wrapper

def do_maths(fn):
    def wrapper(*args):
        print(f"do some maths")
        return fn(*args)
    return wrapper

def adding(num1,num2):
    return num1 + num2

# decoratorin voi antaa näin
maths = calculate_twice(adding)
print(maths(1,1))
print(maths(2,2))

# tai näin, tai vaikka useamman!
@do_maths
@calculate_twice
def multiply(num1,num2):
    """Täällä kerrotaan asioita!"""
    return num1 * num2

@calculate_twice
def square(num1):
    """neliöt ovat jänniä!"""
    return num1 * num1

print(multiply(2,3))
print(square(2))
print(square.__name__)
print(square.__doc__)


print("------------")

# from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ints_are_true = True
        for arg in args:
            if type(arg)==int:
                ints_are_true = True
            else:
                ints_are_true = False
        if ints_are_true:
#  MUISTA PALAUTTAA FUNCTIO!
            return fn(*args, **kwargs)
        else: 
            return "Please only invoke with integers."
    return wrapper

def only_ints2(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner


@only_ints
def summing(*args):
    return sum(args)

print(summing(1,2,3))

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        else:
            return "Unauthorized"
    return wrapper