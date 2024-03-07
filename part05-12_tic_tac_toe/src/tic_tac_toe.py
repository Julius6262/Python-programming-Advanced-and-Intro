# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # Check if x and y are within the valid range
    if 0 <= x < len(game_board[0]) and 0 <= y < len(game_board):
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
    return False
