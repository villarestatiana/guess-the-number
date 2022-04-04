import random 
from art import logo

print(logo)
random_number = random.randint(0, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.")


def game(attempts):
  
  print(f"You have {attempts} attempts remaining to guess the number.")
  users_number = int(input("Choose a number: "))
  attempts -= 1
   
  while attempts > 0 and users_number != random_number: 
    if users_number < random_number:
      print("Too low. Guess Again")
      users_number = int(input(f"You have {attempts} attempts remaining to guess the number. Choose a number : "))    
    elif users_number > random_number:
      print("Too high. Guess Again")
      users_number = int(input(f"You have {attempts} attempts remaining to guess the number. Choose a number : "))  
    attempts -= 1

  if users_number == random_number:
    print("You got it!")
  elif attempts == 0:
    print(f"You've run out of guesses, you lose. The number was {random_number}")

if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

game(attempts)
  
  
  


  
  