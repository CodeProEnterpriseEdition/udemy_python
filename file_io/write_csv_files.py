from csv import reader, writer

with open("fighter3.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    
    
with open("fighters.csv", "r") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in fighters:
        print(row)
    # csv_writer.writerow(["Character", "Move"])
    # csv_writer.writerow(["Ryu", "Hadouken"])

with open("screaming.csv", "w") as file:
    csv_writer = writer(file)
    for row in fighters:
        csv_writer.writerow(row)
        print(row)


#  siistimpi tapa hoitaa tää

with open("fighters.csv") as file:
    csv_reader = reader (file)
    with open("screaming_fighters2.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])