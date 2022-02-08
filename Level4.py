from random import randint

gameType = input(
    "Enter 1 if toy would like to guess, Enter 2 for computer to guess")
if gameType == "1":
    computer = randint(1, 10)
    print(computer)

    guesses = 3

    if guesses == 0:
        print("the number was", computer)

    while guesses > 0:
        player = int(input("Guess a number between 1 and 10: "))

        if computer == player:
            print("You guessed it!!", computer)
            break
        elif player > computer:
            guesses -= 1
            print("Too High")
            print("you have", guesses, "guesses left")
        elif player < computer:
            guesses -= 1
            print("Too Low")
            print("you have", guesses, "guesses left")


if gameType == "2":
    player = int(input("Pick a number between 1 and 10: "))


guesses = 3

if guesses == 0:
    print("the number was", player)

while guesses > 0:
    if guesses == 3:
        computer = randint(1, 10)
    if player == computer:
        print("Computer guessed it!!", player)
        break
    elif computer > player:
        guesses -= 1
        print("computer picked: ", computer)
        print("Too High")
        print("computer has", guesses, " guesses left")
        computer = randint(1, computer)

    elif computer < player:
        print("computer picked: ", computer)
        guesses -= 1
        print("Too Low")
        print("computer has", guesses, " guesses left")
        computer = randint(computer, 10)
