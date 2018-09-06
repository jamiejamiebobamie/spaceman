import random

guesses = 0
guessed_letters = []

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


#show is a tuple with first element being the hidden_letters and the second element being the shown_letters
show = updateLetters()
while guesses < 8:
    if "_" not in show[0]:
        print(show[1])
        print("You won!")
        break
    else:
        print(guessed_letters)
        print(show[0])
        print(guesses)
        x = input("Please enter a letter.")
        if type(x) is str and len(x) == 1 and x not in guessed_letters:
            guessed_letters.append(x)
            show = updateLetters()
            if x not in show[0]:
                guesses += 1
else:
    print("You Lost")
