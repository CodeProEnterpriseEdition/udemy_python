with open("textfile.txt", "r+") as file:
    print(file.readlines())
print("suljettu on") if file.closed else print("ei kyl oo")

with open("textfile.txt", "a") as file:
    file.write("onpas hemuli kasvanut\n")
print("suljettu on") if file.closed else print("ei kyl oo")


with open("textfile.txt", "r") as file:
    print(file.readlines())
    
