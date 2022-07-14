paivat = {2: "Monday", 3: "Tuesday", 4: "Wednesday",
          5: "Thursday", 6: "Friday", 7: "Saturday", 1: "Sunday"}


def return_day(number):
    return paivat.get(number)


print(return_day(2))


def last_element(list1):
    return list1.pop() if bool(list1) else None


list1 = list(range(1, 10))
print(last_element(list1))
list1 = []
print(last_element(list1))


def last_element(l):
    if l:
        return l[-1]
    return None


list1 = list(range(1, 10))
print(last_element(list1))
list1 = []
print(last_element(list1))


print("----------")


def single_letter_count(word, letter):
    count = word.upper().count(letter.upper())
    return 0 if count == 0 else count


print(single_letter_count("perunapate", "E"))
print(single_letter_count("perunapate", "i"))

print("----------")


def multiple_letter_count(text):
    new_dict = {key: text.count(key) for key in text}
    return new_dict


def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


print(multiple_letter_count("awesome"))

print("----------")

list1 = list(range(10))


def list_manipulation(collection, command, location, value=None):
    if command == "remove" and location == "end":
        return collection.pop()
    elif command == "remove" and location == "beginning":
        return collection.pop(0)
    elif command == "add" and location == "beginning":
        return collection.insert(0, value)
    elif command == "add" and location == "end":
        return collection.append(value)


def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0, value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection


print(list1)
print(list_manipulation(list1, "remove", "end"))
print(list1)
print(list_manipulation(list1, "remove", "beginning"))
print(list1)
print(list_manipulation(list1, "add", "end", 20))
print(list1)
print(list_manipulation(list1, "add", "beginning", 11))
print(list1)
