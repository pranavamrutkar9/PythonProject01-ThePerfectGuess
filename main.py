from random import randint

# Generate a random number between 0 and 100
number_to_guess = randint(0, 100)
guess = -1
attempts = 0

print("Welcome to 'The Perfect Guess'!")
print("I'm thinking of a number between 0 and 100.")

while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")

print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
