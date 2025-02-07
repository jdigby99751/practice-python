from JdPythonPractice.display_pattern import (
    left_sided_triangle as print_left_sided_triangle
)
from JdPythonPractice.display_pattern import (
    left_sided_triangle_reverse as print_left_sided_triangle_reverse
)


def print_half_diamond(n: int) -> None:
    print_left_sided_triangle.print_left_sided_triangle(n)
    print_left_sided_triangle_reverse.print_left_sided_triangle_reverse(n)


if __name__ == "__main__":
    print_half_diamond(5)
