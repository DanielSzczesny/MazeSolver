from window import Window
from maze import Maze


def main():
    win = Window(1200, 1200)
    maze = Maze(5, 5, 25, 25, 40, 40, win)

    maze.solve()

    win.wait_for_close()


main()
