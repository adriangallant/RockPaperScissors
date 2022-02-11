# Make a Rock, Paper, Scissors Program
# I did my own version, then made improvements inspired from (notably dictionary, enums, exceptions)
# https://realpython.com/python-rock-paper-scissors/#play-several-games-in-a-row https://cocalc.com
from services import GameLogicService as gameLogicService

isPlaying = True

gameLogicService.print_game_introduction()
isComputerPlaying = gameLogicService.decide_game_mode()

while isPlaying:
    user1_selection = gameLogicService.get_user_selection()
    if isComputerPlaying:
        user2_selection = gameLogicService.get_computer_selection()
    else:
        user2_selection = gameLogicService.get_user_selection()
    gameLogicService.determine_winner(user1_selection, user2_selection, isComputerPlaying)
    isPlaying = gameLogicService.ask_keep_playing()

gameLogicService.end_game(isComputerPlaying)

# TODO: ADD DATABASE FOR CPU/PLAYER STAT TRACKING?
