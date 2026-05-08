from dataclasses import dataclass
from enum import Enum

class Player(Enum):
    RED = "red"
    BLACK = "black"


@dataclass
class Piece:
    player: Player
    is_king: bool = False
