

# raise ValueError('invalid value')
print("hello")


def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be strings")
    if type(color) is not str:
        raise TypeError("color must be strings")
    if color not in colors:
        raise ValueError("Color not choosable")
    print(f"Printed {text} in {color}")


colorize("hello", "cyan")
colorize("hello", 1)
colorize("hello", "red")
