name = input("Enter your character's name: ")

print(f"Welcome {name} to the adventure game!")

answer = input("You are on a quest to find the lost treasure. You come across a fork in the road. Do you want to go left or right? (left/right): ").lower()

if answer == "left":
    print("You chose to go left.")
    answer = input("You are walking through the dark forest and you hear water flowing nearby. you follow the sound and find a river. Do you want to swim to cross the river or walk around it? (swim/walk): ").lower()
    
    if answer == "swim":
        print("There are crocodiles in the river! You are eaten alive. Game Over.")
    elif answer == "walk":
        print("You walked for many miles , ran out of water and died of dehydration. Game Over.")
    else:
        print("Invalid choice. Please choose 'swim' or 'walk'.")
            
elif answer == "right":
    print("You chose to go right.")
    answer = input("You find a cave. Do you want to enter the cave or keep walking? (enter/keep walking): ").lower()
    if answer == "enter":
        print("You enter the cave and find the lost treasure! Congratulations, you win!")
    elif answer == "keep walking":
        print("You keep walking and get lost in the wilderness. Game Over.")
    else: 
        print("Invalid choice. Please choose 'enter' or 'keep walking'.")    
else:
    print("Invalid choice. Please choose 'left' or 'right'.")        