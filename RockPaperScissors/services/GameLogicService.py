import random
import getpass
from actions import Action
from database import databaseService as dB

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
            user_input = int(getpass.getpass(prompt=f"Enter a choice ({choices_str}):"))
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


def determine_winner(user1_selection, user2_selection, is_computer_playing):
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
        dB.insert_result(
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            Action.Selections(user1_selection).name,
            (lambda cpu_playing: Action.Players.Computer.value if cpu_playing else Action.Players.Player2.value)(
                is_computer_playing)
        )
    elif user2_selection in defeats:
        print(f"{user1_selection.name} beats {user2_selection.name}!",
              (lambda cpu_playing: 'You win!' if cpu_playing else 'Player 1 wins!')(is_computer_playing))
        wins += 1
        dB.insert_result(
            Action.Players.Player1.value,
            (lambda cpu_playing: Action.Players.Computer.value if cpu_playing else Action.Players.Player2.value)(
                is_computer_playing),
            Action.Selections(user1_selection).name,
            Action.Selections(user2_selection).name,
            'NONE',
            (lambda cpu_playing: Action.Players.Computer.value if cpu_playing else Action.Players.Player2.value)(
                is_computer_playing)
        )
    else:
        print(f"{user2_selection.name} beats {user1_selection.name}!",
              (lambda cpu_playing: 'You lose!' if cpu_playing else 'Player 2 wins!')(is_computer_playing))
        losses += 1
        dB.insert_result(
            (lambda cpu_playing: Action.Players.Computer.value if cpu_playing else Action.Players.Player2.value)(
                is_computer_playing),
            Action.Players.Player1.value,
            Action.Selections(user2_selection).name,
            Action.Selections(user1_selection).name,
            'NONE',
            (lambda cpu_playing: Action.Players.Computer.value if cpu_playing else Action.Players.Player2.value)(
                is_computer_playing)
        )
    print_total_game_results(is_computer_playing)


def print_total_game_results(is_computer_playing):
    global wins, losses, ties
    print()
    if is_computer_playing:
        print('Wins: %s\nLosses: %s\nTies: %s' % (wins, losses, ties))
    else:
        print('Player 1 Wins: %s\nPlayer 2 Wins: %s\nTies: %s' % (wins, losses, ties))
    print()


def end_game(is_computer_playing):
    print()
    print('Thank you for playing!')
    print('Here is your record for this session: ')
    print_total_game_results(is_computer_playing)
    print('Goodbye!')
    print()


def ask_keep_playing():
    while True:
        keep_playing_flag = input('Play again? (y/n):').lower().strip()
        if keep_playing_flag == 'y':
            return True
        elif keep_playing_flag == 'n':
            return False
        else:
            print('Incorrect Option, Try Again:')
            continue


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
        except ValueError:
            print('Incorrect Option, Try Again:')
            continue
