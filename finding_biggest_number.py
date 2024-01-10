#Name: Jamaica C. Palillo
#Section: BSCPE 1-5

# Assignment: Ask the user to input 3 numbers. Find and print the biggest number using only if-else statement.

# adding window
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title ("Highest Number Finder")
root.geometry ("875x450") 
bg_color = "#C1ECEA"


def highest_number ():
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
# title widget
title = Label (root, text = "Biggest Number Finder", font=("STIX", 20, "bold"), fg="#F63392", bg="#C1ECEA", relief=GROOVE, bd=10)
title.pack (fill=X)



# creating widgets

# adding widgets for entry or inputs
# title: input number
input_number=Label(root, text = "Input a Number", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
input_number.place(x=5, y=55, width=520, height=65)


# for inputting numbers
input_num=LabelFrame(root, bg="#EED3E1", relief=GROOVE, bd=7)
input_num.place(x=5, y=120, width=520, height=240)

number1=Label(input_num, text=" 1st Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number1.grid(row=1, column=0, padx=20, pady=15)
number1=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER)
number1.grid (row=1, column=1, padx=20, pady=15)
number2=Label(input_num, text="2nd Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number2.grid(row=2, column=0, padx=20, pady=15)
number2=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER)
number2.grid (row=2, column=1, padx=20, pady=15)
number3=Label(input_num, text="3rd Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number3.grid(row=3, column=0, padx=20, pady=15)
number3=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER)
number3.grid (row=3, column=1, padx=20, pady=15)

# title: highest number
highest_number=Label(root, text = "Highest Number", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
highest_number.place(x=525, y=55, width=345, height=65)



root.mainloop()
