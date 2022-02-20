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
   0 : choices[2],
   1 : choices[0],
   2 : choices[1],
}

const PLAYERS = {
    player1: 'P1',
    player2: 'P2',
    computer: 'CPU',
}

const cpuDialogue = {
    pregame: [
        'Choose your option. I am going to win!',
        'Get Ready!',
        "I'm gonna win!",
        'You are going to lose!',
        'Get used to second place...',
    ],
    duringChoice: [
        'Picking right now...',
        'Get ready to cry....',
        'Currently picking....',
        "I'm picking...",
        'Hmmmm...',
    ],
    winning: [
        'I won!',
        'Told you I was going to win!',
        'You lose!',
        'You lose! Hahaha!',
        'You should cry home to mama!',
        'Is that all you got? I win!',
    ],
    losing: [
        'Noooo! You win!',
        "I can't believe I lost to you!",
        'I lose... :(',
        "Don't get used to this feeling! I will win next time",
        'Maybe next time...',
    ],
    tie: [
        'A tie??',
        'You should be happy you managed to tie against me!',
        'Tie? Boring!',
    ],
}

function displayComputerDialogue(result) {
    let dialogueIndex = null;
    switch (result) {
        case 'tie':
            dialogueIndex = Math.floor(Math.random() * cpuDialogue.tie.length);
            document.getElementById('computerDialogue').innerHTML = cpuDialogue.tie[dialogueIndex];
            break;
        case 'loss':
            dialogueIndex = Math.floor(Math.random() * cpuDialogue.losing.length);
            document.getElementById('computerDialogue').innerHTML = cpuDialogue.losing[dialogueIndex];
            break;
        case 'win':
            dialogueIndex = Math.floor(Math.random() * cpuDialogue.winning.length);
            document.getElementById('computerDialogue').innerHTML = cpuDialogue.winning[dialogueIndex];
            break;
        case 'duringChoice':
            dialogueIndex = Math.floor(Math.random() * cpuDialogue.duringChoice.length);
            document.getElementById('computerDialogue').innerHTML = cpuDialogue.duringChoice[dialogueIndex];
            break;
        case 'pregame':
            dialogueIndex = Math.floor(Math.random() * cpuDialogue.pregame.length);
            document.getElementById('computerDialogue').innerHTML = cpuDialogue.pregame[dialogueIndex];
            break;
        default:
            document.getElementById('computerDialogue').innerHTML = 'Sorry, something went wrong!';
    }
}

function setComputerPlaying(bool) {
    isComputerPlaying = bool;
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
        displayComputerDialogue('tie');
    } else if (Number(player2Choice) === Number(losingChoice)) {
        wins += 1;
        gameRecord = buildGameResult( PLAYERS.player1,
                                      player2,
                                      choices[player1Choice],
                                      choices[player2Choice],
                                      'NONE',
                                      player2
                                    );
        displayComputerDialogue('win');
    } else {
        losses += 1;
        gameRecord = buildGameResult( player2,
                                      PLAYERS.player1,
                                      choices[player2Choice],
                                      choices[player1Choice],
                                      'NONE',
                                      player2
                                    );
        displayComputerDialogue('loss');
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
    let player2Choice = ''
    if (isComputerPlaying) {
        displayComputerDialogue('duringChoice');
        player2Choice = getComputerChoice();
        setTimeout(function (){ determineWinner(player1Choice, player2Choice); }, 2000);
    } else {
        // TODO: Add local multiplayer
    }
    console.log(`Player Choice: ${player1Choice}, Computer Choice: ${player2Choice}`);
}

function init() {
    displayComputerDialogue('pregame');
}
