
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y


def eat_food(food):
    assert food in ["peruna", "pizza",
                    "karkki"], "Hei älä nyt {} syö".format(food)
    print("im eating {}".format(food))


print(add_positive_numbers(1, 2))
# print(add_positive_numbers(1, -2))
eat_food("pizza")
eat_food("pahvi")
