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


def game_state():
    state1 = """
        x-------x
    """
    state2 = """
        x-------x
        |
        |
        |
        |
        |
    """
    state3 = """
        x-------x
        |       |
        |       0
        |
        |
        |
    """
    state4 = """
        x-------x
        |       |
        |       0
        |       |
        |
        |
    """
    state5 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """
    state6 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """
    state7 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
    # print(state1, state2, state3, state4, state5, state6, state7, sep="\n")

# Part 2.2 + 4 + 5
def is_valid_input(letter_guessed):
    """
    function check the validity of the user input
    if use input is longer than 1 char or is not a-z letter, return false
    else return true
    """
    if (len(letter_guessed) != 1) or (not letter_guessed.isalpha()):
        return False
    else:
        return True


# Part 3
"""
secret_word = input("Please enter a word: ")
print("_ " * len(secret_word))
"""


# Part 5
def main():
    print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    letter_guessed = input("Guess a letter:").lower()
    print(is_valid_input(letter_guessed))
    return


if __name__ == "__main__":
    main()
