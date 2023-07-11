import random


def guess_number():
    number = random.randint(1, top_of_range)
    attempts = 5

    print("==========")

    while True:
        if attempts > 0:
            user_guess = int(input("Take a guess: "))
            attempts -= 1
            print("==========")

            if user_guess == number:
                print("Your guess is correct!")
                print("You got it in " + str((5 - attempts)) + " attempts.")
                print("==========")
                quit()

            elif user_guess > number:
                print("You were above the number!")
                print(f"You have {attempts} attempts left.")
                print("==========")

            else:
                print("You were below the number!")
                print(f"You have {attempts} attempts left.")
                print("==========")
        else:
            print("You don't have any attempts left!")
            print(f"The correct number was {number}.")
            print("==========")
            quit()


while True:
    print("==========")
    print("Welcome to the Number Guessing Game!")
    print("You only have 5 attempts.")
    print("==========")

    top_of_range = int(input("Type the ending number: "))

    if top_of_range > 0:
        guess_number()

    else:
        print("Please type a number larger than 0.")
