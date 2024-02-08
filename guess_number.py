number = 10
max_guesses = 5
current_guess = 0

print("I'm thinking of a number...")

while current_guess < max_guesses:
    guess_input = input(f"What number am I thinking of? (Enter 'q' to quit):  ")
    
    if guess_input.lower() == 'q':
        print(f"The correct number was {number}.")
        break

    guess = int(guess_input)
    current_guess += 1

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif current_guess == max_guesses:
        print("Sorry, you have no more guesses. The correct number was {number}.")
    else:
        guesses_left = max_guesses - current_guess
        print(f"Sorry, that is incorrect. You have {guesses_left} guess(s)? left.")

