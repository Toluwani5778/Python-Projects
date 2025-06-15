from maze import Window, Maze, Cell, Point, Line


def main():
    window = Window(800, 600)
    # point_1 = Point(100, 100)
    # point_2 = Point(250, 100)
    # point_3 = Point(250, 150)
    # point_4 = Point(300, 300)
    # line_1 = Line(point_1, point_2)
    # line_2 = Line(point_3, point_4)
    # window.draw_line(line_1, "black")
    # window.draw_line(line_2, "red")
    # cell_1 = Cell(window)
    # cell_1.draw(50, 50, 150, 150)
    # cell_2 = Cell(window)
    # cell_2.draw(50, 200, 150, 300)
    # cell_1.draw_move(cell_2)
    # cell_1.draw_move(cell_2, undo=True)
    maze = Maze(
        5,
        5,
        10,
        20,
        50,
        50,
        window,
        # seed=42,
    )
    # maze._Maze__break_entrance_and_exit()
    # for col in range(maze._Maze__num_cols):
    #     for row in range(maze._Maze__num_rows):
    #         maze._Maze__break_walls_r(col, row)
    window.wait_for_close()


if __name__ == "__main__":
    main()
