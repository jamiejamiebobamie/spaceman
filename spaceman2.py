import random

guesses = 0
guessed_letters = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def load_word():
    words = ["car", "bike", "eagle", "fish", "secret", "computer", "desk", "chair", "light", "kite", "button", "bear", "descent", "sun", "moon", "otter", "picture"]
    secret_word = random.choice(words)
    return secret_word

secret_word = load_word()

def updateLetters():
    shown_letters = list(secret_word)
    hidden_letters = list("_"* len(shown_letters))
    for i, item in enumerate(shown_letters):
        for letters in guessed_letters:
            if shown_letters[i] == letters:
                hidden_letters[i] = letters
    return (hidden_letters, shown_letters)


def displayWordFromArray(x):
    stringShown = ""
    for chars in x:
        stringShown += (str(chars + " "))
    return stringShown

def displayLettersGuessedFromArray(x):
    stringShown = ""
    for chars in x:
        stringShown += (str(chars + ", "))
    return stringShown

def drawMan(x):
    if x == 1:
        return "  ^"
    elif x == 2:
        return ("  ^\n"
                "  ||")
    elif x == 3:
        return ("  ^\n"
                "  ||\n"
        "   @  - Goodbye, says the spaceman!")
    elif x == 4:
        return ("  ^\n"
                "  ||\n"
        "   @  - Goodbye, says the spaceman!\n"
        "  ||")
    elif x == 5:
        return ("  ^\n"
                "  ||\n"
        "   @  - Goodbye, says the spaceman!\n"
        "  ||\n"
        "  || - T-MINUS 3!")
    elif x == 6:
        return ("  ^\n"
                "  ||\n"
        "   @  - Goodbye, says the spaceman!\n"
        "  ||\n"
        "  || - T-MINUS 3!\n"
        "  vv - 2!")
    elif x == 7:
        return ("  ^\n"
                "  ||\n"
        "   @  - Goodbye, says the spaceman!\n"
        "  ||\n"
        "  || - T-MINUS 3!\n"
        "  vv - 2!\n"
        "  XX - 1!")
    elif x == 8:
            return ("  ^\n"
                    "  ||\n"
            "   @  - Goodbye, says the spaceman!\n"
            "  ||\n"
            "  || - T-MINUS 3!\n"
            "  vv - 2!\n"
            "  XX - 1! \n"
            " XXXX -BLAST OFF!!")



show = updateLetters()
while guesses < 8:
    if "_" not in show[0]:
        print("\nWORD: " + displayWordFromArray(show[1]))
        print("\nYou won!\n")
        break
    else:
        print("\nGuessed letters: " + displayLettersGuessedFromArray(guessed_letters))
        print("\nWORD: " + displayWordFromArray(show[0]))
        if (8 - guesses) > 1:
            print("\nYou have " + str((8 - guesses))+ " guesses.\n")
        else:
            print("\nYou have " + str((8 - guesses))+ " guess.\n")
        if guesses != 0:
            print(drawMan(guesses))
        x = input("\n\nPlease enter a letter. \n\n")
        x = str.lower(x)
        if x in alphabet and len(x) == 1 and x not in guessed_letters:
            guessed_letters.append(x)
            show = updateLetters()
            if x not in show[0]:
                guesses += 1
        elif x in guessed_letters:
            print("\n\nPlease guess a letter you haven't guessed already.")
        elif len(x) > 1:
            print("\n\nPlease guess just one letter.")
        elif x not in alphabet:
            print("\n\nPlease guess a letter.")
        else:
            print("\n\nI have no idea what you typed, but it was wrong. Try entering a letter.")
else:
    print(drawMan(guesses))
    print("\nWORD: " + displayWordFromArray(show[1]))
    print("\nYou Lost\n")
