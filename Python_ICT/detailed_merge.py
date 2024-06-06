import sys


def read_lines(file_a, file_b):
    """
    Merge two files line by line.

    Args:
        file_a (str): Path to the first file.
        file_b (str): Path to the second file.

    Returns:
        None

    This function reads two files line by line and writes merged lines to stdout.
    """
    with open(file_a, "r") as fa, open(file_b, "r") as fb:
        line_a = fa.readline()
        line_b = fb.readline()

        while line_a or line_b:
            if line_a:
                sys.stdout.write(line_a)
                line_a = fa.readline()
                if not line_a and line_b:
                    sys.stdout.write("\n")
            if line_b:
                sys.stdout.write(line_b)
                line_b = fb.readline()
                if not line_b and line_a:
                    sys.stdout.write("\n")
            sys.stdout.write("\n")


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 3:
        print(
            """Usage: python script.py <file_a> <file_b>
    Two paths are required"""
        )
        sys.exit(1)

    file_a = sys.argv[1]
    file_b = sys.argv[2]

    # exception handling
    try:
        read_lines(file_a, file_b)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        sys.exit(1)
