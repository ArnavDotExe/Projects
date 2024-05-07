import random 
from names import people 
import pandas as pd


# The function higher_lower() is defined to play the Higher Lower game.
def higher_lower():
    print("Welcome to Higher Lower!")
    score = 0
    while True:
        person1 = random.choice(list(people.keys()))
        person2 = random.choice(list(people.keys()))
        while person1 == person2:
            person2 = random.choice(list(people.keys()))
        print(f"Who has more Instagram followers? {person1} or {person2}?")
        guess = input("Type 'A' for the first person, 'B' for the second person or 'Q' to quit: ")
        if guess.lower() == 'q':
            print(f"Your final score was {score}")
            break
        elif people[person1] > people[person2] and guess.lower() == 'a':
            score += 1
            print(f"Correct! Your score is {score}")
        elif people[person1] < people[person2] and guess.lower() == 'b':
            score += 1
            print(f"Correct! Your score is {score}")
        else:
            print(f"Wrong! Your final score was {score}")
            break
        
higher_lower()