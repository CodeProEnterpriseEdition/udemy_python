def is_palindrome(text):
    is_palindrome = True
    for index in range(len(text)):
        if text[-index-1] != text[index]:
            is_palindrome = False
    return is_palindrome


print(is_palindrome("hahhah"))
print(is_palindrome("peruna"))


def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]


print(is_palindrome("hahhah"))
print(is_palindrome("peruna"))

def multiply_even_numbers(numbers_list):
    sum = 1
    for n in range(len(numbers_list)):
        if numbers_list[n] % 2 == 0:
            sum = sum * numbers_list[n]
    return sum

print(multiply_even_numbers([2,3,4,5,6]))

#  etsi samat arvot kahdesta listasta
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]