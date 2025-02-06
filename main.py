from window import Window
from point import Point, Line

def main():
    win = Window(800, 600)
    line_a = Line(Point(20, 20), Point(60, 20))
    line_b = Line(Point(40, 40), Point(40, 60))
    win.draw_line(line_a, "black")
    win.draw_line(line_b, "red")
    win.wait_for_close()

main()
