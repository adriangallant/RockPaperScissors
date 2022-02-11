from enum import IntEnum, Enum


class Selections(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class Players(Enum):
    Player1 = 'P1'
    Player2 = 'P2'
    Computer = 'CPU'
