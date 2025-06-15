import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_small_maze(self):
        num_cols = 2
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)

    def test_large_maze(self):
        num_cols = 20
        num_rows = 20
        m3 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)

    def test_wide_maze(self):
        num_cols = 20
        num_rows = 5
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m4._Maze__cells), num_cols)
        self.assertEqual(len(m4._Maze__cells[0]), num_rows)

    def test_tall_maze(self):
        num_cols = 5
        num_rows = 20
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m5._Maze__cells), num_cols)
        self.assertEqual(len(m5._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m._Maze__cells[0][0]
        exit_cell = m._Maze__cells[num_cols - 1][num_rows - 1]

        # Entrance should have no top wall
        self.assertFalse(
            entrance_cell.has_top_wall, "Entrance cell should not have a top wall"
        )

        # Exit should have no bottom wall
        self.assertFalse(
            exit_cell.has_bottom_wall, "Exit cell should not have a bottom wall"
        )

    def test_reset_cells_visited(self):
        num_cols = 4
        num_rows = 4
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Manually set some cells as visited
        for col in m._Maze__cells:
            for cell in col:
                cell.visited = True  # Simulate visitation

        # Now call the reset method
        m._Maze__reset_cells_visited()

        # Check that all cells are now marked as not visited
        for col in m._Maze__cells:
            for cell in col:
                self.assertFalse(
                    cell.visited, "Cell visited flag should be reset to False"
                )


if __name__ == "__main__":
    unittest.main()
