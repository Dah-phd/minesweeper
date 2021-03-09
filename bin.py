# simple enough to make it single file
import pygame as pg
from modules.logic import mine_field


class GUI:
    def __init__(self, box_side=40):
        self.box_side = box_side
        self.grid = pg.display.set_mode((30*box_side, 16*box_side))
        pg.display.set_caption('Python on python, by Dah')
        self.font = pg.font.SysFont('Times New Roman', 33)
        self.setup()

    def setup(self):
        while True:
            self.grid.fill((0, 0, 0))
            self.grid.blit(self.font.render('Press Enter to start!',
                                            True, (255, 255, 255)), (100, 100))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            if pg.key.get_pressed()[pg.K_RETURN]:
                print('here')
                self.reset()
                return
            pg.display.update()

    def reset(self):
        self.field = mine_field()
        self.main()

    def main(self):
        while True:
            self.grid.fill((0, 0, 0))
            self.draw()
            if not self.field.alive:
                self.end()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            pg.display.update()

    def end(self):
        pass

    def draw(self):
        for n_row, row in enumerate(self.field.board):
            for n_cell, cell in enumerate(row):
                if cell[1] == 0:
                    pg.draw.rect(self.grid,
                                 (30, 30, 30),
                                 (n_row*self.box_side, n_cell *
                                  self.box_side, self.box_side, self.box_side),
                                 )
                elif cell[1] == 1:
                    pass


if __name__ == '__main__':
    pg.init()
    game = GUI()
pg.quit()
