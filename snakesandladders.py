import random


ladders = {2: 38, 4: 14, 8: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

def dice_roll():
    return random.randint(1, 6)

def get_position(player, position):
    if position in ladders:
        print(f"Player {player} hit a ladder at {position}! Climb up to {ladders[position]}")
        return ladders[position]
    elif position in snakes:
        print(f"Player {player} got bitten by a snake at {position}! Slide down to {snakes[position]}")
        return snakes[position]
    return position

def play():
    players = ["Player 1", "Player 2"]
    positions = [0, 0]
    winner = None
    
    print("Welcome to Snake and Ladder Game.")
    print("Version: 1.0.0")
    print("Rules:")
    print("  1. Initially all the players are at starting position i.e. 0.")
    print("     Take it in turns to roll the dice.")
    print("     Move forward the number of spaces shown on the dice.")
    print("  2. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
    print("  3. If you land on the head of a snake, you must slide down to the bottom of the snake.")
    print("  4. The first player to get to the FINAL position is the winner.")
    print("  5. Hit enter to roll the dice.")
    print("  6. Sign up the number of players and names to begin")

    while not winner:
        for i, player in enumerate(players):
            input(f"{player}'s turn. Press Enter to roll the dice...")
            roll = dice_roll()
            print(f"{player} rolled a {roll}.")
            positions[i] += roll
            positions[i] = get_position(player, positions[i])
            print(f"{player} is now at position {positions[i]}.\n")

            if positions[i] >= 100:
                winner = player
                break

    print(f"Congratulations! {winner} wins the game!")

if __name__ == "__main__":
    play()
