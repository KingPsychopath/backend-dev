# Set-up
To install the packages listed in a `requirements.txt` file, you can use the `pip install -r` command. Here's how you can do it:

   ```bash
   pip install -r requirements.txt
   ```

This will install all the packages listed in the `requirements.txt` file, along with their specific versions.

If you're using a virtual environment (which is a good practice to isolate your project's dependencies), make sure to activate it before running the `pip install -r` command.

Remember, the `pip install -r` command reads the `requirements.txt` file line by line, and installs each package listed. The packages should be listed in the format `package==version`. If a package doesn't have a version number, `pip` will install the latest version.

# Flask

Uses Jinja2 Syntax for templating.
