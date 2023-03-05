# Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:

# Volume Range : label
# 1 cm3 – 10 cm3  : Extra Small
# 11 cm3 – 25 cm3 : Small
# 26 cm3 – 75 cm3 : Medium
# 76 cm3 – 100 cm3 : Large
# 101 cm3 – 250 cm3 : Extra Large
# 251 cm3 and above : Extra-Extra Large

# Take user inputs for height, width, and depth
height = float(input("Enter the height of the cube: "))
width = float(input("Enter the width of the cube: "))
depth = float(input("Enter the depth of the cube: "))

# Calculate the volume of the cube
volume = height * width * depth

# Determine the relevant label based on the volume range
if volume >= 1 and volume <= 10:
    label = "Extra Small"
elif volume >= 11 and volume <= 25:
    label = "Small"
elif volume >= 26 and volume <= 75:
    label = "Medium"
elif volume >= 76 and volume <= 100:
    label = "Large"
elif volume >= 101 and volume <= 250:
    label = "Extra Large"
elif volume >= 251:
    label = "Extra-Extra Large"
else:
    label = "Invalid volume"

# Print the volume and label
print("The volume of the cube is", volume, "cm^3")
print("The label for this volume is", label)
