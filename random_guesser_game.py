import time
import os
import platform
import random
import csv

class Player:
    def __init__(self, name, player_id, score):
        self.name = name
        self.player_id = player_id
        self.score = score
    
    def display(self):
        print(f"Name: {self.name}, ID: {self.player_id}, Score: {self.score}")
'''
Ver 1: Game - Done

Ver 2: Leaderboard Functionality - Done

Ver 3: Sorting Leaderboard Viewing (asc, desc, A-Z, Z-A, asc/desc ID numbers) - upcoming
'''

# Constants
SLEEP_TIME_SHORT = 0.75
SLEEP_TIME_LONG = 1

g_score = 0 #might use later to help track a user's score
g_game_counter = 0

def leaderboard_option():
    print("\nWould you like to add your score to the leaderboard?")
    print("1. Yes")
    print("2. No")

    while True:
        try: 
            choice = int(input("\nChoice (1 or 2): "))
        except ValueError:
            print("Please enter a valid option (1 or 2).\n")
            continue
        if (choice == 1):
            add_to_leaderboard()
            break
        elif (choice == 2):
            print("\nThank you for playing!\n")
            break
        else:
            print("\nInvalid choice. Please choose 1 or 2.")
        
def clear_terminal():
    input("\nPress Enter to clear the terminal")

    # Check the operating system and clear accordingly
    current_os = platform.system().lower()
    
    if current_os == "windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux or macOS

def intro_screen():
    print("\n| ---------------------------------- |")
    print("| Welcome to my Random Guesser Game! |")
    print("| ---------------------------------- |")

#rule screen if user selects option 1
def rules():
    print("\n| ----- |")
    print("| Rules |")
    print("| ----- |")
    print("\nHere is how the game works.")
    print("There are a series of levels.")
    print("Each one is more difficult than the previous one.\n")
    print("    Level 1:")
    print("        Range: 1-5, 3 guesses")
    print("        Correct Guess = 1 point")
    print("    Level 2:")
    print("        Range: 1-10, 5 guesses")
    print("        Correct Guess = 3 points")
    print("    Level 3:")
    print("        Range: 1-50, 10 guesses")
    print("        Correct Guess = 5 points")
    print("    Level 4:")
    print("        Range: 1-100, 20 guesses")
    print("        Correct Guess = 10 points")

    print("\nIf you guess correctly the first time, you get double the points.\n")

def loading_animation(duration=SLEEP_TIME_SHORT, dots=3):
    for _ in range(dots):
        print(".", end='', flush=True)
        time.sleep(SLEEP_TIME_LONG)

#this is level 1 
def level_one():
    global g_score

    print(f"\nThe computer is generating a random number between 1-5: \n")
        
    answer = random.randint(1,5)
    points = 1

    for i in range (1, 4):
        try:
            guess = int(input(f"Guess {i}: "))

            if guess == answer and i == 1:
                print("\nCongratulations! You got it on the first attempt!")
                points *= 2
                g_score = points
                print(f"Score: {g_score}")
                leaderboard_option()
                break
            elif guess == answer and i in range(2,4):
                print(f"\nCongratulations! You got it in {i} attempts!")
                g_score = points
                print(f"Score: {g_score}")
                leaderboard_option()
                break
            else:
                print(f"Invalid Attempts: {i}/3")    
                if (i == 3):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0
        except ValueError:
            print(f"Please enter only integer values.")
            print(f"Invalid Attempts: {i}/3")
            if (i == 3):
                time.sleep(1)
                print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                points = 0
                g_score = 0

#this is level 2
def level_two():
    print(f"\nThe computer is generating a random number between 1-10: \n")
    
    global g_score  
    answer = random.randint(1,10)
    points = 3

    for i in range (1, 6):
        try:
            guess = int(input(f"Guess {i}: "))

            if guess == answer and i == 1:
                print("\nCongratulations! You got it on the first attempt!")
                points *= 2
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            elif guess == answer and i in range(2,6):
                print(f"\nCongratulations! You got it in {i} attempts!")
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            else:
                print(f"Invalid Attempts: {i}/5")    
                if (i == 5):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0
        except ValueError:
            print(f"Please enter only integer values.")
            print(f"Invalid Attempts: {i}/5")
            if (i == 5):
                time.sleep(1)
                print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                points = 0
                g_score = 0
 
def level_three():
    print(f"\nThe computer is generating a random number between 1-50: \n")
    global g_score
    answer = random.randint(1,50)

    points = 5

    for i in range (1, 11):
        try:
            guess = int(input(f"Guess {i}: "))

            if guess == answer and i == 1:
                print("\nCongratulations! You got it on the first attempt!")
                points *= 2
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            elif guess == answer and i in range(2,11):
                print(f"\nCongratulations! You got it in {i} attempts!")
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            else:
                print(f"Invalid Attempts: {i}/10")    
                if (i == 10):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0
        except ValueError:
            print(f"Please enter only integer values.")
            print(f"Invalid Attempts: {i}/10")
            if (i == 10):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0

