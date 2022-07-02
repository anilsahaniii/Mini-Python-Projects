import random

player_wins = 0
computer_wins = 0
options = ['r','p','s']

while True:

    player_input = input("Type 'R' for rock/'P' for paper/'S' for scissor/'Q' to quit: ").lower()
    if player_input == 'q':
        break
    if player_input not in options:
        print("Please type corret next time")
        continue

    else:
        print("You have typed",player_input+'.')

        random_number = random.randint(0,2)

        computer_pick = options[random_number]
        print("Computer picked",computer_pick+".")

        if player_input == 'r' and computer_pick == 's':
            print("You have won!")
            player_wins +=1
        elif player_input == 'p' and computer_pick == 'r':
            print("You have won!")
            player_wins +=1
        elif player_input == 's' and computer_pick == 'p':
            print("You have won!")
            player_wins +=1
        elif player_input == computer_pick:
            print("It's a draw")
            continue
        else:
            print("computer won!")
            computer_wins += 1
print("You have won",player_wins,"times.")
print("Computer have won",computer_wins,"times.")
print("Thank you! Goodbye!")
