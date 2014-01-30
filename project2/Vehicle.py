class Vehicle:
	name = ""
	kind = "car"
	colour = ""
	value = 10000.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.colour, self.kind, self.value)
		return desc_str

def getDes(Vehicle):
	Vehicle.name = raw_input("Name: ")
	Vehicle.kind = raw_input("Kind: ")
	Vehicle.colour = raw_input("Colour: ")
	Vehicle.value = float(raw_input("Value: "))

print("\nVehicle 1 -")
car1 = Vehicle()
getDes(car1)
print("\nVehicle 2 -")
car2 = Vehicle()
getDes(car2)

print car1.description()
print car2.description()