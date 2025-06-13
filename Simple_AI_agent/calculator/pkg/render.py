# render.py
import sys


def render(expression, result):
    if ("--verbose" in sys.argv) | ("-v" in sys.argv) | ("--debug" in sys.argv):
        print(f"Expression type: {type(expression)}")
        print(f"Result type: {type(result)}")
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)
    if ("--verbose" in sys.argv) | ("-v" in sys.argv) | ("--debug" in sys.argv):
        print(f"Result_str type: {type(result_str)}")

    box_width = max(len(expression), len(result_str)) + 4

    box = []
    box.append("┌" + "─" * box_width + "┐")
    box.append(
        "│" + " " * 2 + expression + " " * (box_width - len(expression) - 2) + "│"
    )
    box.append("│" + " " * box_width + "│")
    box.append("│" + " " * 2 + "=" + " " * (box_width - 3) + "│")
    box.append("│" + " " * box_width + "│")
    box.append(
        "│" + " " * 2 + result_str + " " * (box_width - len(result_str) - 2) + "│"
    )
    box.append("└" + "─" * box_width + "┘")
    return "\n".join(box)
