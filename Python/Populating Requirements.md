To automatically create and populate a `requirements.txt` file for your Python projects, you can use the `pip freeze` command, which outputs all installed packages and their versions in your current Python environment. Here's how you can do it:

1. Activate your project's virtual environment. This step is important to ensure that the `requirements.txt` file only includes the packages that are relevant to your project, not all packages installed in your global Python environment.

   ```bash
   # For venv
   source path_to_your_venv/bin/activate

   # For conda
   conda activate your_env_name
   ```

   Replace `path_to_your_venv` and `your_env_name` with the actual path to your venv directory and the name of your conda environment, respectively.

2. Run the `pip freeze` command and redirect its output to a `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

This will create a `requirements.txt` file in the current directory and populate it with a list of all installed packages and their versions.

Remember to run these steps every time you install a new package or update a package version, so that your `requirements.txt` file stays up-to-date.

If you want to automate this process, you could create a script that activates the virtual environment, installs packages, and updates the `requirements.txt` file. However, this would require some knowledge of shell scripting and might not be suitable for all projects.