let wins = 0;
let losses = 0;
let ties = 0;

let isComputerPlaying = true;

const choices = {
    0 : "Rock",
    1 : "Paper",
    2 : "Scissors",
}

const victoryScenarios = {
   0 : choices[1],
   1 : choices[2],
   2 : choices[3],
}

const PLAYERS = {
    player1: 'P1',
    player2: 'P2',
    computer: 'CPU',
}

function setComputerPlaying(bool) {
    isComputerPlaying = bool;
    console.log(isComputerPlaying);
}

function getKeyByValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
}

function insertResult(gameResult) {
    axios.post('http://127.0.0.1:5000/game/insertResult/', gameResult)
    .then(function (response) {
        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}

function buildGameResult(winner, loser, winner_choice, loser_choice, tie_choice, second_player) {
    let gameResult = {
        winner: winner,
        loser: loser,
        winner_choice: winner_choice,
        loser_choice: loser_choice,
        tie_choice: tie_choice,
        second_player: second_player,
    }
    console.log(gameResult);
    return gameResult;
}

function determineWinner(player1Choice, player2Choice) {
    const player2 = isComputerPlaying ? PLAYERS.computer : PLAYERS.player2;
    let losingChoice = victoryScenarios[player1Choice];
    losingChoice = getKeyByValue(choices, losingChoice);
    let gameRecord = {}
    if (Number(player1Choice) === Number(player2Choice)) {
        ties += 1;
        gameRecord = buildGameResult( 'NONE',
                                      'NONE',
                                      'NONE',
                                      'NONE',
                                      choices[player1Choice],
                                      player2
                                    );
    } else if (Number(player2Choice) === Number(losingChoice)) {
        wins += 1;
        gameRecord = buildGameResult( PLAYERS.player1,
                                      player2,
                                      choices[player1Choice],
                                      choices[player2Choice],
                                      'NONE',
                                      player2
                                    );
        console.log('Player 2 lost');
    } else {
        losses += 1;
        gameRecord = buildGameResult( player2,
                                      PLAYERS.player1,
                                      choices[player2Choice],
                                      choices[player1Choice],
                                      'NONE',
                                      player2
                                    );
        console.log('Player 1 lost');
    }
    console.log(`Wins: ${wins} Losses: ${losses} Ties: ${ties}`);
    insertResult(gameRecord);
}

function getComputerChoice() {
    const choice = Math.floor(Math.random() * Object.keys(choices).length);
    return choice;
}

function playGame(player1Choice) {
    player1Choice = getKeyByValue(choices, player1Choice);
    const computerChoice = getComputerChoice();
    console.log(`Player Choice: ${player1Choice}, Computer Choice: ${computerChoice}`);
    determineWinner(player1Choice, computerChoice);
}





/*

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

*/