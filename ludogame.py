from ludoboard import *
from ludopieces import Piece
from ludoconst import *

class Ludo:
    def __init__(self):
        self.board = Board()
        self.dice = 0
        self.turn = 'B'
        self.winner = None
        self.moves = []
        self.ids = []

    def check_start (self):
        if(self.turn == 'B' and self.dice == 6):
            p = self.board.get_piece_at(0,0)
            if p is None or p.symbol != 'B':
                for i in self.board.first:
                    if(i.position == (-1,-1)):
                        self.ids.append(i)
                        return True
        elif (self.turn == 'R' and self.dice == 6):
            p = self.board.get_piece_at(7,7)
            if p is None or p.symbol != 'R':
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
            d = self.moving_directon((old_row, old_col))
            old_row += d[0]
            old_col += d[1] 
            if self.board.get_piece_at(old_row, old_col) is not None:
                return(-1, -1)
            if self.turn == 'B':
                if old_row == 0 and old_col == 0:
                    return (-1,-1)
            elif self.turn == 'R':
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
            p = self.board.get_piece_at(0,0)
            if p is not None and p.symbol == 'R': 
                p.move((-1,-1))
            self.ids[0].position = (0,0)
            self.board.grid[0][0] = 'B'
            return
        if self.turn == 'R':
            p = self.board.get_piece_at(7,7)
            if p is not None and p.symbol == 'B': 
                p.move((-1,-1))
            self.ids[0].position = (7,7)
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

    def arrive (self):
        if self.turn == 'B':
            row, col = (3,3)
            for i in range(3):
                if self.board.grid[row][col] == '.':
                    self.board.grid[row][col] = 'B'
                    return (row,col)
                row -= 1
                col -= 1
            if (row==0):
                    self.winner = 'Blue'
                    return (row,col)
        elif self.turn == 'R':
            row, col = (4,4)
            for i in range(3):
                if self.board.grid[row][col] == '.':
                    self.board.grid[row][col] = 'R'
                    return (row,col)
                row += 1
                col += 1
            if (row==7):
                    self.winner = 'Red'
                    return (row,col)
        return
    
    def check_win(self):
        if self.winner is not None:
            return True
        return False
    
    def remove(self, position):
            if self.turn == 'B':
                for i in self.board.first:
                    if i.position == position:
                        self.board.first.remove(i)
            else:
                for i in self.board.second:
                    if i.position == position:
                        self.board.second.remove(i)
            
def play():
    a = Ludo()
    while True:
        a.board.display()
        print(a.roll())
        a.get_valid_moves()
        print(a.moves)
        if a.moves:
            print(a.turn)
            #i = int(input("choose number of move: "))
            i = 0
            if (a.moves[i] == 'start'):
                a.start()
            else:
                removed = a.board.get_piece_at(a.moves[i][0], a.moves[i][1])
                if removed is not None:
                    removed.move((-1 , -1))
                a.board.update_piece_position(a.ids[i].position, a.moves[i])
                if a.check_arrive(a.moves[i]):
                    removed = a.arrive()
                    a.board.update_piece_position((0,0), removed)
                    a.remove(removed)
                    if a.check_win():
                        print(a.winner)
                        break
                else: a.ids[i].move(a.moves[i])
        a.moves =[]
        a.ids =[]
        a.board.display()
        a.turn = 'R'
        print(a.roll())
        a.get_valid_moves()
        print(a.moves)
        if a.moves:
            print(a.turn)
           # i = int(input("choose number of move: "))
            i = 0
            if (a.moves[i] == 'start'):
                a.start()
            else:
                removed = a.board.get_piece_at(a.moves[i][0], a.moves[i][1])
                a.board.update_piece_position(a.ids[i].position, a.moves[i])
                if removed is not None:
                    removed.move((-1 , -1))
                if a.check_arrive(a.moves[i]):
                    removed = a.arrive()
                    a.board.update_piece_position((7,7), removed)
                    a.remove(removed)
                    if a.check_win():
                        print(a.winner)
                        break
                else: a.ids[i].position = a.moves[i]
        
        a.moves =[]
        a.ids =[]
        a.turn = 'B'
    a.board.display()



if __name__ == "__main__":
    play()
                

