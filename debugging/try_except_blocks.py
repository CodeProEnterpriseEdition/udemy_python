
print("hellos")
d = {"name": "Ricky"}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, "city"))

print("after")
