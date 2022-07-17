# try:
#     except:
#         else:
# ajetaan silloin kun ei tule erroria
#             finally:
# ajetaan aina lopuksi

from decimal import DivisionByZero
from typing import Type


try:
    num = int(input("please enter a number: "))
    print(num)
except:
    print("thats not a number!")
else:
    print("im in else")
finally:
    print("lopultakin")

print("---")


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zeron please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


print(divide(1, 2))
print("------")
print(divide(1, "asd"))


def divide(num1, num2):
    try:
        result = num1//num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return result


print(divide(4, 2))
print(divide(4, "1"))
print(divide(4, 0))
