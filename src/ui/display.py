from model.board import Board
from model.game import GameState
from model.piece import Piece, Player
from config.symbols import RED_PIECE, BLACK_PIECE


def display_board(board: Board) -> None:
    print("\n  a b c d e f g h")
    print(" +-----------------+")
    for row in range(board.size):
        print(f"{8-row}|", end=" ")
        for col in range(board.size):
            piece = board[row, col]
            if piece is None:
                print(".", end=" ")
            elif piece.player == Player.RED:
                print(RED_PIECE, end=" ")
            else:
                print(BLACK_PIECE, end=" ")
        print(f"|{8-row}")
    print(" +-----------------+")
    print("  a b c d e f g h\n")


def display_game_state(game: GameState) -> None:
    print(f"Turn {game.turn} - {game.current_player.name}'s move")
