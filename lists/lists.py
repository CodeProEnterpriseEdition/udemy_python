r = list(range(1,10))
print(r)

people = ["hemuli", "jeppa", "hmmhmm"]

print("hemuli" in people)
print("hemuli2" in people)

print(len(people))

people[1] = "humppaaja"

print(people)

for henkilö in people:
    print(henkilö)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result=""
for item in sounds:
    result+= item.capitalize()
print(result)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result=""
for item in sounds:
    result+= item.upper()
print(result)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds.append(2)
print(sounds)

sounds2 = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds2.extend([2,4,5])
print(sounds2)
sounds2.pop(1)
print(sounds2)
sounds2.pop()
print(sounds2)

sounds3 = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds3.insert(2,[2,4,5])
print(sounds3)
sounds3.remove('fragil')
print(sounds3)
sounds3.clear()
print(sounds3)

sounds3 = ["super", "cali", "ali","fragil", "istic", "expi", "ali", "docious"]
print(sounds3.index("super"))
print(sounds3.index("ali", 3))
print(sounds3.count("ali"))
print(sounds3.count("ali"))
sounds3.reverse()
print(sounds3)

sounds3.reverse()
print(" ".join(sounds3))
vali = "=> "
print(vali.join(sounds3))

instructors = ["Colt", "Blue", "Lisa"]

print(instructors)
instructors.pop()
print(instructors)
instructors.pop(0)
print(instructors)
instructors.insert(0, "Done")
print(instructors)

numbers = list(range(1,10))
print(numbers)