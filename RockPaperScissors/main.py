# Make a Rock, Paper, Scissors Program
# I did my own version, then made improvements inspired from (notably dictionary, enums, exceptions)
# https://realpython.com/python-rock-paper-scissors/#play-several-games-in-a-row

from services import GameLogicService as gameLogicService

isPlaying = True

gameLogicService.print_game_introduction()
isComputerPlaying = gameLogicService.decide_game_mode()

while isPlaying:
    user1_action = gameLogicService.get_user_action()
    if isComputerPlaying:
        user2_action = gameLogicService.get_computer_action()
    else:
        user2_action = gameLogicService.get_user_action()

    gameLogicService.determine_winner(user1_action, user2_action)
    isPlaying = gameLogicService.ask_keep_playing()

gameLogicService.end_game()

# TODO: ADD DATABASE FOR CPU STATS?
