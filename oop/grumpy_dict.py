class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data

print("--------------")

class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars
        
    def __repr__(self):
        return "{} car train".format(self.num_cars)
    
    def __len__(self):
        return self.num_cars

a_train = Train(4)
print(a_train)
print(len(a_train))


# class GrumpyDict(dict):
# 	def __repr__(self):
# 		print("NONE OF YOUR BUSINESS")
# 		return super().__repr__()

# 	def __missing__(self, key):
# 		print(f"THAT THING YOU WANT ISN'T IN HERE")

# 	def __setitem__(self, key, value):
# 		print("Why do you always have to change things?")
# 		print(f"Ugh fine, setting {key} to {value}")
# 		super().__setitem__(key, value)