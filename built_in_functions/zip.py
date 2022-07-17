
from logging.config import dictConfig


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

final_grades = [max(pair) for pair in zip(midterms,finals)]

print(list(final_grades))
print(dict(zip(students, list(final_grades))))

# Vaihtoehtoinen tapa
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students,midterms,finals)}
print(final_grades)

print("--------lambda version-------")
# Vaihtoehtoinen tapa map ja lambda
    # 1. tee zip:llä tuple tuloksista
    # 2. laske niistä maximi
scores = map(
    lambda pair: {pair[0]:max(pair[1],pair[2])}, 
    zip(students,midterms, finals))
print(list(scores))

scores = zip (
    students,
    map(
        lambda pair: max(pair), 
        zip(midterms, finals))
    )
print(dict(scores))
print("---------------")

# zip ensin stringit yhteen saat [('h','h')('i','a')]
# käy for loopissa join kaikki alkiot läpi
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave("hi", "ha"))

print("---------------")

