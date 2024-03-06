import random 
from hangman_art import logo, stages
from hangman_words import word_list

from hangman_art import logo
print(logo)

chosen_word = random.choice(word_list)
lives = 6
#testing code 
print(f"The chosen word is {chosen_word}")

name = input("Welcome to the Hangman game! What is your name? \n")
print(f"Hello {name}! Let's play Hangman!")



display= []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"


end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
#check guessed letter
    for postion in range(word_length):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The solution is {chosen_word}.")
           
    print(stages[lives]) 
            
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print ("you win !! ")
        print(stages[lives]) 
       
 