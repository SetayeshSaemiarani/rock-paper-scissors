# Project: Rock-Paper-Scissors Game
# Author: Setayesh Saemiarani
# Description: An interactive console-based implementation of Rock-Paper-Scissors.

import random


def get_user_choice():
    """Get a valid user choice between 1 and 3 from the player."""
    while True:
        print("\n--- Choose your weapon ---")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        
        # Strip whitespace to prevent errors from accidental spaces
        user_input = input("Enter your choice (1, 2, or 3): ").strip()

        # Check if the input contains only digits
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a NUMBER (1, 2, or 3).")
            continue
        # Convert validated string to integer    
        user_choice = int(user_input)
        
        # Ensure the number is within the allowed game range
        if 1 <= user_choice <= 3:
            return user_choice
        else:
            print("❌ Invalid range! Please enter 1, 2, or 3.")

def get_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "Tie"
    
    # Logic: 1 (Rock) beats 3 (Scissors), 2 (Paper) beats 1 (Rock), 3 (Scissors) beats 2 (Paper)
    if (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return "User"
    else:
        return "Computer"
    

def display_result(winner):
    """Display the result of the round."""
    if winner == "Tie":
        print("\n🤝 It's a Tie!")
    elif winner == "User":
        print("\n🎉 You Win!")
    else:
        print("\n🤖 Computer Wins!")


def display_score(user_score, computer_score, ties):
    """Display the current scoreboard."""
    print("\n========== SCORE ==========")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    print(f"Ties     : {ties}")
    print("===========================")


def main():
    # Mapping integer inputs to readable string names
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }

    # Initialize game statistics
    user_score = 0
    computer_score = 0
    ties = 0
    print("Welcome to Rock-Paper-Scissors!")

    # Main game loop
    while True:

        # Get valid input from user
        user_choice = get_user_choice()

        # Generate random choice for computer
        computer_choice = random.randint(1, 3)

        # Display what both players chose
        print(f"\nYou chose      : {choices[user_choice]}")
        print(f"Computer chose : {choices[computer_choice]}")

        # Determine the winner
        winner = get_winner(user_choice, computer_choice)

        # Update the scoreboard
        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1
        else:
            ties += 1

        # Show results and current score
        display_result(winner)
        display_score(user_score, computer_score, ties)

        # Prompt for next round with input validation
        while True:
            again = input("\nPlay another round? (y/n): ").strip().lower()
            if again == "y":
                break  # Exit the inner loop to start a new round
            elif again == "n":
                print("\n--- Final Results ---")
                display_score(user_score, computer_score, ties)
                print("👋 Thanks for playing! Goodbye.")
                return  # Exit the entire program
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()