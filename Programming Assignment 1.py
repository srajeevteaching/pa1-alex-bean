# Alex Bean
# Course: CS151, Dr.Rajeev
# Wednesday 22 2021
# Programming Assignment: 1
# Length of room, Width of room, Height of room
# Total area of 4 walls and ceiling to be painted in square feet, Gallons of primer needed, and Gallons of paint needed

# Begin by asking for the length, width, and height.
length=input("What is the length (in feet) of the room?")
length=float(length)

width=input("What is the width (in feet) of the room?")
width=float(width)

height=input("What is the height (in feet) of the room?")
height=float(height)

# Then, take the area of the room from the given values.
area=length*width+2*length*height+2*height*width
area=float(area)

# After, you will need to calculate the gallons of primer and paint.
gallons_of_paint=area/350
gallons_of_primer=area/200

# Finally, output the area of the room's needed dimensions and the needed amount of primer and paint.
print("The area of the four walls and the ceiling is", area, "square feet.")
print("You will therefore need", gallons_of_paint,"gallons of paint.")
print("As well as", gallons_of_primer, "gallons of primer.")


