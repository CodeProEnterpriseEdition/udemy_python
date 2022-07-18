class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0

jane = Human("Jane", "Goodall", 50)
print(jane.age)
jane.age = -100
print(jane.age)
jane.age = 40
print(jane.age)