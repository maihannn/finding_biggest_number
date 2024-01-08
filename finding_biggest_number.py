#Name: Jamaica C. Palillo
#Section: BSCPE 1-5

# Assignment: Ask the user to input 3 numbers. Find and print the biggest number using only if-else statement.

# ask user to input 3 numbers

num1 = (input("Please Enter the First number: "))
num2 = (input("Please Enter the Second number: "))
num3 = (input("Please Enter your Third number: "))

#try
# check if number is the max number
if (num1 > num2) and (num1 > num3):
    print ("The maximum number among the three is: " + num1) 
else:
    print ("All number are equal.")

# find the biggest number
# display the result