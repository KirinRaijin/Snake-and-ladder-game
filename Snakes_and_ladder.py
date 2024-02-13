import random
# admin menu using switch case
def admin_menu():
    print("\nAdmin Menu:")
    print("1. Add/Update/Delete Snakes and Ladders")
    print("2. Play a game as Admin")
    print("3. Go back to main menu")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

#updates snakes and ladder dictionaries or removes entry
def update_snakes_and_ladders():
    print("\nCurrent Snakes and Ladders:")
    print("Snakes:", snakes)
    print("Ladders:", ladders)

    action = input("Do you want to (A)dd, (U)pdate, or (D)elete? ").upper()


    # if the first value is less than the next it is assumed that it is a ladder
    # Else it is a ladder and will be added to that dictionary
    if action == 'A':
        position = int(input("Enter the head of the snake or bottom of the ladder: "))
        destination = int(input("Enter the tail of the snake or top of the ladder: "))
        if position in snakes or position in ladders:
            print("There is already a snake or ladder at that position. Update it instead.")
        elif 1 <= position <= 99:
            if(position>destination):
                snakes[position] = destination
            elif(position<destination):
                ladders[position]=destination
            print("Snake/Ladder added successfully!")
        else:
            print("Invalid position. Position should be between 1 and 99.")

    elif action == 'U':
        position = int(input("Enter the position of the head of the snake or bottom of the ladder to update: "))
        if position in snakes:
            destination = int(input("Enter the new tail of the snake or top of the ladder: "))
            snakes[position] = destination
            print("Snake/Ladder updated successfully!")
        elif position in ladders:
            destination = int(input("Enter the new tail of the snake or top of the ladder: "))
            ladders[position] = destination
            print("Snake/Ladder updated successfully!")
        else:
            print("No snake or ladder found at that position.")

    elif action == 'D':
        position = int(input("Enter the position of the snake or ladder to delete: "))
        if position in snakes:
            del snakes[position]
            print("Snake deleted successfully!")
        elif position in ladders:
            del ladders[position]
            print("Ladder deleted successfully!")
        else:
            print("No snake or ladder found at that position.")
            
#Defines admin gameplay where he can enter any number
def admin_game():
    admin_position = 1
    while admin_position < 100:
        move = int(input("Enter the number (1-6) to move: "))
        admin_position += move

        if admin_position in snakes:
            print(f"Oops! You got bitten by a snake and slid down to {snakes[admin_position]}.")
            admin_position = snakes[admin_position]
        elif admin_position in ladders:
            print(f"Great! You found a ladder and climbed up to {ladders[admin_position]}.")
            admin_position = ladders[admin_position]

        print(f"Now you are at position {admin_position} on the board.")

    print("\nCongratulations! Admin reached position 100. You won!")

#rolls die using random
def roll_dice():
    return random.randint(1, 6)

#moves player 
def move_player(player, steps):
    player['position'] += steps
    if player['position'] in snakes:
        print(f"Oops! {player['name']} got bitten by a snake and slides down.")
        player['position'] = snakes[player['position']]
    elif player['position'] in ladders:
        print(f"Great! {player['name']} found a ladder and climbs up.")
        player['position'] = ladders[player['position']]

#prints the board and replace the tiles with the current position
def print_board():
    print("Current Board:")
    for i in range(100, 0, -10):
        row = list(range(i, i - 10, -1))
        for square in row:
            player_at_square = None
            for player in players:
                if player['position'] == square:
                    player_at_square = player['name'][0]
                    break
            print(f"{player_at_square or square:2}", end=" | ")
        print()

#plays a round of snake and ladders for players        
def play_round(players):

    for player in players:
        input(f"{player['name']}, it's your turn. Press Enter to roll the dice.")
        dice_roll = roll_dice()

        print(f"{player['name']} rolled a {dice_roll}.")
        if player['position'] + dice_roll <= 100:
            move_player(player, dice_roll)

        if player['position'] == 100:
            print(f"\nCongratulations, {player['name']}! You won!")
            exit()

        print(f"{player['name']}'s current position: {player['position']}\n")
    print_board()

#menu to choose role
def choose_role():
    while True:
        role = input("Do you want to play as (A)dmin or (P)layer? ").upper()
        if role == 'A':
            while True:
                user_choice = admin_menu()

                if user_choice == '1':
                    update_snakes_and_ladders()
                elif user_choice == '2':
                    admin_game()
                elif user_choice == '4':
                    print("Exiting the game. Goodbye!")
                    exit()
                elif user_choice=='3':
                    print("Going Back to previous menu!")
                    choose_role()
                    
                else:
                    print("Invalid choice. Please enter 1, 2,3 or 4.")

        elif role == 'P':
            num_players = 1 
            #since only one player has to play the game
            
            for i in range(1, num_players + 1):
                player_name = input(f"Enter the name of Player {i}: ")
                players.append({'name': player_name, 'position': 1})

            while True:
                play_round(players)

        else:
            print("Invalid choice. Please enter A or P.")


#default values for snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44}

print("\nWelcome to Snake and Ladder Game!\n")
players = []
choose_role()
