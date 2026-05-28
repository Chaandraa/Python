"""
conditional statements in python

you cab use logical operators as well.
    """
    
# Q1. Accept 2 numbers from user and print the greatest number among them.
"""
a = float(input("Enter first number: "))

b = float(input("Enter second number: "))
 

if a > b:
    print("The greatest number is:", a)
elif b > a:
    print("The greatest number is:", b)
else:
        print("Both numbers are equal.")
"""
 
 #Q2. Accept gender from user and print message accordingly.ex: if user enters "male" then print "Good morning Sir"
"""gender = input("Enter your gender (male/female): ").lower()

user_input = gender[0]

if not user_input:
    print("Please enter a your gender it is required")
    
if user_input == "m":
    print("Good morning Sir")
else:
    print("Good morning Ma'am")            
"""

#Q3.Accept an integer from user and check whether it is even or odd.
"""
number = input("Enter an integer: ")
try: #to handle the error if user enters a non-integer value
    num= int(number)
        
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Invalid input. Please enter an integer.") 
"""

#Q4.accept name and age from user and find out whether the person is eligible to vote or not. (age should be greater than or equal to 18)
#name = input("Enter your name:")
#try:
#    age = int(input("enter your age:"))

#    if age <0 or age >= 120:
#        print("Please enter a valid , realistic age.")
#    elif age >= 18:
#        print(f"{name} is eligible to vote.")
#    else:
#        print(f"{name} is not eligible to vote.")    
#except ValueError:
#    print("Invalid input. Please enter a valid age.")        

#Q5. Accept year from user and check if its a leap year or not. (A leap year is divisible by 4 but not by 100, except if it is divisible by 400)
# year = input("Enter a year: ")
# try:
    # year = int(year)
    # if(year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        # print(f"{year} is a leap year.")
    # else:
        # print(f"{year} is not a leap year.")
# except ValueError:
    # print("Invalid input. Please enter a valid year.")

  