def level_four():
    print(f"\nThe computer is generating a random number between 1-100: \n")
    global g_score
    answer = random.randint(1,100)

    points = 10

    for i in range (1, 21):
        try:
            guess = int(input(f"Guess {i}: "))

            if guess == answer and i == 1:
                print("\nCongratulations! You got it on the first attempt!")
                points *= 2
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            elif guess == answer and i in range(2,21):
                print(f"\nCongratulations! You got it in {i} attempts!")
                g_score = points
                print(f"Score: {points}")
                leaderboard_option()
                break
            else:
                print(f"Invalid Attempts: {i}/20")    
                if (i == 20):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0
        except ValueError:
            print(f"Please enter only integer values.")
            print(f"Invalid Attempts: {i}/20")
            if (i == 20):
                    time.sleep(1)
                    print(f"\nAwh! Unfortunately the number was {answer}! Better luck next time!")
                    points = 0
                    g_score = 0

#this is a helper for the user to input their level to then put this input into game()
def choice_of_level():
    levels = [1,2,3,4]
     
    while True:
        try:
            level_choice = int(input("Please enter your choice of level [1-4]: "))
            if level_choice in levels:
                return level_choice
            else:
                print("Invalid choice. Please enter a number between [1-4].\n")
        except ValueError:
            print("Please only input integer values.\n")
    
#this function will handle the game itself which is associated with the levels
def game(level):
    if (level == 1):
        level_one()
    elif (level == 2):
        level_two()
    elif (level == 3):
        level_three()
    elif (level == 4):
        level_four()

def options():
    choices = [1,2,3,4,5,6]

    try: 
        print("\nWhat would you like to do?")
        print("1. Read the Rules")
        print("2. Play the Game")
        print("3. View Leaderboard")
        print("4. Add Your Name to Leaderboard")
        print("5. Remove Your Name from Leaderboard")
        print("6. Exit")

        choice = int(input("\nChoose an option between [1-6]: "))

        if choice not in choices:
            print("    Please only input values between [1-6].\n")
        return choice

    except ValueError:
        print("    Please only input integer values between [1-6].")

def view_leaderboard():
    leaderboard = "leaderboard.csv"
    labels = ["Player Name: ", "Player ID: ", "Player Score: "]

    if not os.path.exists(leaderboard):
        with open(leaderboard, "w") as lead:
            pass
    
    with open(leaderboard, "r") as lead:
        data = csv.reader(lead)
        print("\n|-------------|")
        print("| Leaderboard |")
        print("|-------------|\n")
        for row in data:
            #format output
            formatted_output = [f"{label}{value} | " for label, value in zip(labels, row)]
            
            for line in formatted_output:
                csv_row = ','.join(row)
                print(line, end='')

            print()


def add_to_leaderboard():
    g_name = input("Please enter your name: ")
    player_id = random.randrange(100000, 999999, 1)

    leaderboard = "leaderboard.csv"

    with open(leaderboard, "a", newline = '') as lead:
        #lead.write(f"Player Name: {g_name}, Player ID: {g_id}, Player Score: {g_score}\n")
        writer = csv.writer(lead)
        writer.writerow([g_name, player_id, g_score])



def remove_from_leaderboard():
    view_leaderboard()

    found = False
    target_id = input("Please enter your id: ")

    leaderboard = "leaderboard.csv"

    #read all lines
    with open(leaderboard, "r") as lead:
        lines = lead.readlines()

    #write everything back but that id
    with open(leaderboard, "w") as lead:
        for line in lines:
            parts = line.strip().split(", ") #parse the file
            player_id = None 

            for part in parts:
                if part.startswith("Player ID: "):
                    player_id = part.replace("Player ID: ", "") #replace with nothing
                    break

            if player_id is not None and player_id == target_id:
                found = True
                continue
            else:
                lead.write(line)
    
    if found:
        print(f"Player ID: {target_id} was successfully removed.")
    else:
        print(f"Player ID: {target_id} does not exist.")
                
#this function handles the decision for the initial user input
def decision(choice):
    #next step: functions 3-5
    
    decision = 0

    if choice == 1:
        rules()
    elif choice == 2:
        level_choice = choice_of_level()
        game(level_choice)
    elif choice == 3:
        view_leaderboard()
    elif choice == 4:
        add_to_leaderboard()
    elif choice == 5:
        remove_from_leaderboard()
    elif choice == 6:
        print("\nThank you for playing my Number Guessing Game!")
        print("Have a nice rest of your day!")
        clear_terminal()

        decision = 1
    
    return decision

def main():
    intro_screen()

    while True:
        if decision(options()) == 1:
            break                               

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting gracefully.")
        time.sleep(1)
        clear_terminal()
