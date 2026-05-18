# ===========================================================
# PROJECT 1: Mad Libs Generator
# CONCEPTS: variable, input(), print(), f-strings, .upper()
# ===========================================================
# A Mad Lib is a story wherre YOU fill in the blanks. 
# The program asks the words, then drops them into a story.
# ===========================================================

# --- STEP 1: Greet the user ---
# print() just displays text on the screen
print("=" * 40)
print(" Welcome to Python Mad Libs!")
print("=" * 40)
print("Answer the questions below.")
print("Then watch your story come to life!\n")

# ---- STEP 2: Collect words from the users ---
# input() pauses the program and waits for the user to type something
# Whatever they type gets stored in a variable (the word on the left)

name        = input("Enter a person's name: ")
place       =  input("Enter a place (city, planet, jungle...): ")
animal      = input("Enter an animal: ")
adjective1  = input("Enter an adjective (describing word): ")
adjective2  = input("Enter another adjective: ")
verb_past   = input("Enter a verb in past tense (ran, ate, flew...): ")
number      = input("Enter a number: ")
food        = input("Enter a food: ")

# --- STEP 3: Build the story ---
# f-strings let you plug variables directly into text
# Just wrap the variable name in curly braces inside the string: {variable}
# .upper() make the name ALL CAPS for dramatic effect

story = f"""
\n{'=' * 40}
    YOUR MAD LIB STORY
{'=' * 40}

One {adjective1} morning, {name.upper()} woke up in {place}
and immediately spotted a {adjective2} {animal} sitting on 
the kitchen table, eating all the {food}.

"{name} let out a scream and {verb_past} away so fast that they 
ran {number} miles without stopping.

Scientists later confirmed it was the most {adjective1}
encounter with a {animal} ever recorded in {place}.

The {animal} was never seen again. The {food} was gone forever.

THE END.
{'=' * 40}
"""

# --- STEP 4: Display the story ---
print(story)

