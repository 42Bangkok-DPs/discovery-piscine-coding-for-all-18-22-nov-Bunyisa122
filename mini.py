# Chess piece and board classes
class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, position, board):
        # Basic valid move function, to be expanded per piece type
        return []

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        x, y = position
        moves = [(x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2)
                 if 0 <= x+dx < 8 and 0 <= y+dy < 8 and (dx != 0 or dy != 0)]
        return moves

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        # Queen moves like a rook + bishop
        return []

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        return []

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        return []

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        x, y = position
        # Knight moves in an L-shape
        moves = [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
                 (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
        return [(nx, ny) for nx, ny in moves if 0 <= nx < 8 and 0 <= ny < 8]

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        x, y = position
        direction = 1 if self.color == "white" else -1
        moves = [(x + direction, y)]
        return moves

# Chessboard setup
class ChessBoard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Initialize white pieces
        self.board[0] = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        self.board[1] = [Pawn('white')] * 8
        
        # Initialize black pieces
        self.board[7] = [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')]
        self.board[6] = [Pawn('black')] * 8

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece.__class__.__name__[0] if piece else '.') for piece in row]))

    def get_piece(self, x, y):
        return self.board[x][y]

    def move_piece(self, start, end):
        sx, sy = start
        ex, ey = end
        piece = self.get_piece(sx, sy)
        if piece and (ex, ey) in piece.valid_moves(start, self.board):
            self.board[ex][ey] = piece
            self.board[sx][sy] = None
            return True
        return False

# Game loop
def play_game():
    board = ChessBoard()
    board.print_board()

    # Basic game loop (turn-based, no game-ending conditions yet)
    turn = 0  # 0 for white, 1 for black
    while True:
        player_color = "white" if turn == 0 else "black"
        print(f"{player_color.capitalize()}'s turn")
        start = input("Enter start position (e.g., 'e2'): ")
        end = input("Enter end position (e.g., 'e4'): ")

        # Convert positions to board indices
        start = (8 - int(start[1]), ord(start[0]) - ord('a'))
        end = (8 - int(end[1]), ord(end[0]) - ord('a'))

        if board.move_piece(start, end):
            board.print_board()
            turn = 1 - turn  # Switch turns
        else:
            print("Invalid move, try again.")

# Run the game
if __name__ == "__main__":
    play_game()
