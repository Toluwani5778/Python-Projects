from tkinter import Tk, BOTH, Canvas
from time import sleep
import random


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Resizable Window")

        self.canvas = Canvas(self.__root, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.window_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x_1, y_1, x_2, y_2):
        self.__x1 = x_1
        self.__y1 = y_1
        self.__x2 = x_2
        self.__y2 = y_2
        if self.__win != None:
            if self.has_left_wall:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_1, y_2)), "black")
            else:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_1, y_2)), "white")
            if self.has_top_wall:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_2, y_1)), "black")
            else:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_2, y_1)), "white")
            if self.has_right_wall:
                self.__win.draw_line(Line(Point(x_2, y_1), Point(x_2, y_2)), "black")
            else:
                self.__win.draw_line(Line(Point(x_2, y_1), Point(x_2, y_2)), "white")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(Point(x_1, y_2), Point(x_2, y_2)), "black")
            else:
                self.__win.draw_line(Line(Point(x_1, y_2), Point(x_2, y_2)), "white")

    def draw_move(self, to_cell, undo=False):
        if self.__win != None:
            if not undo:
                self.__win.draw_line(
                    Line(self.midpoint(), to_cell.midpoint()),
                    "red",
                )

            else:
                self.__win.draw_line(
                    Line(self.midpoint(), to_cell.midpoint()),
                    "gray",
                )

    def midpoint(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)


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
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = random.seed(seed) if seed is not None else None
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for col in range(self.__num_cols):
            cell_cols = []
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                self.__draw_cell(cell, col, row)
                cell_cols.append(cell)
            self.__cells.append(cell_cols)

    def __draw_cell(self, cell, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win != None:
            self.__win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(self.__cells[0][0], 0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(
            self.__cells[self.__num_cols - 1][self.__num_rows - 1],
            self.__num_cols - 1,
            self.__num_rows - 1,
        )

    def __break_walls_r(self, i, j):
        cell = self.__cells[i][j]
        cell.visited = True
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while True:
            cells_to_visit = []
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < self.__num_cols and 0 <= nj < self.__num_rows:
                    neighbor_cell = self.__cells[ni][nj]
                    if not neighbor_cell.visited:
                        cells_to_visit.append((ni, nj))
            if not cells_to_visit:
                cell.draw(
                    self.__x1 + i * self.__cell_size_x,
                    self.__y1 + j * self.__cell_size_y,
                    self.__x1 + (i + 1) * self.__cell_size_x,
                    self.__y1 + (j + 1) * self.__cell_size_y,
                )
                return
            else:
                ni, nj = random.choice(cells_to_visit)
                # print(f"Breaking walls between ({i}, {j}) and ({ni}, {nj})")
                self.__break_walls(cell, self.__cells[ni][nj])
                self.__draw_cell(cell, i, j)
                self.__draw_cell(self.__cells[ni][nj], ni, nj)
                self.__animate()
                self.__break_walls_r(ni, nj)

    def __break_walls(self, cell1, cell2):
        if cell1.midpoint().x < cell2.midpoint().x:
            cell1.has_right_wall = False
            cell2.has_left_wall = False
        elif cell1.midpoint().x > cell2.midpoint().x:
            cell1.has_left_wall = False
            cell2.has_right_wall = False
        elif cell1.midpoint().y < cell2.midpoint().y:
            cell1.has_bottom_wall = False
            cell2.has_top_wall = False
        elif cell1.midpoint().y > cell2.midpoint().y:
            cell1.has_top_wall = False
            cell2.has_bottom_wall = False

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False
