#Name: Jamaica C. Palillo
#Section: BSCPE 1-5

# Assignment: Ask the user to input 3 numbers. Find and print the biggest number using only if-else statement.

# adding window
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title ("Biggest Number Finder")
root.geometry ("350x200") 
bg_color="#C1ECEA"


def get_number ():
    try:

        # getting the inut
        num1 = float (input ("Enter the First Number: "))
        num2 = float (input ("Enter the Second Number: "))
        num3 = float (input ("Enter the Third Number: "))
        largest = 0
        
    except ValueError:
        print ("Error.")

    #if-else
    if num1 >= num2 and num1 >= num3:
        largest = num1
        print (f"The Largest Number among the Three is {num1}")
    elif num2 >= num1 and num2 >= num3:
        largest = num2
        print (f"The Largest Number among the Three is {num2}")
    else:
        largest = num3
        print (f"The Largest Number among the Three is {num3}")

    return largest

# creating widgets

title = Label (root, text = "Biggest Number Finder", font=("STIX", 20, "bold"), fg="#F63392", bg="#C1ECEA")
title.pack (fill=X)

num1 = Label (root, text = "Please Enter the First Number", font=("Garuda", 10, "bold"), fg = "#3B9A95", bg="#C1ECEA")
num1_entry = Entry (root)
num2 = Label (root, text = "   Please Enter the Second Number", font=("Garuda", 10, "bold"), fg = "#3B9A95", bg="#C1ECEA")
num2_entry = Entry (root)
num3 = Label (root, text = "Please Enter the Third Number", font=("Garuda", 10, "bold"), fg = "#3B9A95", bg="#C1ECEA")
num3_entry = Entry (root)
find_button = Button (root, text = "Find the Maximum Number")

# adding widgets
title.grid (row = 0, column =0, columnspan = 2)
num1.grid (row=1, column=0)
num1_entry.grid (row=1, column=1)
num2.grid (row=2, column=0)
num2_entry.grid (row=2, column=1)
num3.grid (row=3, column=0)
num3_entry.grid (row=3, column=1)


root.mainloop()
