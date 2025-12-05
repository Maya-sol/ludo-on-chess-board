from ludopieces import Piece
from ludoconst import *
import random


class Board:
    def __init__(self):
        self.grid = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.first = [Piece('B',id) for id in range(1,5)]
        self.second = [Piece('R',id) for id in range(1,5)]

    def display(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                print(self.grid[i][j] + " ", end="")
            print()

    def is_valid_position(self, row, column):
        if(row == 0 or row == BOARD_SIZE - 1):
            return 0 <= column < BOARD_SIZE
        if(column == 0 or column == BOARD_SIZE - 1):
            return 0 <= row < BOARD_SIZE
        return False
    
    def is_empty(self, row, column):
        return self.grid[row][column] == '.'
    
    def get_piece_at(self, row, column):
        if self.is_valid_position(row, column) and not self.is_empty(row, column):
            for i in self.first:
                if i.position == (row,column):
                    return i
            for i in self.second:
                if i.position == (row, column):
                    return i
        return None
    
    def update_piece_position(self, old_position, new_position):
        old_row, old_col = old_position
        new_row, new_col = new_position

        if self.is_valid_position(old_row, old_col):
            i = self.get_piece_at(old_row, old_col)
            if i is not None:
                self.grid[old_row][old_col] = '.'
                self.grid[new_row][new_col] = i.symbol
                i.move(new_position)
            return True
        return False
    

