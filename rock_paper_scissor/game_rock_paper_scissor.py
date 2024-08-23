def play_game():
    list_options = ["rock", "paper", "scissor"]
    while True:
        user1 = input("User1: Select rock, paper, scissor or STOP.").strip().lower()
        if user1 == "stop":
            print("Game Over!")
            break
        user2 = input("User2: Select rock, paper or scissor or STOP.").strip().lower()
        if user2 == "stop":
            print("Game Over!")
            break
        if user1 not in list_options or user2 not in list_options:
            print("Incorrect data. Please select rock, paper or scissor.")
            continue
        elif user1 == user2:
            print("Play again...")
            continue
        elif (user1 == "paper" and user2 == "scissor" or
              user1 == "scissor" and user2 == "rock" or
              user1 == "rock" and user2 == "paper"):
            print("User2 wins..")
        else:
            print("User1 wins..")


play_game()
