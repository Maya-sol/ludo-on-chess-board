from ludoboard import *
from ludopieces import Piece
from ludoconst import *

class Ludo:
    def __init__(self):
        self.board = Board()
        self.dice = 0
        self.turn = 'B'
        self.moves = []
        self.ids = []

    def check_start (self):
        if(self.turn == 'B' and self.dice == 6):
            for i in self.board.first:
                if(i.position == (-1,-1)):
                    self.ids.append(i)
                    return True
        elif (self.turn == 'R' and self.dice == 6):
            for i in self.board.second:
                if(i.position == (-1,-1)):
                    self.ids.append(i)
                    return True
        return False
    
    def moving_directon(self, position):
        if(position[0] == 0 and position[1] > 0):
            return (0,-1)
        if(position[0] < 7 and position[1] == 0):
            return (1,0)
        if(position[0] == 7 and position[1] < 7):
            return (0,1)
        if(position[0] > 0 and position[1] == 7):
            return (-1,0)
        if(position == (0,0)):
            return (1,0)
        return (-1,0)
        
    def check_road(self, position):
        old_row, old_col = position
        for i in range(1, self.dice):
            d1 = self.moving_directon((old_row, old_col))
            old_row += d1[0]
            old_col += d1[1] 
            if self.board.grid[old_row][old_col] != '.':
                return(-1, -1)
            if self.turn == 'B':
                if old_row == 0 and old_col == 0:
                    return (-1,-1)
            else:
                if old_row == 7 and old_col == 7:
                    return (-1,-1)      
        
        a = self.moving_directon((old_row,old_col))
        old_row += a[0]
        old_col += a[1]    
        return (old_row, old_col)



    def get_valid_moves(self):
        if (self.check_start()):
            self.moves.append('start')
        if (self.turn == 'B'):
            for i in self.board.first:
                m = self.check_road(i.position)
                if self.board.is_valid_position(m[0],m[1]):
                    self.moves.append(m)
                    self.ids. append(i)
        elif (self.turn == 'R'):
            for i in self.board.second:
                m = self.check_road(i.position)
                if self.board.is_valid_position(m[0],m[1]):
                    self.moves.append(m)
                    self.ids. append(i)
    
    def start(self):
        if self.turn == 'B':
            if self.board.grid[0][0] == 'B':
                return
            if self.board.grid[0][0] == 'R':
                p = self.board.get_piece_at(0,0)
                if (p is not None):
                    p.position = (-1,-1)
                self.board.grid[0][0] = 'B'
                return
            for i in self.board.first:
                if i.position == (-1,-1):
                    i.position = (0,0)
                    self.board.grid[0][0] = 'B'
                    return
        if self.turn == 'R':
            if self.board.grid[7][7] == 'R':
                return
            if self.board.grid[7][7] == 'B':
                p = self.board.get_piece_at(7,7)
                if (p is not None):
                    p.position = (-1,-1)
                self.board.grid[7][7] = 'R'
                return
            for i in self.board.second:
                if i.position == (-1,-1):
                    i.position = (7,7)
                    self.board.grid[7][7] = 'R'
                    return
                
    def check_arrive(self, position):
        if self.turn == 'B' and position == (0,0):
            return True
        if self.turn == 'R' and position == (7,7):
            return True
        return False

    def roll(self):
        elements = [1, 2, 3, 4, 5, 6]
        weights = [1, 1, 1, 1, 1, 3]
        self.dice = random.choices(elements, weights=weights, k=1)[0]
        return self.dice

    def arrive (self, piece):
        if self.turn == 'B':
            if self.board.get_piece_at(3,3) is None:
                piece.position = (3,3)
            elif self.board.get_piece_at(2,2) is None:
                piece.position = (2,2)
            elif self.board.get_piece_at(1,1) is None:
                piece.position = (1,1)
            elif self.board.get_piece_at(0,0) is None:
                piece.position = (0,0)
            for i in self.board.first:
                if i.id == piece.id:
                    self.board.first.remove(i)
                    break
        else:
            if self.board.get_piece_at(4,4) is None:
                piece.position = (4,4)
            elif self.board.get_piece_at(5,5) is None:
                piece.position = (5,5)
            elif self.board.get_piece_at(6,6) is None:
                piece.position = (6,6)
            elif self.board.get_piece_at(7,7) is None:
                piece.position = (7,7)
            for i in self.board.second:
                if i.id == piece.id:
                    self.board.second.remove(i)
                    break
        return piece.position
            
def play():
    a = Ludo()
    while True:
        a.board.display()
        print(a.roll())
        a.get_valid_moves()
        print(a.moves)
        if a.moves:
            print(a.turn)
            i = int(input("choose number of move"))
            print(a.ids[i].id)
            if (a.moves[i] == 'start'):
                a.start()
            else:
                removed = a.board.get_piece_at(a.moves[i][0], a.moves[i][1])
                a.board.update_piece_position(a.ids[i].position, a.moves[i], 'B')
                if removed is not None:
                    removed.position = (-1 , -1)
                if a.check_arrive(a.moves[i]):
                    a.board.update_piece_position(a.ids[i].position, a.arrive(a.ids[i]), 'B')
                else: a.ids[i].position = a.moves[i]
        a.moves =[]
        a.ids =[]
        a.board.display()
        a.turn = 'R'
        print(a.roll())
        a.get_valid_moves()
        print(a.moves)
        if a.moves:
            print(a.turn)
            i = int(input("choose number of move"))
            print(a.ids[i])
            if (a.moves[i] == 'start'):
                a.start()
            else:
                removed = a.board.get_piece_at(a.moves[i][0], a.moves[i][1])
                a.board.update_piece_position(a.ids[i].position, a.moves[i],'R')
                if removed is not None:
                    removed.position = (-1 , -1)
                if a.check_arrive(a.moves[i]):
                    a.board.update_piece_position(a.ids[i].position, a.arrive(a.ids[i]), 'R')
                else: a.ids[i].position = a.moves[i]
        
        a.moves =[]
        a.ids =[]
        a.turn = 'B'



if __name__ == "__main__":
    play()
                

