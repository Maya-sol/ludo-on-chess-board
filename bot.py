from ludoboard import Board

class Bot:
    def __init__(self, board: Board):
        self.board = board

    def opponent_at_start(self):
        for i in self.board.first:
            if i.position == (7,7):
                return True
        return False
    
    def opponent_at_move_end(self, position):
        piece = self.board.get_piece_at(position[0], position[1])
        if piece is not None and piece.symbol == 'B':
            return True
        return False
    
    def distance_from_start(self, position):
        if position[0] == 7:
            return 7 - position[1]
        if position[1] == 0:
            return 14 - position[0]
        if position[0] == 0:
            return 14 + position[1]
        return 21 + position[0]


    def choose_move(self, moves):
        if len(moves) == 1:
            return 0
        move = len(moves) - 1
        distance = 30
        for i in range(len(moves) - 1, -1, -1):
            if moves[i] == 'start':
                move = 0
                if self.opponent_at_start():
                    return move
            elif self.opponent_at_move_end(moves[i]):
                return i
            elif self.distance_from_start(moves[i]) < distance:
                move = i
        return move
            

