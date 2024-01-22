"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Skřivánek
email: ddaniel.skrivanek@seznam.cz
discord: vetrex89cz #3080
"""
import random
import time

def generate_secret_number():
    """Generuje tajné 4místné číslo s unikátními číslicemi."""
    digits = list(range(1, 10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def evaluate_guess(secret_number, user_guess):
    """Vyhodnotí tip uživatele a vrátí počet bull/cows."""
    bulls, cows = 0, 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            bulls += 1
        elif user_guess[i] in secret_number:
            cows += 1
    return bulls, cows

def print_result(guesses, elapsed_time):
    """Vypíše text na základě počtu odhadů"""
    if guesses == 1:
        print("That's amazing!")
    elif guesses <= 3:
        print("That's great!")
    elif guesses <= 6:
        print("That's good.")
    else:
        print("Not so good.")
    
    plural_guesses = "guess" if guesses == 1 else "guesses"
    
    print(f"Correct, you've guessed the right number in {guesses} {plural_guesses}!")
    print(f"It took you {elapsed_time:.2f} seconds.")

def main():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    total_guesses = []

    while True:
        secret_number = generate_secret_number()
        guesses = 0
        start_time = time.time()

        while True:
            user_input = input("Enter a number: ")

            if not user_input.isdigit() or len(user_input) != 4 or  \
                len(set(user_input)) != 4 or user_input[0] == "0":
            
                print(
                    "Invalid input. Please enter a valid 4-digit number."
                )
                print("-" * 47)
                continue

            guesses += 1
            bulls, cows = evaluate_guess(secret_number, user_input)

            plural_bulls = "bull" if bulls == 1 else "bulls"
            plural_cows = "cow" if cows == 1 else "cows"
        
            print(f"{bulls} {plural_bulls}, {cows} {plural_cows}")
            print("-" * 47)
        
            if bulls == 4:
                end_time = time.time()
                elapsed_time = end_time - start_time
                total_guesses.append(guesses)
                print_result(guesses, elapsed_time)
                print("Game is over!")
                quit()
            
if __name__ == "__main__":
    main()            