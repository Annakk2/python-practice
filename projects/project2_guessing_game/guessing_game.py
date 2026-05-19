# ====================================================================
# PROJECT 2: Number Guessin Game
# CONCEPTS: import, random, while loops, if/elif/else,
#           int(), comparisons, tracking attempts
# ====================================================================
# The computer picks a secret number between 1 and 100.
# You kwwp guessing until find it. 
# The program tells you if you're too high, too low, or correct.
# ====================================================================

# --- STEP 1: Import the random module ---
# Python has built-in tools called modules. 
# 'random' lets us generate random numbers.
# We have to import it before we can use it. 
import random 

# --- STEP 2: Set up the game ---
# random.randint(1, 100) picks a random whole number between 1 and 100
# We store it in secret_number - the player never sees this directly
secret_number = random.randint(1, 100)

# This variable tracks how many guesses the player has made
attempts = 0

# This controls our game loop - as long as it's True, the game contionues
playing = True

# --- STEP 3: Welcome the player ---
print("=" * 40)
print(" Welcome to the Guessing Game!")
print("=" * 40)
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it?\n")

# --- STEP 4: The game loop ----
# 'while True' means: keep repeating this block FOREVER
# until we explicitly tell to stop with 'break'
while playing:
    
    # Ask the player for a guess
    # input() always returns a STRING, so we wrap it int()
    # to convert it to a number we can compare mathematically
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
 

    # Every time the player guesses, add 1 to attempts
    attempts += 1 # this is shorthand for: attempts = attempts + 1
    
    if attempts >= 10 and guess != secret_number:
        print(f"Out of guesses! The number was {secret_number}.") 
        playing = False
        continue
    

    # --- STEP 5: Check the guess --- 
    # if/elif/else lets the program make decisions
    # if checks conditions top to bottom and runs the first true one

    if guess < secret_number:
        print("Too low! Try higher.\n")

    elif guess > secret_number:
        print("Too high! Try lower.\n")

    else:
        # If it's not lower and not higher, it must be correct
        print(f"\n{'=' * 40}")
        print(f" YOU GOT IT! The number was {secret_number}. ")
        print(f" It took you {attempts} guess(es).")
        
       
        another_round = input("Would you like to play again? (yes/no):  ")
        if another_round.lower() == "yes":
            secret_number = random.randint(1,100)
            attempts = 0
            print("\n0k! I'm thinking of a new number. \n")
        else:
            playing = False

    

        # Give the player a rating based on how many attempts they used
        if attempts <= 5:
            print(" Incredible - you're a natural!")
        elif attempts <= 10:
            print(" Nice work. Solid guessing.")
        else:
            print(" You got there eventually. Keep practicing!")

        print(f"{"=" * 40}\n")

        # Stop the loop - the game is over
        playing = False

# --- STEP 6: Sign off ---
print("Thanks for playing. Run the file again for a new member!")





   