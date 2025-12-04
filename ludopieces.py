class Piece:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id
        self.position = (-1,-1)
        self.selected = False
    
    def get_valid_moves(self, board):
        possible = True
        if(self.position != (-1,-1)):
            print("yes")

        elif(board.dice == 6):
            print("yup")
    
    def move(self, new_position, board):
        old_position = self.position
        self.position = new_position
        return True
    
