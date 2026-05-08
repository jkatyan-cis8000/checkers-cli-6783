def algebraic_to_coords(algebraic: str) -> tuple[int, int]:
    """Convert algebraic notation (e.g., 'e6') to grid coordinates (row, col)."""
    if len(algebraic) != 2:
        raise ValueError("Invalid algebraic notation")
    
    col_char = algebraic[0]
    row_char = algebraic[1]
    
    if col_char not in 'abcdefgh':
        raise ValueError(f"Invalid column: {col_char}")
    if row_char not in '12345678':
        raise ValueError(f"Invalid row: {row_char}")
    
    col = ord(col_char) - ord('a')
    row = 8 - int(row_char)
    
    return (row, col)
