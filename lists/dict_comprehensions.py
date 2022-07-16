numbers = dict(first=1, second=2, third=3)
print(numbers)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

num_list = list(range(1, 5))
eo_list = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(eo_list)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]: person[i][1] for i in range(0, len(person))}
print(answer)

answer = {thing[0]: thing[1] for thing in person}
print(answer)

answer = {key: value for key, value in person}
print(answer)

answer = dict(person)
print(answer)

answer = {char: 0 for char in 'aeiou'}
print(answer)

answer = dict.fromkeys("aeiou", 0)
print(answer)

answer = {count: chr(count) for count in range(65, 91)}
print(answer)
print(chr(65))
