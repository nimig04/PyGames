number = 4

user_input = input ("Enter 'y' if you woud like to play: ").lower()

if user_input == ("y"):
    user_number = int(input("Guess the magic number: "))
    if user_number == number:
        print("You're a hero! You did it!")
    elif abs(number - user_number)  == 1:
        print("You were off by one!")
    else:
        print("It's not you, it's me...")