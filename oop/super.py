class Animal:

    def __init__(self, name , species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        # super viittaa parent classiin
        # super().__init__ = Animal.__init__
        super().__init__(name, species)
        # Animal.__init__(self,name,species)
        self.breed = breed
        self.toy = toy

blue = Cat("blue", "cat", "maatiais", "string")
print(blue)

class Character:
    
    def __init__(self, name,hp,level):
        self.name = name
        self.hp = hp
        self.level= level
        

class NPC(Character):
    
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)

    def speak(self):
        return "I head there were monsters running around last night!"

villager = NPC("bob", 100, 12)
print(villager.name)
print(villager.speak())
# mro:lla saat selville luokkien ajojärjestyksen
print(NPC.mro())