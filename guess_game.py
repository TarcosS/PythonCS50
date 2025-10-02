import random

def selected_number():
    # Randomly select a number between 1 and 100
    return random.randint(1, 100)

def get_guess():
    # Prompt the user for a guess and ensure it's an integer
    while True:
        try:
            # Make sure to convert input to an integer
            guess = int(input("What is your guess? "))
            return guess
        # Handle the case where conversion to int fails
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
def main():
    # Define number before the loop to avoid re-selection
    number = selected_number()
    while True:
        guess = get_guess()
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            return # Exit from loop and end program

main()