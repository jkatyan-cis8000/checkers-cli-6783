from dataclasses import dataclass
from .board import Board
from .piece import Player


@dataclass
class GameState:
    board: Board
    current_player: Player
    turn: int = 1
