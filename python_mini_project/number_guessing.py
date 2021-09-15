# updated version
import random
# for instructions so that the user understands
def instructions():
    print("Welcome to the guessing game you will have 3 tries to pick a number 1-10")
    print("Good luck btw it's all random")


instructions()
# guess limit so the user can't guess too much.
guess_limit = 1
# The random guess
number = random.randint(1, 10)
print(number)
# What users can type and see.
user = int(input("What is the number?: "))
# The while loop so it can go on.
while user != number:

    if user > number:
        print("Lower")

    elif user < number:
        print("Higher")

    user = int(input("What is the number?: "))
    guess_limit += 1
    if guess_limit == 3:
        print("------------------------------------------------------")
        print("You ran out of guess ;( the answer was", number, "<--")
        print("------------------------------------------------------")
        break
else:
    print("You guessed it right! The number is", number,
          "and it only took you ", guess_limit, "tries")