import random


class mine_field:
    def __init__(self):
        self.board = [[0 for _ in range(30)] for _ in range(16)]
        self.mines()
        self.add_numbers()

    def mines(self):
        n = 99
        while n > 0:
            row = random.randint(0, 15)
            col = random.randint(0, 29)
            if self.board[row][col] == 0:
                self.board[row][col] = 'B'
                n -= 1

    def add_numbers(self):
        for row in range(16):
            for cell in range(30):
                if self.board[row][cell] == 0:
                    self.board[row][cell] = self.count_bombs(row, cell)

    def count_bombs(self, row, cell):
        count = 0
        if row != 0 and self.board[row-1][cell] == 'B':
            count += 1
        if row != 15 and self.board[row+1][cell] == 'B':
            count += 1
        if cell != 0 and self.board[row][cell-1] == 'B':
            count += 1
        if cell != 29 and self.board[row][cell+1] == 'B':
            count += 1
        if row != 0 and cell != 0 and self.board[row-1][cell-1] == 'B':
            count += 1
        if row != 15 and cell != 0 and self.board[row+1][cell-1] == 'B':
            count += 1
        if row != 0 and cell != 29 and self.board[row-1][cell+1] == 'B':
            count += 1
        if row != 15 and cell != 29 and self.board[row+1][cell+1] == 'B':
            count += 1
        return count


if __name__ == '__main__':
    new = mine_field()
    for row in new.board:
        print(row)
