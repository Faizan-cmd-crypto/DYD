import random

choices = ["snake", "water", "gun"]
user_score = 0
comp_score = 0
MAX_SCORE = 5

print("Welcome to Snake Water Gun Game!")
print("First to 5 wins!\n")

while user_score < MAX_SCORE and comp_score < MAX_SCORE:
    user = input("Choose (snake/water/gun): ").lower()
    if user not in choices:
        print("Invalid choice. Try again.\n")
        continue

    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a draw!\n")
    elif (user == "snake" and comp == "water") or \
         (user == "water" and comp == "gun") or \
         (user == "gun" and comp == "snake"):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        comp_score += 1

    print(f"Score: You {user_score} - {comp_score} Computer\n")

# Final result
if user_score == MAX_SCORE:
    print("Congratulations! You WON the game!")
else:
    print("Game Over! Computer WON the game!")