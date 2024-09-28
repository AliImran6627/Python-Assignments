import random
NUM_ROUNDS = 3
PlayerPoints = 0
print("Welcome to the High-Low Game!")
print("---------------------------------")

for i in range(1,NUM_ROUNDS+1):
    print(f"ROUND {i}")
    plr_num = random.randint(1,100)
    comp_num = random.randint(1,100)

    print(f"Your number is {plr_num}")

    plr_guess = input("Guessing time! Is your number higher or lower than the computer's number? ")
    if type(plr_guess) == str:
        if plr_guess == "higher" or plr_guess == "Higher" or plr_guess == "HIGHER":
            if plr_num > comp_num:
                print("Your guess was correct!")
                PlayerPoints += 1
            elif plr_num == comp_num:
                print("It's a tie, computer wins")
            else:
                print("You guessed wrong, better luck next time.")
        elif plr_guess == "lower" or plr_guess == "LOWER" or plr_guess == "Lower":
            if plr_num < comp_num:
                print("Your guess was correct!")
                PlayerPoints += 1
            elif plr_num == comp_num:
                print("It's a tie, computer wins")
            else:
                print("You guessed wrong, better luck next time.")
        print(f"(Player) {plr_num} : {comp_num} (Computer)")
        print(f"Current score is: {PlayerPoints}\n")
    else:
        print("Invalid input")
print("GAME OVER")