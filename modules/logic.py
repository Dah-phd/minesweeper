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

    def _massclick(self, row, square, limit=False):
        if row != 0:
            self.onclick(row-1, square, limit=limit)
        if row != 15:
            self.onclick(row+1, square, limit=limit)
        if square != 0:
            self.onclick(row, square-1, limit=limit)
        if square != 29:
            self.onclick(row, square+1, limit=limit)
        if row != 0 and square != 0:
            self.onclick(row-1, square-1, limit=limit)
        if row != 15 and square != 0:
            self.onclick(row+1, square-1, limit=limit)
        if row != 0 and square != 29:
            self.onclick(row-1, square+1, limit=limit)
        if row != 15 and square != 29:
            self.onclick(row+1, square+1, limit=limit)

    def onclick(self, row, square, limit=False):
        if self.alive:
            print(self.board[row][square][0])
            if self.board[row][square][1] == 0 and self.board[row][square][2] == 0:
                self.board[row][square] = (self.board[row][square][0], 1, 0)
                if self.board[row][square][0] == 'B':
                    self.boom()
                elif self.board[row][square][0] == 0:
                    self._massclick(row, square)
            elif self.board[row][square][1] == 1 and self.board[row][square][0] != 0 and not limit:
                locked = self.counter(row, square, location=2, value=1)
                if locked == self.board[row][square][0]:
                    unopened = self.counter(
                        row, square, location=1, value=0) - locked
                    print('up', unopened)
                    if unopened > 0:
                        self._massclick(row, square, limit=True)
        return

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
                    self.board[row][cell] = (self.counter(row, cell), 0, 0)

    def counter(self, row, cell, location=0, value='B'):
        count = 0
        if row != 0 and self.board[row-1][cell][location] == value:
            count += 1
        if row != 15 and self.board[row+1][cell][location] == value:
            count += 1
        if cell != 0 and self.board[row][cell-1][location] == value:
            count += 1
        if cell != 29 and self.board[row][cell+1][location] == value:
            count += 1
        if row != 0 and cell != 0 and self.board[row-1][cell-1][location] == value:
            count += 1
        if row != 15 and cell != 0 and self.board[row+1][cell-1][location] == value:
            count += 1
        if row != 0 and cell != 29 and self.board[row-1][cell+1][location] == value:
            count += 1
        if row != 15 and cell != 29 and self.board[row+1][cell+1][location] == value:
            count += 1
        return count
