
from array import array
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def array_diff(a, b):
    print("array diff")
    print("len a ja b " + str(len(a)) + "  " + str(len(b)))
    return [num for num in a if num not in b]


@speed_test
def array_diff_with_set(a, b):
    print("array diff with set")
    b = set(b)
    print("len a ja len b " + str(len(a)) + "  " + str(len(b)))
    return [num for num in a if num not in b]


lst = [1, 2, 3, 4, 2, 3, 5]
print(set(lst))

# array_diff([1,2,2,2,3],[2]) == [1,3]
# print(list(range(1, 1231, 7)))
# print(list(range(5, 1231, 6)))
a = list(range(1, 123134, 7))
b = list(range(4, 123134, 13)) + list(range(3, 123134, 15)) + \
    list(range(3, 123134, 15)) + list(range(3, 123134, 15))
print(len(a))
print(len(b))

# a = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64,
#      71, 78, 85, 92, 99, 106, 113, 120, 127]
# b = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65,
#      71, 77, 83, 89, 95, 101, 107, 113, 119, 125]

# print(array_diff(a, b))
# print(array_diff(a, b))
a_list = array_diff_with_set(a, b)
b_list = array_diff(a, b)
a_list.sort()
b_sorted = sorted(b_list)
print("a lista " + str(len(a_list)) + " b lista " + str(len(b_sorted)))
if (a_list == b_sorted):
    print("on ne samat!")

if([1, 2, 3, 4] == [2, 3, 1, 4]):
    print("on nääkin samat")
else:
    print("ei ollukkaan samat")
