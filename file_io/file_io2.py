with open("textfile.txt", "r+") as file:
    print(file.readlines())
print("suljettu on") if file.closed else print("ei kyl oo")

with open("textfile.txt", "a") as file:
    file.write("onpas hemuli kasvanut\n")
print("suljettu on") if file.closed else print("ei kyl oo")


with open("textfile.txt", "r") as file:
    print(file.readlines())
    
# tiedoston kopioiminen
def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)

# tiedoston rivien, sanojen, kirjainten tulostaminen
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

# sanan etsiminen ja korvaaminen uudella sanalla
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()