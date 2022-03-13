def print_welcome():
    """
    print hangman screen
    :return: None
    """
    # print the hangman start screen
    HANGMAN_ASCII_ART = """      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART)


def choose_word(file_path, index):
    """
    This function get file, the index want to check, and return tuple with words num is not dup
    and the word we check
    :param file_path: file loction
    :type: str
    :param index: index user want from file
    :type: int
    :return: the word
    :rtype: str
    """
    with open(file_path, "r") as txt_file:
        lines_list = txt_file.read().split() #creat list of lines in txt file
        for x in range(0, index): #loop of indexes
            currect_word = lines_list[x % len(lines_list)]
    return (currect_word)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function show the hidden word with delel the word is not in the old letter list
    :param secret_word: the string of the user
    :type: str
    :param old_letters_guessed: the list of the user
    :type: list
    :return: the string with _ in the letter is not in the list
    :rtype: str
    """
    string = ""
    for check_loction in secret_word:
        string += " "
        if check_loction in old_letters_guessed:
            string += check_loction
        else:
            string += "_"
    return string.strip()


def print_hangman(num_of_tries):
    """
    This function print hangman frame like the tries
    :param num_of_tries: the frame we need print
    :return: None
    """
    HANGMAN_PHOTOS = { 1: """
    x-------x""",

    2 : """
:(  
    x-------x
    |
    |
    |
    |
    | """,

    3 : """
:(  
    x-------x
    |       |
    |       0
    |
    |
    | """,

    4 : """  
:(  
    x-------x
    |       |
    |       0
    |       |
    |
    | """,

    5 : """
:(  
    x-------x
    |       |
    |       0
    |      /|\\
    |
    | """,

    6 : """
:(  
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    | """,

    7 : """
:(  
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}
    print(HANGMAN_PHOTOS[num_of_tries])
    return None


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function get a string and return if it is more then 1 letter or it is not letter(False)
    :param letter_guessed: is the string
    :type letter_guessed: str
    :return: if the string pass the test
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    return ((len(letter_guessed) == 1) and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function get a string and return if it is more then 1 letter or it is not letter(False)
    :param letter_guessed: is the string
    :type letter_guessed: str
    :return: if the string pass the test
    :rtype: bool
    """
    # checking if we have invalid input
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        input_answer = True
        old_letters_guessed.append(letter_guessed.lower())
    else:
        print("X")
        list_small_to_big_letter = " -> ".join(sorted(old_letters_guessed))
        print(list_small_to_big_letter)
        input_answer = False
    return input_answer


def check_win(secret_word, old_letters_guessed):
    """
    This function check if the gess of the user is right
    :param secret_word: the secret string
    :type: str
    :param old_letters_guessed: the gusses of the user
    :type: list
    :return: if the user win
    :rtype: bool
    """
    answer = True
    if "_" in show_hidden_word(secret_word, old_letters_guessed): #if the word is clear and not have empty loctions
        answer = False
    return answer


def main():
    """
    This function is the manage
    :return: None
    """
    MAX_TRIES = 6
    old_letters_guessed = []
    num_of_tries = 1

    #print welcome and how much tries
    print_welcome()
    print(MAX_TRIES)

    #get word from user
    user_path = input("Please enter file path: ")
    user_index = int(input("Please enter the index: "))
    secret_word = choose_word(user_path, user_index)

    #starting game
    print("\nLet's start!")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    #game main loop
    while(num_of_tries <= MAX_TRIES and not check_win(secret_word, old_letters_guessed)):
        user_letter_guess = input("Guess a letter: ") #input letter
        if check_valid_input(user_letter_guess, old_letters_guessed) == False: #if the letter is valid, stop
            try_update_letter_guessed(user_letter_guess, old_letters_guessed)

        else: #letter is not valid, keep moving
            old_letters_guessed += user_letter_guess #add letter to list
            if user_letter_guess in secret_word: #currect letter
                print(show_hidden_word(secret_word, old_letters_guessed))
            else: #wrong letter
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
    #checking win
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")

    return None

if __name__ == '__main__':
    main()
