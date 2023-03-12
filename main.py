# developed by Paecho


import methods as meth
import col
import graph as gr

# variables
valid = False


while not valid:  # loop until the user enters a valid int
    try:
        dis = int(input('Enter the length of a side: '))
        valid = True  # if this point is reached, x is a valid int So valid is true

    except ValueError:
        print('Please only input valid answer like - 123')

valid = False  # value set default

while not valid:   # loop until the user enters a valid int
    try:
        sides = int(input("Enter the Sides : "))  # the sides of
        valid = True  # if this point is reached, x is a valid int So valid is true
        if 10 < sides or sides <= 2:
            valid = False
            print("value out of range !!!! range (3,4,5,6,7,8,9,10)")
    except ValueError:
        print('Please only input valid answer like - 123')
c = input("Select Colour : \nred - 1\nblue - 2 \nblack - 0\n : ")
colour = col.colo(c)
print(colour)
gr.draw(dis, sides, colour)

