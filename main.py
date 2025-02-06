from window import Window
from point import Point, Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 20, 20, 20, 20, win)

    win.wait_for_close()


main()
