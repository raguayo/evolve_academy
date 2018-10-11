basket = ['orange', 'apple', 'watermelon', 'pineapple', 'strawberry']
user_fruit_guess = raw_input("Guess a fruit:\n")
match = False;
for fruit in basket:
    if fruit  == user_fruit_guess:
        match = True
if match:
    print("You guessed right!")
else:
    print("Sorry, you guessed wrong!");


