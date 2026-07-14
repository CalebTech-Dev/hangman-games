import random

print('Welcome')
words = ['caleb', 'nguper', 'saakum']

secret_word = random.choice(words)
# loop the display word
display_word = []

for letter in secret_word:
    display_word += "_"
print(display_word)

guess = input('guess a letter to play... ').lower()
print(guess)

for position in range(len(secret_word)) :
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
    else:
        print('wrong')
print(display_word)