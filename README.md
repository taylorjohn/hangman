# The largest heading
## The second largest heading
###### The smallest heading

**This is bold text**

*This text is italicized*

~~This was mistaken text~~

**This text is _extremely_ important**

***All this text is important***

[GitHub Pages](https://pages.github.com/)





# HANGMAN GAME FROM 100 DAYS OF CODE

My goal is to complete it, then add additional features like a computer player, menu, scores and etc.

- [x] Hangman 
- [x] Hangman vs Random Computer Choice
- [ ] Hangman vs Frequency Computer Choice
- [ ] Hangman vs Word Length Frequency Computer Choice
- [ ] Hangman vs All Computer Choices

## Hangman

**Hangman -** The regular game as in the challenge

Here is my pthon file [Hangman](https://github.com/taylorjohn/hangman/blob/main/hangman.py)

1.   A real player chooses letters and play
2.  computer picks random letters and plays (horrible odds)

# Additional improvements beyong regular hangman 

1. **Menu**
   - Select Game type
     - Play selected game

2. **Computer Player**

  - **Computer Random Letter Choices**
    - picks letter at random should have horrible odds of getting words
      -  Compare Players score to the random Computer choices
  
  - **Computer picks letter based on generic frequency**
    - (ok odds of winning) but based on all words not a specific word length
      -  Compare Players score to the random Computer choices

  - **Computer pick letters base on frequency of the length of the word**
    -  I assume this will improve its odds
        -  Compare Players score to the random Computer choices

  - **compares scores you playing not only against the hangman but the computer a few ways.**

1. scores
  a.  your score - win - 2 life left - 2nd place
  b.  random - lose - 0 life left - 4th place
  c.  frequency - win - 1 life left - 3rd place
  d.  adv frequency - win 3 life left - 1st place

2. print number of lifes and make it score
  add number life’s left f print


3.  clear screen each time so no long scroll
- [x]  Working - clear screen each time so no long vertical scroll whikle playing

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


Finally the computer guessing via the top frequency of letters based on word length.

Grab first word get length 
Save the count of letters into a file of word size

Example input
word_list = [“roof”, “window”, “carpet”, “table”, “wall”, “garage”]



Output takes input and gets letter add if doesn’t exit

If letter exist increase amount by 1

four_letters =[“r = 1”, “o= 2”, “f = 1”, “w = 1”, “a = 1”, “l= 2”]
five_letters =[“t = 1”, “a = 1”, “b = 1”, “l = 1”, “e = 1”]
six_letters =[”i = 1”, ”n = 1”, ”d= 1”, ”o = 1”, ”w = 2”, ”c = 1”, ”p = 1”, ”t = 1”, ”r = 2”, ”a = 3”, ”g = 2”, ”e =2”]

Then sort highest value and put keyword as input.


