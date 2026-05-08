from dataclasses import dataclass
from typing import Optional

from .piece import Piece


@dataclass
class Board:
    size: int = 8
    _grid: Optional[list] = None

    def __post_init__(self):
        if self._grid is None:
            self._grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def __getitem__(self, position: tuple[int, int]) -> Optional[Piece]:
        row, col = position
        return self._grid[row][col]

    def __setitem__(self, position: tuple[int, int], piece: Optional[Piece]) -> None:
        row, col = position
        self._grid[row][col] = piece
