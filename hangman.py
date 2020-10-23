import random
wordList = []
correctGuesses = []
wrongGuesses = []
wrong = 0
hidden = ""

def updateDisplay(key):
    hidden = ""
    for i in key:
        if i in correctGuesses:
            hidden += i
        elif i == " ":
            hidden+=""
        elif i.isalpha():
            hidden += "_"       
    return "\n"+hidden

with open('words.txt', 'r') as rf:
    for line in rf:
        if len(line) > 6:
            wordList.append(line)
randomIndex = random.randint(0, len(wordList)-1)
key = wordList[randomIndex]
key = key.upper()
hidden = updateDisplay(key)

while wrong < 10 and "_" in hidden:
    print(hidden)
    guess = input("\nGuess a letter (case-insensitive): ")
    guess = guess.upper()
    if guess.isalpha() and len(guess) == 1:
        if guess in key:
            if guess in correctGuesses:
                print("\nYou've guessed that correctly already.")
            else:
                correctGuesses.append(guess)
                hidden = updateDisplay(key)
                print("\nCorrect!")
        else:
            if guess in wrongGuesses:
                print("\nYou've guessed that incorrectly already.")
            else:
                wrong += 1
                wrongGuesses.append(guess)
                print("\nIncorrect. You have %d incorrect guess(es) remaining."%(10-wrong))
    else:
        print("\nYou must guess 1 letter per turn.")
if wrong == 10:
    print("\nGame Over. The word was: %s"%key)
else:
    print(hidden)
    print("\nCongratulations, you win!")



