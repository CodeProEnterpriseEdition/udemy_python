
# import regex module
import re


# define our phone number regex
# HUOM muista laittaa "r" eteen, se tekee stringistä raw stringin
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with our regex
res = pattern.search('call me at 415 555-4242!')

print(res)
print(res.group())

# vaihtoehtoinen tapa käyttää regex searchia
res2 = re.search(r'\d{3} \d{3}-\d{4}', 'call me at 415 555-4242!')
print(res2.group())
