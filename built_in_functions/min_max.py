lst = list(range(1, 10, 3))
print(lst)
print(max(lst))

names = ("Arya", "Samson", "Dore", "Tim", "ollicander")

print(max([len(name) for name in names]))
# Huom! ei tarvii sulkuja, jolloin kyseessä ei ole lista vaan
# general expression, joka on laskennallisesti/tilanpuolesta tehokkaampi
print(min(len(name) for name in names))

# lambda käy kaikki nimet läpi, ja tekee listan pituuksista?
#
print(max(names, key=lambda n: len(n)))


songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print(lst)
print(max(lst))
print(max(names))
print(min(names, key=len))
# lambda tekee listan laulujen playcount:sta
# jonka jälkeen max() functio palauttaa niistä isoimman
print(max(songs, key=lambda n: n['playcount']))

print("-----")
lst = [1,2,3,4,5]
nums = [99, 25, 30 ,-7]
name = 'alcatraz'

extremes = lambda iterable: (min(iterable), max(iterable))

print(extremes(lst))
print(extremes(nums))
print(extremes(name))