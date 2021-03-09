# simple enough to make it single file
import pygame as pg
from modules.logic import mine_field


class GUI:
    def __init__(self, box_side=40):
        self.box_side = box_side
        self.grid = pg.display.set_mode((30*box_side, 16*box_side+50))
        pg.display.set_caption('Minefield, by Dah')
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
                self.reset()
                return
            pg.display.update()

    def reset(self):
        self.field = mine_field()
        self.make_boxes()
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
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                self.controls(event)
            pg.display.update()

    def end(self):
        self.setup()

    def controls(self, event):
        for row in self.boxes:
            for box in row:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if box[0].collidepoint(event.pos):
                        print('a')
                        self.field.onclick(box[1], box[2])

    def draw(self):
        for row in self.boxes:
            for tup in row:
                if self.field.board[tup[1]][tup[2]][1] == 0:
                    pg.draw.rect(self.grid, (200, 200, 200), tup[0])
                elif self.field.board[tup[1]][tup[2]][1] == 1:
                    self.grid.blit(self.font.render(
                        str(self.field.board[tup[1]][tup[2]][0]),
                        True, (255, 255, 255)),
                        (tup[0].x+5, tup[0].y))


if __name__ == '__main__':
    pg.init()
    game = GUI()
pg.quit()
