# Part 2.1
HANGMAN_ASCII_ART = """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")

# Part 2.2 + 4
user_guess = input("Guess a letter:").lower()
# check input validity:
if len(user_guess) != 1:  # more then 1 letter
    if user_guess.isalpha():
        print("E1")
    else:
        print("E3")
elif not user_guess.isalpha():  # special char
    print("E2")
else:
    print(user_guess)

# Part 3
secret_word = input("Please enter a word: ")
print("_ " * len(secret_word))

