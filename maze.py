import time

from cell import Cell
from point import Point


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(0, self.num_cols):
            column = []
            for j in range(0, self.num_rows):
                point_a = Point(self.x1 + (self.cell_size_x * j), self.y1 + (self.cell_size_y * i))
                point_b = Point(self.x1 + self.cell_size_x + (self.cell_size_x * j),
                                self.y1 + self.cell_size_y + (self.cell_size_y * i))
                cell = Cell(point_a, point_b, self.win)
                column.append(cell)
            self._cells.append(column)
        self._draw_cell()

    def _draw_cell(self):
        for column in self._cells:
            for cell in column:
                cell.draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell()
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell()
