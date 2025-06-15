from tkinter import Tk, BOTH, Canvas
from time import sleep


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

    def draw(self, x_1, y_1, x_2, y_2):
        self.__x1 = x_1
        self.__y1 = y_1
        self.__x2 = x_2
        self.__y2 = y_2
        if self.__win != None:
            if self.has_left_wall:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_1, y_2)), "black")
            if self.has_top_wall:
                self.__win.draw_line(Line(Point(x_1, y_1), Point(x_2, y_1)), "black")
            if self.has_right_wall:
                self.__win.draw_line(Line(Point(x_2, y_1), Point(x_2, y_2)), "black")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(Point(x_1, y_2), Point(x_2, y_2)), "black")

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
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for col in range(self.__num_cols):
            cell_cols = []
            for row in range(self.__num_rows):
                cell = self.__draw_cell(col, row)
                cell_cols.append(cell)
            self.__cells.append(cell_cols)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell = Cell(self.__win)
        cell.draw(x1, y1, x2, y2)
        self.__animate()
        return cell

    def __animate(self):
        if self.__win != None:
            self.__win.redraw()
        sleep(0.05)
