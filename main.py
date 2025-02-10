import sys
from filesystem_builder import build_filesystem_tree

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
        return

    path = sys.argv[1]
    try:
        root = build_filesystem_tree(path)
        root.draw()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()