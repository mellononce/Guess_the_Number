import random


class Guess:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0
        self.current_guess = 0

    def make_guess(self):
        while self.current_guess != self.number:
            try:
                self.current_guess = int(input("Guess a number between 1 and 100: "))
                self.guesses += 1
                if self.current_guess < self.number:
                    print("Too low")
                elif self.current_guess > self.number:
                    print("Too high")
            except ValueError:
                print("Please enter a valid integer.")
        print("You guessed the number in", self.guesses, "guesses")


# Create an instance of the game and play
game = Guess()
game.make_guess()
