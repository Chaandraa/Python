"""num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    elif num1<num2:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num1} and {num2} are equal.")
else:
    print("Enter valid numbers only.")"""
    
"""gender = input("Please enter your gender: ")

if gender.lower() == "male":
    print(" Good Morning! Sir.")
elif gender.lower() == "female":
    print("Good Morning! Ma'am.")
else:
    print("Invalid gender entered.")"""

"""
num = input("Enter a number: ")    

if num.isdigit():
    num = int(num)
    if num%2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
else:
    print("Please enter a valid number.")
"""

"""name = input("Please enter your name: ")
if name.isalpha():
    print(f"Hello, {name}! Please enter your age to check if you are eligible to vote.")
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age >= 18:
            print(f"Congratulations, {name}! You are eligible to vote.")
        else:
            print(f"Sorry, {name}. You are not eligible to vote yet.")
    else:
        print("Please enter a valid age.")"""


"""year = int(input("Please enter a year: "))

if (year % 4==0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")"""
    
"""temp = input("Please enter the temperature in Celsius: ")
temp = float(temp)
if temp < 0:
        print("Freezing")  
    
elif 0<= temp <10:
        print("Very Cold")
elif 10<= temp <20:
        print("Cold")  
elif 20<= temp <30:
        print("Pleasant")
elif 30<= temp <40:
        print("Hot")
else:
        print("Very Hot")"""
        
        
"""print("Welcome! We are Toby's. Please fill the necessary information below so we can proceed further :) ")

name = input("Enter your name: ").strip().lower()        
age = input("Enter your age as per the ID: ")
password = input("Enter the 8 character password: ")

if age.isdigit():
    age = int(age)
    
    if age >=18:
        print("Allowed")
    else: 
        print("Not Allowed") 
else:
    print("Please enter a valid age.")"""
    

"""password = input("Enter the 8 character password: ")

if len(password) < 8:
    print("Weak Password.")
elif password.isalpha():
    print("Add digits to make it stronger.")
elif password.isdigit():
    print("Add letters to make it stronger.")
else:
    print("Strong Password.")"""            


"""num = input("Enter a number: ")

try:
    num = float(num)
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is zero.")
except ValueError:
    print("Please enter a valid number.")"""
    
"""print("check if a number is divisible by 3 and 5")

num = int(input("Enter a number: ")) 

if num % 3 == 0 and num % 5 == 0:
    print("Jackpot! The number is divisible by both 3 and 5.")
elif num%3 == 0:
    print("The number is only divisible by 3.")  
elif num%5 == 0:
    print("The number is only divisible by 5.")
else:
    print("The number is not divisible by either 3 or 5.")"""
    
"""import random    
print("Stop and check the traffic light color!")

light_color = random.randint(0, 2)
     # red: 0, yellow: 1, green: 2

if light_color == 0:
    print("Red light! Stop.")
elif light_color == 1:
    print("Yellow light! Slow down.")
else:
    print("Green light! Go.")"""     
     
"""print("Welcome to Syne-plex! Please enter your age to get the Discount or price on your movie ticket.")  

age = input("Enter your age: ")

if not age.isdigit():
    print("Please enter a valid age.")
    
else:
    age = int(age)
    
    if age < 5:
        print("Free!")
        
    elif  age >= 5 and age < 18:
        print("Pay 150/-.")
        
    elif age >= 18 and age <= 60:
        student_status = input("Are you a student? (yes/no): ").strip().lower()
        
        if student_status == "yes":
            print("Pay", 300-(300*0.2), "/-.")
        else:
            print("Pay 300/-.")
            
    else:
        print("Pay 100/-.")"""


"""print("Triangle Validator")

a, b, c = map(float, input(
    "Enter 3 sides separated by spaces: "
).split())

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")"""                                              
       