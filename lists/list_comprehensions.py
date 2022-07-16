from traceback import print_tb


nums = list(range(1, 10))

print(nums)
print([x*10 for x in nums])

name = 'colt'
print([char.upper() for char in name])

friends = ['hemuli', 'haihattelia', 'jumppailija']
print([name.capitalize() for name in friends])

print(bool("asd"))

evens = [num for num in nums if num % 2 == 0]
print(evens)
bigger = [num for num in nums if num > 4]
print(bigger)

persons = ["Elie", "Tim", "Matt"]
answer = [person[0] for person in persons]
numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in numbers if num % 2 == 0]
