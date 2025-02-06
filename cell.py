from point import Point, Line


class Cell:
    def __init__(self, point_a, point_b, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = point_a.x
        self.y1 = point_a.y
        self.x2 = point_b.x
        self.y2 = point_b.y
        self._win = window

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        start_point = Point(self.x1 + ((self.x2 - self.x1) / 2), self.y1 + ((self.y2 - self.y1) / 2))
        end_point = Point(to_cell.x1 + ((to_cell.x2 - to_cell.x1) / 2), to_cell.y1 + ((to_cell.y2 - to_cell.y1) / 2))
        if undo:
            self._win.draw_line(Line(start_point, end_point), "grey")
        else:
            self._win.draw_line(Line(start_point, end_point), "red")
