list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer = [num for num in list1 if num in list2]
print(answer)
list3 = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in list3]
print(answer2)
numbers = list(range(1,101))
answer3 =  [num for num in numbers if num %12==0]
print(answer3)
answer4 = [char for char in "amazing" if char not in ["a","e","i","o","u"]]
print(answer4)
answer5 = [char for char in "amazing" if char not in "aeiou"] 
print(answer5)