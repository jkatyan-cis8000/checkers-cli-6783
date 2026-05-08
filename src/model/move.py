from dataclasses import dataclass
from typing import Optional

from .board import Board
from .piece import Player


@dataclass
class Move:
    start_row: int
    start_col: int
    end_row: int
    end_col: int
    is_capture: bool = False
    captured_row: Optional[int] = None
    captured_col: Optional[int] = None
