import random as codeMaker
import sys as killSwitch

#Generate 4 unique numbers between 1 and 9
numbers = codeMaker.sample(range(1, 10), 4)

print(numbers)

correct1 = 0
correct2 = 0
correct3 = 0
correct4 = 0

guessCount = 0

guess = ""

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
    global guess1, guess2, guess3, guess4, guess
    print("Welcome to Mastermind!")
    while guess is not int:
        guess = input("Enter your guess for the code (four digits, must be any number from 1-9): ")
        if guess == "help":
            print(
                "In Mastermind, you must guess a four digit code "
                "that is randomly generated before each game.\n"
                "The original Mastermind board game used 9 colours "
                "but we are using the numbers 1-9 to make things easier.\n"
                "In the four digit code, all numbers are unique. "
                "One example of a guess you can make is 6381."
            )
        elif guess == "quit":
            killSwitch.exit("Thank you for playing Mastermind. Have a great day!")
        else:
            guess1 = int(guess[findGuess1])
            guess2 = int(guess[findGuess2])
            guess3 = int(guess[findGuess3])
            guess4 = int(guess[findGuess4])
            break
        
    print(guess1, guess2, guess3, guess4)


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

while guessCount < 3:
    getGuess()
    checkGuess()
    guessResults()
    if correct1 == correct2 == correct3 == correct4 == 1:
        break
    else:
        guessCount += 1

if correct1 == correct2 == correct3 == correct4 == 1:
    print("Correct! You win!")
else:
    print("You didn't win. Try again!")