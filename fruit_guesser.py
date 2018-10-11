import sys

basket = ['orange', 'apple', 'watermelon', 'pineapple', 'strawberry']
num_guesses = 1
while num_guesses <= 3:
    user_fruit_guess = raw_input("Guess a fruit: ")
    match = False;
    for fruit in basket:
        if fruit  == user_fruit_guess:
            match = True
    if match:
        print("You guessed right!")
        sys.exit(0)
    else:
        print("Sorry, you guessed wrong!");
        if num_guesses < 3:
            print("Guess again, I'll let you try " + str(3 - num_guesses) + " more time(s).\n")
        
    num_guesses += 1

