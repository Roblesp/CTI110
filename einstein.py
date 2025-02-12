#This program calucualtes energy in joules

print("clcuate energy based on mass entered!!")

#Get the mass from the user
mass = float(input("Enter the mass of the object:"))

#Declare the variable spead_of_light
speed_of_light = 299792458

# Calculate E of energy
energy = mass * speed_of_light ** 2

# Display results to the screen
print("The formula for energy is energy = mass * speed_of_light ** 2 and the value is", energy)
