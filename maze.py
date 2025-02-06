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
            win
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
        for column in self._cells:
            for cell in column:
                cell.draw()
