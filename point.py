class Point:
    def __init__(self, x=0, y=0):
        """
        Point class
        :param x: x=0 is the left of the screen
        :param y: y=0 is the top of the screen
        """
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2
        )
