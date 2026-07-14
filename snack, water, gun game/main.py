import random

while True:

    choices = {
        "snake": 1,
        "water": -1,
        "gun": 0
    }

    reverse = {
        1: "snake",
        -1: "water",
        0: "gun"
    }

    user_score = 0
    computer_score = 0

    print("\n===== Snake Water Gun Game =====")

    # 5 Rounds
    for round in range(1, 6):

        print(f"\n--------- Round {round} ---------")

        computer = random.choice([1, -1, 0])

        user = input("Enter snake, water or gun: ").lower()

        if user not in choices:
            print("Invalid Choice! Round Skipped.")
            continue

        you = choices[user]

        print(f"Computer: {reverse[computer]}")
        print(f"You: {reverse[you]}")

        if computer == you:
            print("Result : Draw!")

        elif (you == 1 and computer == -1) or \
             (you == -1 and computer == 0) or \
             (you == 0 and computer == 1):

            print("Result : You Win!")
            user_score += 1

        else:
            print("Result : Computer Wins!")
            computer_score += 1

        print(f"Score --> You: {user_score} | Computer: {computer_score}")

    print("\n========== FINAL SCORE ==========")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    if user_score > computer_score:
        print("\n🎉 Congratulations! You Won the Game!")

    elif computer_score > user_score:
        print("\n😔 Computer Won the Game!")

    else:
        print("\n🤝 Match Draw!")

    play = input("\nDo you want to play again? (Y/N): ").lower()

    if play != "y":
        print("\nThanks for Playing! 😊")
        break
