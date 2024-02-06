# Recursion on a tree

Recursion is often used in "tree-like" structures. For example, it's often used to iterate over nested Python dictionaries, classes that link to one another or files in a nested directory file system.

## Assignment

You're responsible for a module in Doc2Doc that can scan a file system (represented in our code as nested dictionaries) and list all the files by appending them to a list.

Complete the recursive `list_files` function:

```
Args:

- current_node (dict): Dictionary representing the file system (see the test suite)
- current_path (str): A string representing the current path (e.g. "root/dir1/dir2")

Returns:

- List[str]: A list of file paths
```

Use a `/` character to separate the directories in the path, including the root. For example, this:

```py
{
    "Documents": {
        "Proposal.docx": None,
    },
}
```

Has a path of `/Documents/Proposal.docx`.

## Instructions for writing the function

1. Create an empty list to store the file paths.
2. For each "node" in the current dictionary:
    1. If the node maps to `None`, add the full path for that node to the list.
    2. Otherwise, [extend](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) the file list with the results of calling `list_files` on the node. Be sure to update the current path to include the current node.
3. Return the list of file paths.