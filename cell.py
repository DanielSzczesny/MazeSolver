from point import Point, Line


class Cell:
    def __init__(self, point_a, point_b, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = point_a.x
        self.y1 = point_a.y
        self.x2 = point_b.x
        self.y2 = point_b.y
        self._win = window
        self.visited = False

    def draw(self):
        if self._win is None:
            return

        line_left = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        line_right = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        line_top = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        line_bottom = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))

        self._win.draw_line(line_left, "white")
        if self.has_left_wall:
            self._win.draw_line(line_left)
        self._win.draw_line(line_right, "white")
        if self.has_right_wall:
            self._win.draw_line(line_right)
        self._win.draw_line(line_top, "white")
        if self.has_top_wall:
            self._win.draw_line(line_top)
        self._win.draw_line(line_bottom, "white")
        if self.has_bottom_wall:
            self._win.draw_line(line_bottom)

    def draw_move(self, to_cell, undo=False):
        start_point = Point(self.x1 + ((self.x2 - self.x1) / 2), self.y1 + ((self.y2 - self.y1) / 2))
        end_point = Point(to_cell.x1 + ((to_cell.x2 - to_cell.x1) / 2), to_cell.y1 + ((to_cell.y2 - to_cell.y1) / 2))
        if undo:
            self._win.draw_line(Line(start_point, end_point), "grey")
        else:
            self._win.draw_line(Line(start_point, end_point), "red")
