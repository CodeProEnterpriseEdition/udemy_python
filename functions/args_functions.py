# args:in voi nimetä toisinkin
# se kerää kaikki annetut parametrit tupleksi,
# joita voi käyttää functiossa


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(3, 5, 2, 7))


def contains_purple(*args):
    if "purple" in args:
        return True

    return False


print(contains_purple("helo peruna", "purple"))
print(contains_purple("helo peruna purpllalal"))

# Jos haluaa antaa listan *argsille, muista käyttää tähteä list argumentin edessä


def sum_all_from_list(*args):
    total = 0
    for num in args:
        total += num
    return total


list1 = [1, 2, 3, 4]
print(sum_all_from_list(*list1))
