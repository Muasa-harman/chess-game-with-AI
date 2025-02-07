from const import *
from square import Square
from piece import Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create
# Square(row,col) for col in range(COLS)

    def _create(self):
        self._add_pieces('white')
        self._add_pieces('black')

        for row in range(ROWS):
            for col in range(COLS):
                #  if not isinstance(self.squares[row][col], Square):
                    self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # if color == 'white':
        #     row_pawn, row_other = (6,7)  #or
        # else:
        #     row_pawn, row_other = (1,0)    

        row_pawn, row_other = (6,7) if color == 'white'else (1,0)

        # add  pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color))

            # knights
            self.squares[row_other][1] = Square(row_other, 1, Knight(color))
            self.squares[row_other][6] = Square(row_other,6,Knight(color))

            # bishops
            self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
            self.squares[row_other][5] = Square(row_other,5,Bishop(color))

            # Rooks
            self.squares[row_other][0] = Square(row_other, 0, Rook(color))
            self.squares[row_other][7] = Square(row_other,7,Rook(color))

            # queens
            self.squares[row_other][3] = Square(row_other, 3, Queen(color))

            # kings
            self.squares[row_other][4] = Square(row_other, 4, King(color))