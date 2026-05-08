from ..model.board import Board
from ..model.game import GameState
from ..model.piece import Piece, Player
from ..config.symbols import RED_PIECE, BLACK_PIECE
from ..service.moves import get_valid_moves, apply_move
from ..service.rules import check_winner
from ..ui.display import display_board, display_game_state
from ..ui.input import get_user_move


def initialize_game() -> GameState:
    board = Board(size=8)
    
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:
                if row < 3:
                    board[row, col] = Piece(player=Player.BLACK, is_king=False)
                elif row > 4:
                    board[row, col] = Piece(player=Player.RED, is_king=False)
    
    return GameState(board, Player.RED, 1)


def game_loop(game: GameState) -> None:
    while True:
        display_board(game.board)
        display_game_state(game)
        
        move = get_user_move()
        
        game = apply_move(game, move)
        
        winner = check_winner(game)
        if winner is not None:
            display_board(game.board)
            print(f"Game over! Winner: {'RED' if winner == Player.RED else 'BLACK'}")
            break


def main() -> None:
    game = initialize_game()
    game_loop(game)


if __name__ == "__main__":
    main()
