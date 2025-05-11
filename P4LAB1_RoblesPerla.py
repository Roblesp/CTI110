# Perla Robles
# 3/19/2025
# P4LAB1
# Turtle graphics program to draw triangle and square

import turtle 
win = turtle.Screen()
win.bgcolor('pink')
timmy = turtle.Turtle()

# set the way tmmy looks
timmy.pensize(6)
timmy.pencolor('purple')
timmy.shape('arrow')

# Test 
# timmy.forward(100)

# for loop that runs 4 times
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

#while loopthat runs 3 times
this_run = 0

while this_run < 3:
    timmy.forward(100)
    timmy.left(120)
    this_run += 1

# Keeps the window open after shape is drawn
win.mainloop()

