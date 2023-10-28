# Gabriel Sanchez-Jorgensen
# Assignment Module 2.2
# 10/28/2023

# Creating a program that can calculate the cost of fiber optic cable per square feet for user.

# Display a welcome message
print("Welcome to Bellevue Fiber Optics!")

# Get the number of fiber optic feet to be installed
feetOfFiberOpticCable = float(input("How many feet of fiber optic cable do you need? "))

# Multiply the total cost based on the number of feet requested.
if feetOfFiberOpticCable > 500:
    cost = feetOfFiberOpticCable * 0.50
elif feetOfFiberOpticCable > 250:
    cost = feetOfFiberOpticCable * 0.70
elif feetOfFiberOpticCable > 100:
    cost = feetOfFiberOpticCable * 0.80
else:
    cost = feetOfFiberOpticCable * 0.87

# Display the calculated information and company name.
print(f"Your total is {cost:.2f} dollars.\n" "-Bellevue Fiber Optics")

# I'm adding this last command so that if run on Python,
# the program does not immediately close after calculation is run.
print("Press Enter to exit.")
input()
