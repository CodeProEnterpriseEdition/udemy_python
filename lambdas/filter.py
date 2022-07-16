
# filter käy listan läpi ja ajaa lambda function jokaisen
# elementin kohdalla. Jos tulee True, niin "filtteröi" sen talteen
list_1 = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, list_1))
print(evens)
names = ["austin", "penny", "anthony", "angel", "billy"]
a_names = list(filter(lambda name: name[0] == "a", names))
print(a_names)


def remove_negatives(list1):
    return list(filter(lambda n: n >= 0, list1))


print(remove_negatives([0, 1, 2, 3, -2, -5]))
