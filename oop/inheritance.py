class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

a = Animal()
a.make_sound("Chirp")
cat = Cat()
cat.make_sound("meaow")

print(isinstance(cat,Animal))
print(isinstance(cat,Cat))