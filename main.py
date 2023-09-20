import random as ran

#Generate 4 unique numbers between 1 and 9
numbers = ran.sample(range(1, 10), 4)

print(numbers)

correct1 = True
correct2 = True
correct3 = True
correct4 = True

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
    if guess1 == answer1:
        correct1 = True
    elif guess1 in (answer2, answer3, answer4):
        correct1 = 1
    else:
        correct1 = False

    if guess2 == answer2:
        correct2 = True
    elif guess1 in (answer1, answer3, answer4):
        correct2 = 1
    else:
        correct2 = False

    if guess3 == answer3:
        correct3 = True
    elif guess3 in (answer1, answer2, answer4):
        correct3 = 1
    else:
        correct3 = False

    if guess4 == answer4:
        correct4 = True
    elif guess4 in (answer1, answer2, answer3):
        correct3 = 1
    else:
        correct4 = False
    print(correct1, correct2, correct3, correct4)
checkGuess()

if correct1 and correct2 and correct3 and correct4:
    print("Correct! You win!")
elif correct1 or correct2 or correct3 or correct4:
    print("At least one of these numbers is correct.")
else:
    print("None of these numbers are correct.")