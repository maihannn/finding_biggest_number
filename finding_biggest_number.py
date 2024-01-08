#Name: Jamaica C. Palillo
#Section: BSCPE 1-5

# Assignment: Ask the user to input 3 numbers. Find and print the biggest number using only if-else statement.

# ask user to input 3 numbers

# variables
num1 = float ((input ("Please Enter the First Number: ")))
num2 = float ((input ("Please Enter the Second Number: ")))
num3 = float ((input ("Please Enter the Third Number: ")))
maximum = 0


#if-else
if (num1 > num2) and (num1 > num3):
    maximum = num1
    print ("The highest number among the three is: ", num1)
elif (num2 > num1) and (num2 > num3):
    maximum = num2
    print ("The highest number among the three is: ", num2)
else:
    print ("The highest number among the three is: ", num3)


# find the biggest number
    
# display the result