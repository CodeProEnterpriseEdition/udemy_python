#  python csv modules
# reader; iterate over rows as lists
# DictReader; iterate over rows as orderedDicts

from csv import reader, DictReader

with open("fighters.csv") as file:
    csv_reader = reader(file)
    # skippaa ekan rivin
    next(csv_reader)
    for row in csv_reader:
        print(row)

print("\n '|' delimiter \n")

with open("fighters2.csv") as file:
    csv_reader = reader(file, delimiter="|")
    # skippaa ekan rivin
    next(csv_reader)
    for row in csv_reader:
        print(row)


print("\n dict reader \n")

with open("fighters.csv") as file:
    dict_reader = DictReader(file)
    for row in dict_reader:
        print(row)
