class Square:
    def __init__(self,row,col,piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def __repr__(self):
        return f'Square({self.row}, {self.col})'
    
    def has_piece(self):
        return self.piece is not None
    