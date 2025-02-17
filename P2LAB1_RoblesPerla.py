#Perla Robles
#02/17/2025
#P2LAB1
#Using formatting and floats

import math

# Get the radius from user as float
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = 2 * radius

# Calcuate circumference
circum = 2 * math.pi * radius

# Calculate area
area =  math.pi * radius ** 2 

# Display values to user
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circum:.2f}")
print()
print(f"The area of the circle is {area:.3f}")