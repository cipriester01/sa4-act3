number = 10
print("I'm thinking of a number...")

while True:
    guess_input = input("What number am I thinking of? (Enter 'q' to quit):  ")
    
    if guess_input.lower() == 'q':
        print(f"The correct number was {number}.")
        break

    guess = int(guess_input)

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry, your guess is too low..")
    else:
        print("Sorry, your guess is too high..")

