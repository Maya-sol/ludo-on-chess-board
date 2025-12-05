class Piece:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id
        self.position = (-1,-1)
        self.selected = False
    
    def get_valid_moves(self, board):
     return
    
    def move(self, new_position):
        old_position = self.position
        self.position = new_position
        return old_position
    
