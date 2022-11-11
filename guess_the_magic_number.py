from random import randint

played = False

while True:

    question = "Play again? (y/n)" if played else "Wanna play? (y/n)"

    playing = input(question).strip().lower() == "y"

    if playing:

        played = True

        # Choose a random number
        number_to_guess = randint(1, 10)

        # Get player's guess
        while True:
            try:
                number_guessed = int(input("Guess the magic number: "))
                break

            except ValueError:
                print("That's not a number. Try again.")

        # Evaluate guess
        if number_guessed == number_to_guess:
            print("You're a hero! You did it!")

        elif abs(number_to_guess - number_guessed) == 1:
            print("You were off by one!")

        else:
            print("It's not you, it's me...")

    else:
        print("Thanks for playing!")
        break
