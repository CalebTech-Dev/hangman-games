# HANGMAN GAME INITIAL VERSION

import random
 
# Creating a greeting program
print('welcome to Caleb Tech-Dev')
# Create wordlist
words = ['Pentester', 'analyst', 'Hacker']
# Randomly chose a word from the wordlist 
secret_word = random.choice(words).lower()
# Ask useer to guese a letter
guess = input('guess a letter.... ').lower()
print(guess)
# make the program take an input from the user and turn it to lowercase
for letter in secret_word:
    if letter == guess:
        print('you are right')
    else:
        print('your are wrong')
# Check if the letter is in the word