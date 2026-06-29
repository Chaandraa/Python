import random 

# constants

#why are these outside the function? because we want to use them in multiple functions. If we put them inside a function, they will only be accessible in that function. By putting them outside, we can use them in any function in this file.

MAX_LINES = 3 #this is used to limit the number of lines the user can bet on. It is set to 3 because we have 3 rows in our slot machine.
MAX_BET = 100 #this will limit the amount the user can bet oneach line.We dont want them to use a lot in one single line.
MIN_BET = 1 #this will limit the amount the user can bet on each line.Its the minimum value we dont want some negative or 0.

ROWS = 3 # this is used to limit the number of rows in our slot machine. It is set to 3 because we have 3 rows in our slot machine.
COLS = 3 #this is used to limit the number of columns in our slot machine. It is set to 3 because we have 3 columns in our slot machine.

#the below dictionary symbol_count tell us how many of each symbol we have in 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

"""This function here is responsible of user input and keep asking unlit they give valid input.
   the function works as follows:
    1. It will ask the user to input the amount they want to deposit.
    2. It will check if the input is a valid number using the isdigit() method.
    3. If the input is a valid number, it will convert it to an integer and check if it is greater than 0.
    4. If the input is not a valid number or less than or equal to 0, it will print an error message and ask for the input again.
"""
def deposit():
    #this is a while loop that will keep asking for the input until the user gives a valid input.
    while True:
        amount = input("What would you like to deposit? $")
        
        #now i put a condition .isdigit that checks for a valid number. We dont want to accept negative numbers or letters.
        if amount.isdigit():
            #amount is a string so we need to convert it to an integer.
            amount = int(amount)
            if amount > 0: # amount must be greater if not 0 than we will have to ask for the input again.
                break
            else:
                print("Amount must be greater than 0.")
        #here the else works as a catch for any invalid input that is not a number. It will print the message and ask for the input again.        
        else:
            print("Please enter a number.")
    #now we return my amount variable to be used in the main function.
    return amount

""" This function is responsible for getting the number of lines the user wants to bet on. It will keep asking for the input until the user gives a valid input. The function works as follows:
    1. It will ask the user to input the number of lines they want to bet on.
    2. It will check if the input is a valid number using the isdigit() method.
    3. If the input is a valid number, it will convert it to an integer and check if it is between 1 and MAX_LINES.
    4. If the input is not a valid number or not in the range, it will print an error message and ask for the input again.
"""
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #MAX LINES is a constant that we defined at the top of the file. It is used to limit the number of lines the user can bet on.
                break #break will exit the while loop and return the value of lines.if the input is not a valid number or not in the range, it will print an error message and ask for the input again.
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

""" This function is responsible for getting the amount the user wants to bet on each line. It will keep asking for the input until the user gives a valid input. The function works as follows:
    1. It will ask the user to input the amount they want to bet on each line.
    2. It will check if the input is a valid number using the isdigit() method.
    3. If the input is a valid number, it will convert it to an integer and check if it is between MIN_BET and MAX_BET.
    4. If the input is not a valid number or not in the range, it will print an error message and ask for the input again.
"""
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

""" We want to check if the user have enough balance for the desired bet.so this fuction does exactly that. It will use get_number_of_lines() and get_bet() to get the number of lines and the amount the user wants to bet on each line. It will then calculate the total bet and check if the user has enough balance. If not, it will print an error message and ask for the input again. If the user has enough balance, it will spin the slot machine and check for winnings. It will then return the net change in balance (winnings - total bet)."""

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#I updated the main function to show "you ran out of money" when the balance is 0 or less. I also added a check to see if the user has enough balance to bet on the desired number of lines and amount. If not, it will print an error message and ask for the input again. If the user has enough balance, it will spin the slot machine and check for winnings. It will then return the net change in balance (winnings - total bet). before it was an endless loop that would keep running even when the user ran out of money.
def main():
    balance = deposit()

    while True:

        print(f"Current balance is ${balance}")

        # stop if no money left
        if balance <= 0:
            print("You ran out of money!")
            break

        answer = input("Press enter to play (q to quit): ").lower()

        if answer == "q":
            break

        # only allow Enter
        if answer != "":
            print("Invalid input.")
            continue

        balance += spin(balance)

    print(f"You left with ${balance}")


main()