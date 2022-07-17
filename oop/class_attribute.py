class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet")
        self.species = species
cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# tiger = Pet("Tony", "tiger")
print(dog.allowed)
cat.allowed = ["tiger", "elefant"]
Pet.allowed = ["husky", "eagle"]

print(dog.allowed)
print(cat.allowed)

class Chicken:
    
    total_eggs=0
    
    def __init__(self, name, species):
        self.name=name
        self.species=species
        self.eggs=0
    
    def lay_egg(self):
        self.eggs+=1
        Chicken.total_eggs+=1
        return self.eggs