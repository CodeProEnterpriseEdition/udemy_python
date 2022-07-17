
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

print("--------------")

def triple_and_filter(numbers):
    filtered = filter(lambda n: n%4==0, numbers)
    return [n*3 for n in filtered]

lst = [1,2,3,4,5,6,12,22,24]

print(triple_and_filter(lst))

def triple_and_filter(numbers):
    return [n*3 for n in numbers if n%4==0]

lst = [1,2,3,4,5,6,12,22,24]

print(triple_and_filter(lst))

def triple_and_filter(numbers):
    return [n*3 for n in numbers if n%4==0]

lst = [1,2,3,4,5,6,12,22,24]

print(triple_and_filter(lst))