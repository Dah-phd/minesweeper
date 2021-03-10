import random


class mine_field:
    def __init__(self):
        self.reset()

    def reset(self):
        self.alive = True
        self.board = [[(0, 0, 0) for _ in range(30)] for _ in range(16)]
        self.mines()
        self.add_numbers()

    def get_current(self):
        result = []
        for row in range(16):
            result.append([])
            for cell in range(30):
                result[row].append(self.board[row][cell][0]
                                   if self.board[row][cell][1] == 1 else 0)
        return result

    def boom(self):
        self.alive = False
        for n_row in range(16):
            for n_sq in range(30):
                if self.board[n_row][n_sq][0] == 'B':
                    self.board[n_row][n_sq] = ('B', 1, 0)

    def lock(self, row, square):
        if self.board[row][square][2] == 1:
            self.board[row][square] = (
                self.board[row][square][0], self.board[row][square][1], 0)
        else:
            self.board[row][square] = (
                self.board[row][square][0], self.board[row][square][1], 1)

    def onclick(self, row, square):
        if self.alive and self.board[row][square][1] == 0 and self.board[row][square][2] == 0:
            self.board[row][square] = (self.board[row][square][0], 1, 1)
            if self.board[row][square][0] == 'B':
                self.boom()
            elif self.board[row][square][0] == 0:
                if row != 0:
                    self.onclick(row-1, square)
                if row != 15:
                    self.onclick(row+1, square)
                if square != 0:
                    self.onclick(row, square-1)
                if square != 29:
                    self.onclick(row, square+1)
                if row != 0 and square != 0:
                    self.onclick(row-1, square-1)
                if row != 15 and square != 0:
                    self.onclick(row+1, square-1)
                if row != 0 and square != 29:
                    self.onclick(row-1, square+1)
                if row != 15 and square != 29:
                    self.onclick(row+1, square+1)

    def mines(self):
        n = 99
        while n > 0:
            row = random.randint(0, 15)
            col = random.randint(0, 29)
            if self.board[row][col][0] == 0:
                self.board[row][col] = ('B', 0, 0)
                n -= 1

    def add_numbers(self):
        for row in range(16):
            for cell in range(30):
                if self.board[row][cell][0] == 0:
                    self.board[row][cell] = (self.count_bombs(row, cell), 0, 0)

    def count_bombs(self, row, cell):
        count = 0
        if row != 0 and self.board[row-1][cell][0] == 'B':
            count += 1
        if row != 15 and self.board[row+1][cell][0] == 'B':
            count += 1
        if cell != 0 and self.board[row][cell-1][0] == 'B':
            count += 1
        if cell != 29 and self.board[row][cell+1][0] == 'B':
            count += 1
        if row != 0 and cell != 0 and self.board[row-1][cell-1][0] == 'B':
            count += 1
        if row != 15 and cell != 0 and self.board[row+1][cell-1][0] == 'B':
            count += 1
        if row != 0 and cell != 29 and self.board[row-1][cell+1][0] == 'B':
            count += 1
        if row != 15 and cell != 29 and self.board[row+1][cell+1][0] == 'B':
            count += 1
        return count
