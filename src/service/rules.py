from typing import List, Optional
from model.game import GameState
from model.piece import Player
from model.board import Board
from service.moves import get_valid_moves, is_capture_move


def check_winner(game: GameState) -> Optional[Player]:
    board = game.board
    red_pieces = 0
    black_pieces = 0
    
    for row in range(board.size):
        for col in range(board.size):
            piece = board[row, col]
            if piece is not None:
                if piece.player == Player.RED:
                    red_pieces += 1
                elif piece.player == Player.BLACK:
                    black_pieces += 1
    
    if red_pieces == 0:
        return Player.BLACK
    if black_pieces == 0:
        return Player.RED
    
    if not has_valid_moves(game, game.current_player):
        return Player.BLACK if game.current_player == Player.RED else Player.RED
    
    return None


def has_valid_moves(game: GameState, player: Player) -> bool:
    board = game.board
    
    for row in range(board.size):
        for col in range(board.size):
            piece = board[row, col]
            if piece is not None and piece.player == player:
                moves = get_valid_moves(game, row, col)
                if len(moves) > 0:
                    return True
    
    return False
