import random

def main():
    '''
    Main Program
    '''

    # Added some extra print statements for readable output.

    print("ROCK - PAPER - SCISSOR Game")
    print("Score 5 points to win.")
    print()

    # Declaring variables
    choices = ["Rock", "Paper", "Scissor"]
    user_pts = 0
    comp_pts = 0

    while True:

        # Asking user for his choice
        print("R for Rock | P for Paper | S for Scissor")
        user_choice = input("Enter your choice : ")

        # Randomly choosing something
        comp_choice = random.choice(choices)
        print("Computer chose : ", comp_choice)
        print()

        # Checking the result
        if user_choice.upper() == 'R':

            if comp_choice == 'Rock':
                print("Oh! It's a tie.")

            elif comp_choice == 'Paper':
                print("Computer WINS!")
                comp_pts += 1

            else:
                print("You WIN!")
                user_pts += 1

        elif user_choice.upper() == 'P':

            if comp_choice == 'Rock':
                print("You WIN!")
                user_pts += 1

            elif comp_choice == 'Paper':
                print("Oh! It's a tie.")

            else:
                print("Computer WINS!")
                comp_pts += 1

        elif user_choice.upper() == 'S':

            if comp_choice == 'Rock':
                print("Computer WINS!")
                comp_pts += 1

            elif comp_choice == 'Paper':
                print("You WIN!")
                user_pts += 1

            else:
                print("Oh! It's a tie.")

        else:
            print("Could not determine result since you entered an invalid choice.")

        # Displaying the score
        print()
        print(f"You {user_pts} | Computer {comp_pts}")
        print()

        # Checking if either the computer or the user won.
        if comp_pts == 5:
            print("Computer WINS the game. Better luck next time.")
            break

        elif user_pts == 5:
            print("Congratulations! You have beaten the computer.")
            break

if __name__ == '__main__':
    main()