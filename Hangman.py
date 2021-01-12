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

# part 8
HANGMAN_PHOTOS = {
        0: """
        x-------x
        
        
        
        
        """, 1: """
        x-------x
        |
        |
        |
        |
        |""", 2: """
        x-------x
        |       |
        |       0
        |
        |
        |""", 3: """
        x-------x
        |       |
        |       0
        |       |
        |
        |""", 4: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""", 5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""", 6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


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


# part 7
def show_hidden_word(secret_word, old_letters_guessed):
    """
    show user his game status, letters he guessed correctly and number
    of remaining letters to guess.
    :param secret_word: string
    :param old_letters_guessed: list
    :return: string of partly the secret word
    """
    secret = list(secret_word)
    i = 0
    for letter in secret:
        if not (letter in old_letters_guessed):
            secret[i] = "_"
        i += 1
    return " ".join(secret)


def check_win(secret_word, old_letters_guessed):
    """
    checks if user won the game by checking if all
    letters in the secret word are guessed
    :param secret_word: string
    :param old_letters_guessed: list
    :return: if won return True else False
    """
    for letter in secret_word:
        if not (letter in old_letters_guessed):
            return False
    return True


# Part 3
"""
secret_word = input("Please enter a word: ")
print("_ " * len(secret_word))
"""


# Part 5
def main():
    # print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    # old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    # letter_guessed = input("Guess a letter:").lower()
    # print(is_valid_input(letter_guessed, old_letters_guessed))
    # print(try_update_letter_guessed(letter_guessed, old_letters_guessed))
    # secret_word = "mammals"
    # print(show_hidden_word(secret_word, old_letters_guessed))

    # secret_word = "yes"
    # old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    # print(check_win(secret_word, old_letters_guessed))
    print_hangman(0)
    print_hangman(1)
    print_hangman(2)
    print_hangman(3)
    print_hangman(4)
    print_hangman(5)
    print_hangman(6)
    return


if __name__ == "__main__":
    main()
