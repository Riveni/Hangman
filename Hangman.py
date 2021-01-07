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


# Part 2.2 + 4 + 5 + 6
def is_valid_input(letter_guessed, old_letters_guessed):
    """
    check the validity of the user input
    :param letter_guessed: type string
    :param old_letters_guessed: type list
    :return: if use input is longer than 1 char or is not a-z letter, return false
    else return true
    """
    if (len(letter_guessed) != 1) or (not letter_guessed.isalpha()) or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


# part 6
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    check if the user's guess was guessed before or not, if not guessed then the function
    adds it to the guessed letter list
    :param letter_guessed: type string
    :param old_letters_guessed: type list
    :return: false if letter was guessed, true otherwise
    """
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


# Part 3
"""
secret_word = input("Please enter a word: ")
print("_ " * len(secret_word))
"""


# Part 5
def main():
    # print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    old_letters_guessed = ['a', 'p', 'c', 'f']
    letter_guessed = input("Guess a letter:").lower()
    # print(is_valid_input(letter_guessed, old_letters_guessed))
    print(try_update_letter_guessed(letter_guessed, old_letters_guessed))
    return


if __name__ == "__main__":
    main()
