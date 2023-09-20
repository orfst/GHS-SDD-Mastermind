import random as ran

#Generate 4 unique numbers between 1 and 9
numbers = ran.sample(range(1, 10), 4)

print(numbers)

correct1 = 0
correct2 = 0
correct3 = 0
correct4 = 0

findAnswer1 = findGuess1 = 0
findAnswer2 = findGuess2 = 1
findAnswer3 = findGuess3 = 2
findAnswer4 = findGuess4 = 3

answer1 = numbers[findAnswer1]
answer2 = numbers[findAnswer2]
answer3 = numbers[findAnswer3]
answer4 = numbers[findAnswer4]
print(answer1, answer2, answer3, answer4)
def getGuess():
    global guess1, guess2, guess3, guess4
    guess = input("Enter your guess for the code (four digits, must be any number from 1-9): ")
    guess1 = int(guess[findGuess1])
    guess2 = int(guess[findGuess2])
    guess3 = int(guess[findGuess3])
    guess4 = int(guess[findGuess4])
    print(guess1, guess2, guess3, guess4)
getGuess()

def checkGuess():
    global correct1, correct2, correct3, correct4
    if guess1 == answer1:
        correct1 = 1
    elif guess1 in (answer2, answer3, answer4):
        correct1 = 2
    else:
        correct1 = 3

    if guess2 == answer2:
        correct2 = 1
    elif guess2 in (answer1, answer3, answer4):
        correct2 = 2
    else:
        correct2 = 3
    
    if guess3 == answer3:
        correct3 = 1
    elif guess3 in (answer1, answer2, answer4):
        correct3 = 2
    else:
        correct3 = 3
    
    if guess4 == answer4:
        correct4 = 1
    elif guess4 in (answer1, answer2, answer3):
        correct4 = 2
    else:
        correct4 = 3
    
checkGuess()

def guessResults():
    if correct1 == 1:
        print("The first number you guessed is correct.")
    elif correct1 == 2:
        print("The first number you guessed is in the wrong spot.")
    else:
        print("The first number you guessed is not in the code.")

    if correct2 == 1:
        print("The second number you guessed is correct.")
    elif correct2 == 2:
        print("The second number you guessed is in the wrong spot.")
    else:
        print("The second number you guessed is not in the code.")

    if correct3 == 1:
        print("The third number you guessed is correct.")
    elif correct3 == 2:
        print("The third number you guessed is in the wrong spot.")
    else:
        print("The third number you guessed is not in the code.")

    if correct4 == 1:
        print("The fourth number you guessed is correct.")
    elif correct4 == 2:
        print("The fourth number you guessed is in the wrong spot.")
    else:
        print("The fourth number you guessed is not in the code.")

guessResults()

if correct1 == correct2 == correct3 == correct4 == 1:
    print("Correct! You win!")
else:
    print("blub blub vandal :D")