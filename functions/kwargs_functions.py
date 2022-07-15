# kwargs = keyword arguments
#  eli dictionary annetaan functiolle parametreinä
# functio voi sitten käyttää kwargs muuttujaa kuten se
# olisi dict


def combine_words(word, **kwargs):
    new_word = word
    if 'prefix' in kwargs:
        new_word = kwargs["prefix"] + word
    if 'suffix' in kwargs:
        new_word = word + kwargs["suffix"]
    return new_word


print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("work", suffix="er"))
print(combine_words("work", prefix="home"))


def test_kwargs(**kwargs):
    if kwargs['jpa']:
        print("on kyl")
    return kwargs['jpa']


print(test_kwargs(jpa="kylkyl"))


def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))


def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}
display_names(**names)
display_names(first="Colt", second="Rusty")
display_names(**{"first": "Colt", "second": "Rusty"})


def add_and_multiply_numbers(a, b, c):
    print(a + b + c)


data = dict(a=1, b=2, c=3)
add_and_multiply_numbers(**data)
