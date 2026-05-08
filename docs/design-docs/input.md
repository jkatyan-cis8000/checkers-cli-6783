# UI Input Module

## Overview

The `input.py` module handles move notation parsing and user input for the Checkers CLI game.

## Components

### parse_move_input(input_str: str) -> Move

Parses algebraic notation move string (e.g., "e6d5") into a Move object.

**Format:** `<from_square><to_square>` where each square is `<file><rank>`
- file: a-h (columns)
- rank: 1-8 (rows)

**Example:** "e6d5" moves from e6 to d5

**Errors:**
- ValueError if input length != 4
- IndexError if invalid coordinate format

### get_user_move() -> Move

Interactive prompt that:
1. Requests move input from user
2. Parses and validates the input
3. Returns Move object on success
4. Retries on invalid input with error message

**Format:** e6d5 (algebraic notation, case-insensitive)

## Dependencies

- `src.types.move.Move` - Parsed move with notation and positions
- `src.utils.coordinates.algebraic_to_coords()` - Converts notation to (row,col)

## Implementation Notes

- Input is case-insensitive (converted to lowercase)
- Uses `algebraic_to_coords` utility for coordinate conversion
- Loop continues until valid input received
- Error messages guide user to correct format
