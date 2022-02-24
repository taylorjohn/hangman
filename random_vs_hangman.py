#imports
import random
from hangman_words import word_list
from hangman_letters import letter_list
from hangman_art import logo, stages
import os
# start


#display logo
print(logo)
# print a list of choice for different games
print("Select the game type by typing number")
print("1. Normal hangman")
print("2. Player vs Computer Random Choice")
print("3. Player vs Computer Letter Frequence")
print("4. Player vs. Computer Word Length")
print("5. Player vs All Computer")


game_type = input("Type your game choice #: ")
# pick random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
'''
#1 - hangman
if game_type == '1':
    guess = input("Guess a letter: ").lower()
    word_length = len(chosen_word)

#2 - random
elif game_type == '2':
    guess = random.choice(letter_list).lower()
    word_length = len(chosen_word)
'''
# create a list
# word_list = ["window", "door", "table", "bed", "roof", "garage", "Carpet"]

# pick random word from the word list
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

#test chosen word
print(f"The chosen Game type is {game_type}.")
print(f"For testing purposes the chosen word is {chosen_word}.")
# see word length generate list of blanks underscores "_", "_", "_"
display = []
for _ in range(word_length):
    display += "_"
# print(display)


# while not true keeps game running until won or lost game!
game_over = False
random_game_over = False

# number of guess you have before you lose
lives = 6

while not game_over:
    # ask for input letter for a guess make all lowercase

    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    # loop through letter guessed is  == letter on word
    for position in range(word_length):
        letter = chosen_word[position]

        print(f"Current position: {position} \n Current Letter: {letter} \n Guessed Letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            random_game_over = False
            print("You Lose!!")


    print(f"{' '.join(display)}")
                # print("Correct!")
            #else:
            #print("Incorrect!")

    # if all blanks filled game over print you won!!
    if "_" not in display:
        game_over = True
        random_game_over = False
        print(f"You Win!! {lives} with lives left!")

    # if not all blanks they lose a life
    print(stages[lives])

#test chosen word
print(f"For testing purposes the chosen word is {chosen_word}.")
# see word length generate list of blanks underscores "_", "_", "_"
display = []
for _ in range(word_length):
    display += "_"
# print(display)




# number of guess you have before you lose
lives = 6

while not random_game_over:
    # ask for input letter for a guess make all lowercase

    guess = random.choice(letter_list).lower()
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    # loop through letter guessed is  == letter on word
    for position in range(word_length):
        letter = chosen_word[position]

        print(f"Current position: {position} \n Current Letter: {letter} \n Guessed Letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            random_game_over = True
            print("Computer Lose!!")


    print(f"{' '.join(display)}")
                # print("Correct!")
            #else:
            #print("Incorrect!")

    # if all blanks filled game over print you won!!
    if "_" not in display:
        random_game_over = True
        print(f"Computer Win!! {lives} with lives left!")

    # if not all blanks they lose a life
    print(stages[lives])
