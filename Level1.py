from random import randint

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
