# DirTreeViz

DirTreeViz is a Python script that generates a directory tree in either ASCII or Markdown format. You can choose to display the tree in the console or save it to a file.

## Requirements

- Python 3.12

## Usage

### Display the directory tree in the console

To generate and display the directory tree in the console in ASCII format:

```sh
python directory_tree_generator.py /path/to/directory
```

To generate and display the directory tree in the console in Markdown format:

```sh
python directory_tree_generator.py /path/to/directory --markdown
```

### Save the directory tree to a file

To save the directory tree in ASCII format to a file:

```sh
python directory_tree_generator.py /path/to/directory --output output_file.txt
```

To save the directory tree in Markdown format to a file:

```sh
python directory_tree_generator.py /path/to/directory --output output_file.md --markdown
```

### Ignore specific directories and files

To generate the directory tree while ignoring specific directories and files:

```sh
python directory_tree_generator.py /path/to/directory --ignore __pycache__ node_modules
```

## Arguments

- `path`: The directory path for which to generate the tree.
- `-o` or `--output`: The output file where the tree will be written.
- `-m` or `--markdown`: Generate the tree in Markdown format.
- `-i` or `--ignore`: List of directories and files to ignore.

## Example

Generate and display the directory tree for the current directory in ASCII format:

```sh
python directory_tree_generator.py .
```

Generate and save the directory tree for `/home/user/docs` in Markdown format to `tree.md`:

```sh
python directory_tree_generator.py /home/user/docs --output tree.md --markdown
```

Generate the directory tree for `/home/user/docs`, ignoring the `__pycache__` and `node_modules` directories:

```sh
python directory_tree_generator.py /home/user/docs --ignore __pycache__ node_modules
```

### Zawartość repozytorium

```
dir_tree_viz/
├── directory_tree_generator.py
└── README.md
```
