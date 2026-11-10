# BAN 701 - Assignment 8
# Basketball Score Tracker

# This function calculates the average score across all games.
def calculate_average(scores):
    return sum(scores) / len(scores)


def main():
    print("Welcome to the Basketball Score Tracker!")

    # Store the scores entered by the user.
    scores = []

    # Ask the user how many games they want to track.
    number_of_games = int(input("How many games? "))

    if number_of_games <= 0:
        print("Please enter at least one game.")
        return

    # Repeat the process for each basketball game.
    for game in range(number_of_games):
        score = int(input(f"Enter score for game {game + 1}: "))
        scores.append(score)

    # Calculate and display the average score.
    average = calculate_average(scores)

    print("\nBasketball Score Summary")
    print("Games Played:", number_of_games)
    print("Total Points:", sum(scores))
    print("Average Points:", round(average, 2))
    print("Highest Score:", max(scores))
# Start the program.
if __name__ == "__main__":
    main()


