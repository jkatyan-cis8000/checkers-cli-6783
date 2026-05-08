from typing import List, Optional
from model.board import Board
from model.game import GameState
from model.move import Move
from model.piece import Player, Piece


def get_valid_moves(game: GameState, row: int, col: int) -> List[Move]:
    moves = []
    board = game.board

    piece = board[row, col]
    if piece is None:
        return moves

    directions = []
    if piece.player == Player.RED or piece.is_king:
        directions.extend([(-1, -1), (-1, 1)])
    if piece.player == Player.BLACK or piece.is_king:
        directions.extend([(1, -1), (1, 1)])

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if _is_valid_pos(board, new_row, new_col) and board[new_row, new_col] is None:
            moves.append(Move(
                start_row=row, start_col=col,
                end_row=new_row, end_col=new_col,
                is_capture=False
            ))

    for dr, dc in directions:
        jump_row, jump_col = row + 2 * dr, col + 2 * dc
        mid_row, mid_col = row + dr, col + dc
        if _is_valid_pos(board, jump_row, jump_col) and board[jump_row, jump_col] is None:
            mid_piece = board[mid_row, mid_col]
            if mid_piece is not None and mid_piece.player != piece.player:
                moves.append(Move(
                    start_row=row, start_col=col,
                    end_row=jump_row, end_col=jump_col,
                    is_capture=True,
                    captured_row=mid_row,
                    captured_col=mid_col
                ))

    return moves


def _is_valid_pos(board: Board, row: int, col: int) -> bool:
    return 0 <= row < board.size and 0 <= col < board.size


def apply_move(game: GameState, move: Move) -> GameState:
    new_board = Board(size=game.board.size)
    for r in range(game.board.size):
        for c in range(game.board.size):
            new_board[r, c] = game.board[r, c]

    piece = new_board[move.start_row, move.start_col]
    if piece is None:
        return game
    
    new_board[move.start_row, move.start_col] = None

    # Handle capture
    if move.is_capture and move.captured_row is not None and move.captured_col is not None:
        new_board[move.captured_row, move.captured_col] = None

    # King promotion
    is_king = piece.is_king
    if piece.player == Player.RED and move.end_row == 0:
        is_king = True
    elif piece.player == Player.BLACK and move.end_row == new_board.size - 1:
        is_king = True

    new_board[move.end_row, move.end_col] = Piece(player=piece.player, is_king=is_king)

    next_player = Player.BLACK if game.current_player == Player.RED else Player.RED
    next_turn = game.turn + 1

    return GameState(new_board, next_player, next_turn)


def is_capture_move(move: Move) -> bool:
    return move.is_capture
