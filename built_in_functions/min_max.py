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
