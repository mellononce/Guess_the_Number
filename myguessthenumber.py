import random


class GuessNumber:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.number = random.randint(self.min, self.max)
        self.guesses = 0

    def guess(self, number):
        self.guesses += 1  # Increment the number of guesses
        if number < self.number:
            return "Too low"
        elif number > self.number:
            return "Too high"
        else:
            return "You got it!"


    def reset(self):
        self.number = random.randint(self.min, self.max)
        self.guesses = 0    # Reset the number of guesses

    def __str__(self):
        return f"Guess a number between {self.min} and {self.max}"


game = GuessNumber(1, 10)
print(game)

# Game loop
while True:
    try:
        user_guess = int(input("Enter your guess: "))  # Convert the input to an integer
        result = game.guess(user_guess)
        print(result)
        if result == "You got it!":
            if game.guesses == 1:
                print("Congratulations! You guessed the number in 1 guess!")
            else:
                print("Congratulations! You guessed the number in", game.guesses, "guesses.")
            game.reset()
    except ValueError:
        print("Please enter a valid integer.")

