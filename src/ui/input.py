from typing import Optional
from model.move import Move
from model.game import GameState
from utils.coordinates import algebraic_to_coords


def parse_move_input(move_str: str) -> Optional[Move]:
    """Parse algebraic notation like 'e6d5' into Move object."""
    if len(move_str) < 4:
        return None
    
    try:
        start_row, start_col = algebraic_to_coords(move_str[:2])
        end_row, end_col = algebraic_to_coords(move_str[2:4])
        
        return Move(
            start_row=start_row,
            start_col=start_col,
            end_row=end_row,
            end_col=end_col,
            is_capture=False
        )
    except (ValueError, IndexError):
        return None


def get_user_move() -> Move:
    """Get a valid move from the user."""
    while True:
        try:
            move_str = input("Enter move (e.g., e6d5): ").strip().lower()
            move = parse_move_input(move_str)
            if move:
                return move
            print("Invalid move format. Use algebraic notation (e.g., e6d5)")
        except (EOFError, KeyboardInterrupt):
            raise SystemExit
