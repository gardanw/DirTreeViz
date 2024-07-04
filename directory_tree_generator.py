import argparse
import os
from typing import List


def generate_tree(
    path: str,
    prefix: str = "",
    is_last: bool = True,
    markdown: bool = False,
    is_root: bool = True,
    ignore: List[str] | None = None,
) -> List[str]:
    """
    Generate a directory tree in ASCII or Markdown format.

    Args:
        path (str): The directory path for which to generate the tree.
        prefix (str): The prefix to add before each line (used for recursion).
        is_last (bool): Whether the current directory is the last in its parent directory.
        markdown (bool): Whether to format the tree in Markdown (default is ASCII).
        is_root (bool): Whether the current directory is the root directory.
        ignore (List[str]): List of directories and files to ignore.

    Returns:
        List[str]: A list of strings representing the directory tree.
    """
    if ignore is None:
        ignore = []
    tree = []
    if is_root:
        tree.append(f"{os.path.basename(os.path.abspath(path))}{"/" if os.path.isdir(path) else ""}")
    else:
        connector = (
            "├── "
            if not is_last
            else "└── "
            if markdown
            else "|-- "
            if not is_last
            else "`-- "
        )
        tree.append(f"{prefix}{connector}{os.path.basename(path)}{"/" if os.path.isdir(path) else ""}")
        prefix += "    " if is_last else "|   "

    children = sorted([child for child in os.listdir(path) if child not in ignore])
    for index, child in enumerate(children):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            tree.extend(
                generate_tree(
                    child_path,
                    prefix,
                    index == len(children) - 1,
                    markdown,
                    is_root=False,
                    ignore=ignore
                )
            )
        else:
            connector = (
                "├── "
                if index != len(children) - 1
                else "└── "
                if markdown
                else "|-- "
                if index != len(children) - 1
                else "`-- "
            )
            tree.append(f"{prefix}{connector}{child}{"/" if os.path.isdir(child) else ""}")

    return tree


def write_tree(path: str, output_file: str, markdown: bool = False, ignore: List[str] | None = None) -> None:
    """
    Generate a directory tree and write it to a file.

    Args:
        path (str): The directory path for which to generate the tree.
        output_file (str): The output file where the tree will be written.
        markdown (bool): Whether to format the tree in Markdown (default is ASCII).
        ignore (List[str]): List of directories and files to ignore.
    """
    if ignore is None:
        ignore = []
    tree = generate_tree(path, markdown=markdown, ignore=ignore)
    with open(output_file, "w", encoding='utf-8') as f:
        if output_file.endswith(".md"):
            f.write("```\n" + "\n".join(tree) + "\n```\n")
        else:
            f.write("\n".join(tree))
            f.write("\n")


def print_tree(path: str, markdown: bool = False, ignore: List[str] | None = None) -> None:
    """
    Generate a directory tree and print it to the console.

    Args:
        path (str): The directory path for which to generate the tree.
        markdown (bool): Whether to format the tree in Markdown (default is ASCII).
        ignore (List[str]): List of directories and files to ignore.
    """
    if ignore is None:
        ignore = []
    tree = generate_tree(path, markdown=markdown, ignore=ignore)
    for line in tree:
        print(line)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a directory tree in ASCII or Markdown format."
    )
    parser.add_argument(
        "path",
        type=str,
        help="The directory path for which to generate the tree.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="The output file where the tree will be written.",
    )
    parser.add_argument(
        "-m",
        "--markdown",
        action="store_true",
        help="Generate the tree in Markdown format.",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        type=str,
        nargs='*',
        default=[],
        help="List of directories and files to ignore.",
    )

    args = parser.parse_args()
    if args.output:
        write_tree(args.path, args.output, markdown=args.markdown, ignore=args.ignore)
    else:
        print_tree(args.path, markdown=args.markdown, ignore=args.ignore)


if __name__ == "__main__":
    main()
