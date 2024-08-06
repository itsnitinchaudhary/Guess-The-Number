import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        
        guess = input("Enter your guess: ")
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            continue
        
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
        
        
        
        
        
        
        
