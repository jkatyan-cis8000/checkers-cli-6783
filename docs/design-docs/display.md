# UI Display Module

## Overview

The `display.py` module handles terminal rendering for the Checkers game board and game state information.

## Components

### display_board(board: Board) -> None

Renders the 8x8 checkers board to stdout with coordinate labels.

**Format:**
- Columns labeled a-h (left to right)
- Rows labeled 1-8 (bottom to top)
- Empty squares: `·`
- Red piece: `●`
- Red king: `◆`
- Black piece: `○`
- Black king: `◇`

**Layout:**
```
  a b c d e f g h
8 · ● · ● · ● · ● 8
7 ● · ● · ● · ● · 7
6 · ● · ● · ● · ● 6
5 · · · · · · · · 5
4 · · · · · · · · 4
3 ○ · ○ · ○ · ○ · 3
2 · ○ · ○ · ○ · ○ 2
1 ○ · ○ · ○ · ○ · 1
  a b c d e f g h
```

### display_game_state(game: GameState) -> None

Displays current game status:
- Current player (RED or BLACK)
- Turn number

## Dependencies

- `src.types.board.Board` - 8x8 game board
- `src.types.game.GameState` - game state with player and turn
- `src.types.piece.Player` - RED/BLACK enum
- `src.config.symbols` - Unicode piece symbols

## Implementation Notes

- Board grid uses zero-indexed (row, col) with (0,0) = a8
- Coordinate mapping: row 0 = rank 8, col 0 = file a
- Symbols defined in config layer for easy theming
