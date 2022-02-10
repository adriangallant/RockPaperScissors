import random
from actions import Action

wins = losses = ties = 0


def print_game_introduction():
    print()
    print('Welcome to Rock Paper Scissors!')
    print('Rules: ')
    print('*****************************************************')
    print('Rock beats Scissors, but loses to Paper')
    print('Scissors beats Paper, but loses to Rock')
    print('Paper beats Rock, but loses to Scissors')
    print('*****************************************************')
    print()


def get_user_selection():
    choices = [f"{selection.name}[{selection.value}]" for selection in Action.Selections]
    choices_str = ", ".join(choices)
    while True:
        try:
            user_input = int(input(f"Enter a choice ({choices_str}):"))
            selection = Action.Selections(user_input)
            break
        except ValueError:
            range_str = f"[0, {len(Action.Selections) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue
    return selection


def get_computer_selection():
    selection = random.randint(0, len(Action.Selections) - 1)
    selection = Action.Selections(selection)
    return selection


def determine_winner(user1_selection, user2_selection):
    global losses, wins, ties
    victories = {
        Action.Selections.Rock: [Action.Selections.Scissors],  # Rock beats scissors
        Action.Selections.Paper: [Action.Selections.Rock],  # Paper beats rock
        Action.Selections.Scissors: [Action.Selections.Paper]  # Scissors beat paper
    }

    defeats = victories[user1_selection]
    if user1_selection == user2_selection:
        print(f"Both players selected {user1_selection.name}. It's a tie!")
        ties += 1
    elif user2_selection in defeats:
        print(f"{user1_selection.name} beats {user2_selection.name}! You win!")
        wins += 1
    else:
        print(f"{user2_selection.name} beats {user1_selection.name}! You lose.")
        losses += 1
    print_total_game_results()


def print_total_game_results():
    global wins, losses, ties
    print()
    print('Wins: %s, Losses: %s, Ties: %s' % (wins, losses, ties))
    print()


def end_game():
    print('Thank you for playing!')
    print('Here is your record for this session: ')
    print_total_game_results()
    print('Goodbye!')


def ask_keep_playing():
    keep_playing_flag = input('Play again? (y/n):').lower().strip()
    is_playing = ''
    if keep_playing_flag == 'y':
        is_playing = True
    elif keep_playing_flag == 'n':
        is_playing = False
    else:
        print('Incorrect Option, Try Again:')
        ask_keep_playing()
    return is_playing


def decide_game_mode():
    while True:
        try:
            print()
            user_input = int(input('Single Player [1] or Multiplayer [2] :'))
            if user_input == 1:
                return True
            elif user_input == 2:
                return False
            else:
                raise ValueError('Incorrect Option, Try Again:')
        except ValueError as e:
            print(e)
            continue
