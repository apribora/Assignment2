import time
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

low_list = ["Higher", "Too low", "Moreeee", "My number is higher"]
high_list = ["Lower", "Too high", "Lessss", "My number is lower"]

#score tracking
user_score = 0
pc_score = 0
def display_score(nickname, user_score, pc_score):
    print(f"[{nickname}: {user_score} / PC: {pc_score}]")

print("╔╗ ╔╦═══╦╗  ╔╗  ╔═══╗")
time.sleep(0.2)
print("║║ ║║╔══╣║  ║║  ║╔═╗║")
time.sleep(0.2)
print("║╚═╝║╚══╣║  ║║  ║║ ║║")
time.sleep(0.2)
print("║╔═╗║╔══╣║ ╔╣║ ╔╣║ ║║")
time.sleep(0.2)
print("║║ ║║╚══╣╚═╝║╚═╝║╚═╝║")
time.sleep(0.2)
print("╚╝ ╚╩═══╩═══╩═══╩═══╝")
time.sleep(0.2)
print("Welcome to the Number Guessing Game!")

#nickname and explain the rules
print('Enter your nickname:')
nickname = input()
print("=" * 50)
print(f"Hello, {nickname}! Do you know how to play?")
answer = input("Y/N: ").lower()
if answer == 'y':
    print("Great! Let's start the game.")
elif answer == 'n':
    time.sleep(0.5)
    print("I'm thinking of a number between 1 and 50.")
    time.sleep(0.5)
    print("You need to guess the number in a limited number of attempts.")
    time.sleep(0.5)
    print("Difficulty level set your number of attempts. Easy mode sets you 10 attempts. Hard mode sets you 5 attempts.")

#difficulty selection
time.sleep(0.5)
print("=" * 50)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    max_attempts = 10
    os.system('cls' if os.name == 'nt' else 'clear')
elif difficulty == 'hard':
    max_attempts = 5
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Nah, there is no {difficulty} mode. Defaulting to 'easy' mode.")
    max_attempts = 10

print(f"You have {max_attempts} attempts to guess the number.")
time.sleep(0.5)
print("="*50)

#game loop
game = True
while game:
    #number of attempts and random number generation
    attempts = 0
    number_to_guess = random.randint(1, 50)

    #round loop
    while attempts < max_attempts:
        guess = input("Make a guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number_to_guess:
            print(random.choice(low_list))
        elif guess > number_to_guess:
            print(random.choice(high_list))
        else:
            print(f"Congratulations, {nickname}! You've guessed the number {number_to_guess} correctly in {attempts} attempts!")
            user_score += 1
            break
        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print(f"Sorry, {nickname}. You've used all your attempts. The number was {number_to_guess}. Better luck next time!")
            pc_score += 1

    display_score(nickname, user_score, pc_score)

    #ask to play again
    time.sleep(0.5)
    print("="*50)
    time.sleep(0.5)
    print("Game Over. Wanna play again? Type Y/N")
    play_again = input().lower()
    if play_again == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome back, {nickname}!")
        print(f"You have {max_attempts} attempts to guess the number.")
        print("="*50)
        #restart the round loop
        continue
    else:
        #exit the game loop
        game = False
        print("██████╗░██╗░░░██╗███████╗██╗")
        time.sleep(0.2)
        print("██╔══██╗╚██╗░██╔╝██╔════╝██║")
        time.sleep(0.2)
        print("██████╦╝░╚████╔╝░█████╗░░██║")
        time.sleep(0.2)
        print("██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝")
        time.sleep(0.2)
        print("██████╦╝░░░██║░░░███████╗██╗")
        time.sleep(0.2)
        print("╚═════╝░░░░╚═╝░░░╚══════╝╚═╝")