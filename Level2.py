from random import randint

player = int(input("Pick a number between 1 and 10: "))


guesses = 3

if guesses == 0:
    print("the number was", player)

while guesses > 0:
    computer = randint(1, 10)
    if player == computer:
        print("Computer guessed it!!", player)
        break
    elif computer > player:
        guesses -= 1
        print("computer picked: ", computer)
        print("Too High")
        print("computer has", guesses, " guesses left")
    elif computer < player:
        print("computer picked: ", computer)
        guesses -= 1
        print("Too Low")
        print("computer has", guesses, " guesses left")
