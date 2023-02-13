import random

class GuessingGame():
    
    def __init__(self, ans):
        self.answer = ans
        self.status = False

    def solved(self):
        return self.status
    
    def guess(self, user_guess):
        if user_guess == self.answer:
            self.status = True
            return 'correct'
        elif user_guess > self.answer:
            return 'high'
        else:
            return 'low'

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")