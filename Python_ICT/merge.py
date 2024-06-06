import sys


def read_lines(file_a, file_b):
    """
    2つのテキストファイルのパスを受け取り、それらを結合して出力する関数
    """
    with open(file_a, "r") as fa, open(file_b, "r") as fb:
        line_a = fa.readline()
        line_b = fb.readline()

        while line_a or line_b:
            if line_a:
                sys.stdout.write(line_a)
                line_a = fa.readline()
            if line_b:
                sys.stdout.write(line_b)
                line_b = fb.readline()
            sys.stdout.write("\n")


if __name__ == "__main__":
    # コマンドライン引数の個数をチェック
    if len(sys.argv) != 3:
        print(
            """Usage: python script.py <file_a> <file_b>
    Two paths are required"""
        )
        sys.exit(1)

    file_a = sys.argv[1]
    file_b = sys.argv[2]

    # 例外処理
    try:
        read_lines(file_a, file_b)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        sys.exit(1)
