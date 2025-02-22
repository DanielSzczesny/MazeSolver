import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_large(self):
        num_cols = 100
        num_rows = 250
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows
        )

    def test_maze_entrance_exit_ready(self):
        num_cols = 10
        num_rows = 25
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m3._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m3._cells[-1][-1].has_bottom_wall,
            False
        )

    def test_cell_visited_status_reset(self):
        num_cols = 10
        num_rows = 25
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m4._cells[0][0].visited,
            False
        )
        self.assertEqual(
            m4._cells[1][1].visited,
            False
        )


if __name__ == "__main__":
    unittest.main()
