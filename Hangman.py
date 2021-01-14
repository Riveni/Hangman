import os

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
HANGMAN_PHOTOS = {
    0: """
        x-------x
        
        
        
        
        
        """, 1: """
        x-------x
        |
        |
        |
        |
        |
        """, 2: """
        x-------x
        |       |
        |       0
        |
        |
        |
        """, 3: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """, 4: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """, 5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """, 6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """}
MAX_TRIES = 6


def print_hangman(num_of_tries):
    """
    print hangman state according to user tries
    :param num_of_tries: int
    :return: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letters_guessed):
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


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    check if the user's guess was guessed before or not, if not guessed then the function
    adds it to the guessed letter list
    :param letter_guessed: type string
    :param old_letters_guessed: type list
    :return: false if letter was guessed, true otherwise
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


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


def check_guess(guess, secret_word):
    """
    check if user guess is correct or not
    :param guess: string
    :param secret_word: string
    :return: true if letter apear in secret word, false otherwise
    """
    if guess in secret_word:
        return True
    else:
        print(":(")
        return False


def choose_word(file_path, index):
    """
    selects a secret word for the user to guess in the game
    :param file_path: string
    :param index: int
    :return:secret word - string
    """
    words_list = []
    words_file = open(file_path, 'r')
    for line in words_file:
        for word in line.split():
            words_list.append(word)
    words_file.close()
    return words_list[index % len(words_list) - 1]


def initial_game():
    """
    print welcome screen and takes file path, index from user
    and select secret word from the file
    :return: file path and word index
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    while True:
        file_path = input("Enter secret words file path: ")
        try:
            index = int(input("Enter index: "))
            secret_word = choose_word(file_path, index)
            return secret_word
        except:
            print("Invalid input, try again")



def main():
    # Initial game
    secret_word = initial_game()
    old_letters_guessed = []
    num_of_tries = 0
    print_hangman(num_of_tries)

    # Game-play
    while num_of_tries < MAX_TRIES:  # Game runs until user uses all his guesses
        print(show_hidden_word(secret_word, old_letters_guessed), "\n")
        user_guess = input("Guess a letter:").lower()
        if try_update_letter_guessed(user_guess, old_letters_guessed):  # check if user guess is valid
            if check_guess(user_guess, secret_word):  # check if user guess is correct
                if check_win(secret_word, old_letters_guessed):  # check if user won
                    print(show_hidden_word(secret_word, old_letters_guessed), "\n")
                    print("WIN")
                    break  # if user won the game ends
            else:
                # os.system('cls')
                num_of_tries += 1
                print_hangman(num_of_tries)
                if num_of_tries == MAX_TRIES:
                    print(show_hidden_word(secret_word, old_letters_guessed), "\n")
                    print("LOSE")


if __name__ == "__main__":
    main()
