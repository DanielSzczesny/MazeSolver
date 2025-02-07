import random
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
            win=None,
            seed=None
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
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

        self._break_walls_r(0, 0)
        self._reset_visited_status()

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
        self._draw_every_cell()

    def _draw_every_cell(self):
        for column in self._cells:
            for cell in column:
                cell.draw()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        if self.win is None:
            return
        self._cells[i][j].visited = True
        while True:
            next_to_visit = []
            if i + 1 < self.num_cols:
                if self._cells[i + 1][j] is not None and self._cells[i + 1][j].visited is False:
                    next_to_visit.append((i + 1, j))
            if i - 1 >= 0:
                if self._cells[i - 1][j] is not None and self._cells[i - 1][j].visited is False:
                    next_to_visit.append((i - 1, j))
            if j + 1 < self.num_rows:
                if self._cells[i][j + 1] is not None and self._cells[i][j + 1].visited is False:
                    next_to_visit.append((i, j + 1))
            if j - 1 >= 0:
                if self._cells[i][j - 1] is not None and self._cells[i][j - 1].visited is False:
                    next_to_visit.append((i, j - 1))

            if len(next_to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = random.randrange(len(next_to_visit))
                next_i, next_j = next_to_visit[direction]

                if next_i == i:
                    if next_j == j + 1:
                        self._cells[i][j].has_right_wall = False
                        self._cells[i][j + 1].has_left_wall = False
                        self._draw_cell(i, j)
                        self._draw_cell(i, j + 1)
                        self._break_walls_r(i, j + 1)
                    else:
                        self._cells[i][j - 1].has_right_wall = False
                        self._cells[i][j].has_left_wall = False
                        self._draw_cell(i, j)
                        self._draw_cell(i, j - 1)
                        self._break_walls_r(i, j - 1)
                elif next_j == j:
                    if next_i == i + 1:
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[i + 1][j].has_top_wall = False
                        self._draw_cell(i, j)
                        self._draw_cell(i + 1, j)
                        self._break_walls_r(i + 1, j)
                    else:
                        self._cells[i - 1][j].has_bottom_wall = False
                        self._cells[i][j].has_top_wall = False
                        self._draw_cell(i, j)
                        self._draw_cell(i - 1, j)
                        self._break_walls_r(i - 1, j)

    def _reset_visited_status(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        directions = []
        if (i + 1 < self.num_cols and
                self._cells[i + 1][j].visited is False and
                self._cells[i + 1][j].has_top_wall is False):
            directions.append((1, 0))
        if (i - 1 >= 0 and
                self._cells[i - 1][j].visited is False and
                self._cells[i - 1][j].has_bottom_wall is False):
            directions.append((-1, 0))
        if (j + 1 < self.num_rows and
                self._cells[i][j + 1].visited is False and
                self._cells[i][j + 1].has_left_wall is False):
            directions.append((0, 1))
        if (j - 1 >= 0 and
                self._cells[i][j - 1].visited is False and
                self._cells[i][j - 1].has_right_wall is False):
            directions.append((0, -1))
        for d in directions:
            add_i, add_j = d
            next_i = i + add_i
            next_j = j + add_j
            self._cells[i][j].draw_move(self._cells[next_i][next_j])
            result = self._solve_r(next_i, next_j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[next_i][next_j], True)
        return False

    def solve(self):
        result = self._solve_r(0, 0)
        if result:
            print("Solved!")
