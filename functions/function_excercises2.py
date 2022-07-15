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
