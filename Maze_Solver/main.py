from maze import Window, Maze


def main():
    window = Window(800, 600)
    maze = Maze(
        5,
        5,
        15,
        15,
        50,
        50,
        window,
        seed=42,
    )

    maze.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()
