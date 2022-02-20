# hangman
hangman vs computer

Hangman

1.   A real player chooses letters and play
2.  computer picks random letters and plays (horrible odds)

# Additional improvements beyong regular hangman 

3.  computer picks letter based on generic frequency (ok odds of winning) but based on all words not a specific word length
4. computer pick letters base on frequency of the length of the word I assume this will improve its odds

# compares scores you playing not only against the hangman but the computer a few ways.

1. scores
  a.  your score - win - 2 life left - 2nd place
  b.  random - lose - 0 life left - 4th place
  c.  frequency - win - 1 life left - 3rd place
  d.  adv frequency - win 3 life left - 1st place

2. print number of lifes and make it score
  add number life’s left f print


3.  clear screen each time so no long scroll

4. create list of chosen letters
  a.  alphabet list for Random  .py file to import
  b.  frequency list generic frequency  .py file to import
  c.  generate new frequency based on word length
      Iterate throughly word list get first index save length and letter count for each letter which when reach n it will have the word frequency y word length


PseudoCode

0. Get imports needed
1. Start

2. Pick random word from list of words

3. Get length of word print matching amount of length with _ _ _ _ blanks to represent letters in word


# 1 Player choices a letter - input a letter

# 2 Random import list of alphabet and does a
random grab

# 3 Frequency imports a list in higher frequency letters first and grabs a letter in order of highest odds

#4 Advanced frequency picks letter based on the length of the word chosen it picks the best odds for that length of chosen word.

# game loop keeps players game in loop til win or lose
# while game_over not True:

# Check if chosen letter is in position 1 to position n of word length

# If matches current letter choice == with current position print letter in blank space _ o o _

# keep track of life’s Set life = 6

# If not match minus a life

# win - If no blanks left print you win and amount of life’s left

# keep going - If blanks left repeat until no blanks or no life’s left

# lose - run out of life If lifes = 0 print you lose


