
first_zip= zip([1,2,3], [4,5,6])
print(list(first_zip))
first_zip= zip([1,2,3], [4,5,6])
print(dict(first_zip))
# zip yhdistää listoja pareiksi
names = ['paavola', 'pekka', 'maija', 'maja']
scores = [123,22,51]
names_scores = (dict(zip(names,scores)))
print(names_scores)
print(list(zip(*names_scores)))

print("------------")
lst = list(range(1,5))
lst5 = list(range(5,10))
print(lst + lst5)

print("------------")
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

high_scores = zip(students,finals)
print(dict(high_scores))

final_grades = [pair for pair in zip(midterms,finals)]

print(list(final_grades))
