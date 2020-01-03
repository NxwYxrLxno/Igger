# This will import a library random word. The word will be chosen randomly, and
# based on the length of the word, that amount of dashes will be printed. You
# will have 10 guesses.
import random
words= ["cheese", "buns", "beak", "superman", "michael", "beans"]
secret_word=random.choice(words)
dash = "-" * len(secret_word)
number_of_guesses = 10

# This asks the user for a guess. Due to the len(guess) function, it will deter-
# mine whether or not your guess is one letter. I also used the .islower to
# tell you that it must be a lowercase letter. If it fits qualifications, it
# will return the letter.
def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print "Your guess mush be one character. Try again."
        elif not guess.islower():
            print "Guess must be lowercase letter. Try again."
        else:
            return guess

# This is the dashes function. for the length of the word in the library, it will
# print that number of dashes, so that you may guess appropriately. If the dash
# has a letter that is contained in a word, it will print that word and then re-
# turn the dash.
def update_dashes(library, dash, guess):
    for i in range(len(library)):
        if library[i] == guess:
            dash = dash[:i] + guess + dash[i + 1:]
    return dash

# This function is what keeps asking the user for guesses, until they run out
# or get the word correct.
while number_of_guesses > 0 and dash != secret_word:
    print dash
    print str(number_of_guesses) + " guesses left."

# This will determine the number of guesses you have. for each time you get it
# wrong, it will deduct a guess, leaving you with less guesses. If you get a
# letter right, it will not deduct, and let you keep guessing letters. If you
# get all the letters correct, you win.
    guess = get_guess()
    dash = update_dashes(secret_word, dash, guess)
    if guess in secret_word:
        print "Correct! This letter is in the word."
    else:
        print "This letter in not in the word. Guess again."
        number_of_guesses = number_of_guesses - 1

# This simply tells you whether you win or lose. If guesses are equal to 0, you
# lose. If guesses are more, and you guess the word, you win.
if number_of_guesses == 0:
    print "You lose! " + secret_word
else:
    print "You win! " + secret_word
