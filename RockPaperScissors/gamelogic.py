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