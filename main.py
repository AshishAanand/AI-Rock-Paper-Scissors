import random
from collections import Counter

choices = ["Rock", "Paper", "Scissors"]
player_history = []


# Identify Winner
def identify_winner(player, ai):
    if player == ai:
        return "Match Tie"
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Paper" and ai == "Rock") or \
         (player == "Scissors" and ai == "Paper"):
        return "Player Wins"
    else:
        return "AI Wins"


# Smart AI
def smart_ai_choose():
    # If history is small, randomly choose
    if len(player_history) < 5:
        return random.choice(choices)

    # Predict player's most frequent move
    most_common = Counter(player_history).most_common(1)[0][0]

    # Counter the player's most common move
    if most_common == "Rock":
        return "Paper"
    elif most_common == "Paper":
        return "Scissors"
    else:
        return "Rock"


# Main Game Loop
def play_game():
    global player_history

    player_score, ai_score, ties = 0, 0, 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice (Rock, Paper, Scissors) or 'Quit' to end the game.")

    while True:
        player_choose = input("Your Choice: ").capitalize()
        if player_choose == "Quit":
            break
        elif player_choose not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        player_history.append(player_choose)

        ai_choose = smart_ai_choose()


        result = identify_winner(player_choose, ai_choose)

        if result == "Player Wins":
            player_score += 1
        elif result == "AI Wins":
            ai_score += 1
        else:
            ties += 1

        print(f"You chose: {player_choose} | AI chose: {ai_choose}")

        print()

        print(f"Result: {result}")

    print("\nGame Over!")
    print(f"Final Scores - Player: {player_score}, AI: {ai_score}, Ties: {ties}")
    if player_score > ai_score:
        print("You are Great!")
    else:
        print("Thanks for playing Fool !")


if __name__ == "__main__":
    play_game()
