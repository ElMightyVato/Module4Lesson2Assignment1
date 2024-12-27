class Vehicle:
    def __init__(self, reg_num, type, owner): 
# Reg_num is for the cars registration number
# Type is what kind of vehicle
# Owner is for the name of the owner
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
# new_owner is for the new owner
        self.owner = new_owner
        print(f"The owner of {self.type} {self.registration_number} has been updated to {self.owner}.")

# Creating instances of the Vehicle class
vehicle1 = Vehicle("KYS698", "Car", "Joe Biden")
vehicle2 = Vehicle("SUG456", "Truck", "Donald Trump")

# Displaying initial details of vehicles
print(f"Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Changing the owner of vehicle1
vehicle1.update_owner("Baraka Obama")

# Changing the owner of vehicle2
vehicle2.update_owner("Hillary Cliton")

# Displaying updated details of vehicles
print(f"Updated Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Updated Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
