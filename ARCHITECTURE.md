# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `src/types/piece.py`: Piece type (player: Player, is_king: bool)
- `src/types/board.py`: 8x8 board state with piece positions
- `src/types/move.py`: Move notation (e.g., "e6d5") and parsed move
- `src/types/game.py`: Game state (board, current_player, turn_count)
- `src/config/defaults.py`: BOARD_SIZE=8, PLAYER_RED, PLAYER_BLACK constants
- `src/config/symbols.py`: Unicode symbols (●, ○, ◆, ◇) for display
- `src/service/moves.py`: Calculate valid moves, capture detection, kinging
- `src/service/rules.py`: Win detection, mandatory capture check
- `src/ui/display.py`: Render board to terminal, display game state
- `src/ui/input.py`: Parse move notation (e.g., "e6d5")
- `src/utils/coordinates.py`: Convert algebraic notation (a1) to (row, col)
- `src/runtime/main.py`: Entry point, game loop, user interaction

## Interfaces

### Types Layer
- `Piece(player: Player, is_king: bool = False)` - immutable piece
- `Player.RED` / `Player.BLACK` - enum values
- `Board(size=8)` - 2D array of optional Piece
- `Move(notation: str, from_pos: tuple, to_pos: tuple)` - parsed move
- `GameState(board: Board, current_player: Player, turn: int)`

### Service Layer
- `get_valid_moves(game: GameState, row: int, col: int) -> list[Move]` - moves from position
- `apply_move(game: GameState, move: Move) -> GameState` - new state after move
- `check_winner(game: GameState) -> Player | None` - game end detection

### UI Layer
- `display_board(board: Board) -> None` - print to stdout
- `parse_move_input(input_str: str) -> Move` - parse "e6d5" format
- `game_loop() -> None` - main interaction loop

## Shared Data Structures

```python
# Algebraic notation: columns a-h (0-7), rows 1-8 (7-0 in zero-indexed)
# (0, 0) = a8, (7, 7) = h1
# Player: RED = 0, BLACK = 1
# Piece: (player, is_king)
# Board: 8x8 array, None for empty, Piece for occupied
```

## External Dependencies

No external dependencies. Uses only Python standard library.
