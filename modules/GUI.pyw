# simple enough to make it single file
import pygame as pg
from logic import mine_field
import subprocess
import time
from sys import platform


class GUI:
    def __init__(self, box_side=40):
        self.box_side = box_side
        self.grid = pg.display.set_mode((30*box_side, 16*box_side+50))
        pg.display.set_caption('Minefield, by Dah')
        self.font = pg.font.SysFont('Courier New', 33, 'Bold')
        self.reset()

    def reset(self):
        self.field = mine_field()
        self.make_boxes()
        self.start = time.time()
        self.main()

    def make_boxes(self):
        self.boxes = []
        for row in range(16):
            self.boxes.append([])
            for cell in range(30):
                self.boxes[row].append((
                    pg.Rect(cell*self.box_side+1, row*self.box_side+1,
                            self.box_side-2, self.box_side-2),
                    row,
                    cell))

    def main(self):
        while True:
            self.grid.fill((0, 0, 0))
            self.draw()
            if not self.field.alive:
                self.end()
                return
            if self.field.win:
                self.end(True)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                self.controls(event)
            pg.display.update()

    def end(self, win=False):
        pg.display.update()
        if win:
            terminal(time.time() - self.start, 0)
        else:
            terminal(0, 1)
        time.sleep(5)

    def controls(self, event):
        for row in self.boxes:
            for box in row:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if box[0].collidepoint(event.pos):
                        if event.button == 1:
                            self.field.onclick(box[1], box[2])
                        elif event.button == 3:
                            self.field.lock(box[1], box[2])

    def draw(self):
        self.grid.blit(self.font.render(
            self.timer(), False, (30, 220, 30)), (60, 645))
        for row in self.boxes:
            for tup in row:
                if self.field.board[tup[1]][tup[2]][1] == 0:
                    if self.field.board[tup[1]][tup[2]][2] == 1:
                        pg.draw.rect(self.grid, (20, 200, 20), tup[0])
                    else:
                        pg.draw.rect(self.grid, (200, 200, 200), tup[0])
                elif self.field.board[tup[1]][tup[2]][1] == 1 and self.field.board[tup[1]][tup[2]][0] != 0:
                    self.grid.blit(self.font.render(
                        str(self.field.board[tup[1]][tup[2]][0]),
                        False, (30, 220, 30)),
                        (tup[0].x+10, tup[0].y))

    def timer(self):
        moment = time.time() - self.start
        mins = int(moment//60)
        secs = int(moment % 60)
        secs = ('0' + str(secs)) if secs < 10 else secs
        return f'{mins}:{secs}'


def terminal(new, lost):
    if platform[:3] == 'win':
        cmd = f'modules\\terminal.py {new} {lost}'
    else:
        cmd = f'python3 ./modules/terminal.py {new} {lost}'
    subprocess.Popen(
        f'modules\\terminal.py {new} {lost}', shell=True, creationflags=subprocess.DETACHED_PROCESS,
        stdin=None, stdout=None, stderr=None, close_fds=True)


if __name__ == '__main__':
    pg.init()
    game = GUI()
pg.quit()
