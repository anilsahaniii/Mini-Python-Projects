 import random

print("Welcome to Guessing a number game")
top_of_end = input("Enter a number upto which you want to guess: ")

if top_of_end.isdigit():
    top_of_end = int(top_of_end)
    
    if top_of_end <=0:
        print("Please type an number more than 0")
        quit()
else:
    print("Please enter a number next time")
    quit()
    
random_number = random.randint(0,top_of_end)
count = 0
while True:
    count += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number next time")
        continue
    if guess == random_number:
        print("You got it correct")
        break
    elif guess > random_number:
        print("Your guess is higher ,try again")
    else:
        print("Your guess is lower,try again")
        
print("You got it in",count,"guesses")
