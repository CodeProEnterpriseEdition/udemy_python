
from inspect import stack


def high_and_low(str_line_of_numbers):
    sorted_list = sorted([int(n) for n in str_line_of_numbers.split()])
    return "".join(str(sorted_list[-1]) + " " + str(sorted_list[0]))


print(high_and_low("1 2 3 4 5"))  # return "5 1"
print("-------")
print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
print("-------")
print(high_and_low("1 9 3 4 -5"))  # return "9 -5"
print("-------")
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))  # return "42 -9"
