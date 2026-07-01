print("Welcome to the Quiz Game!")

playing = input("Are you ready to play? (yes/no): ").lower()

if playing != "yes":
    quit()
    
print("Great! Let's get started.")
score = 0

answer = input("Which keyword creates a function? ").lower()
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is def.")   
    
answer = input("Abstract class purpose? ").lower()
if answer.lower() == "Hide implementation":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Hide implementation.")  
    
answer = input("OOP stands for? ").lower()
if answer.lower() == "Object Oriented Programming":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Object Oriented Programming.")  


answer = input("Retrieve data? ").lower()
if answer.lower() == "SELECT":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is SELECT.")  


answer = input("Unique identifier? ").lower()
if answer.lower() == "Primary Key":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Primary Key.")                       
    

answer = input("Instance of class is? ").lower()
if answer.lower() == "Object":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Object.")  

print("You got " + str(score) + " questions correct!")

print("You got " + str((score / 6) * 100) + "%.")
        