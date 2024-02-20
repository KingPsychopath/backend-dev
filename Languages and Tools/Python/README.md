# Python Study Materials

This directory contains all of my study materials for the Python programming as well as personal projects created during self-learning.

## Contents

- **Projects**: This folder contains Python projects created by myself during self-learning
- **Practice**: This folder contains Python scripts demonstrating various concepts and techniques for practice
- **Notes**: This folder contains notes on Python programming.

## Usage

Each subdirectory in this directory corresponds to a different type of material (scripts, exercises, or notes). Inside each subdirectory, you'll find relevant Python files and a `README.md` file with more information.

1. Activate your project's virtual environment. This step is important to ensure that the `requirements.txt` file only includes the packages that are relevant to your project, not all packages installed in your global Python environment.

   ```bash
   # For venv
   source path_to_your_venv/bin/activate
   ```

## Requirements

These materials were created using Python 3. Make sure you have Python 3 installed and set as your default Python interpreter.

### Installing and Saving Dependencies

To automatically create and populate a `requirements.txt` file for your Python projects, you can use the `pip freeze` command, which outputs all installed packages and their versions in your current Python environment.

1. Run the `pip freeze` command and redirect its output to a `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

This will create a `requirements.txt` file in the current directory and populate it with a list of all installed packages and their versions.

Remember to run these steps every time you install a new package or update a package version, so that your `requirements.txt` file stays up-to-date.

**Installing packages from a `requirements.txt` file**
To install all the packages listed in a `requirements.txt` file, you can use the `pip install` command with the `-r` flag, followed by the path to the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Contributing

This is a personal study repository so I'm not currently accepting contributions. However, if you find any errors or have any suggestions, feel free to open an issue.

## License

This project is licensed under the terms of the MIT license.
