Refreshing my mind of Java


# Bash Auto-Completion

To enable auto-completion for `java` and `javac` commands in your Bash shell, you need to install bash-completion scripts for these commands. However, unlike Docker or Git, Java does not provide official bash-completion scripts.

You can create a simple bash-completion script for `java` and `javac` commands that auto-completes filenames with `.java` and `.class` extensions. Here's how you can do it:

1. Open a new file in the `/etc/bash_completion.d/` directory named `java_completion`:

   ```bash
   sudo nano /etc/bash_completion.d/java_completion
   ```

2. Add the following lines to the file:

   ```bash
   _java_completion() {
       local cur=${COMP_WORDS[COMP_CWORD]}
       COMPREPLY=( $(compgen -f -X '!*.@(java|class)' -- $cur) )
   }
   complete -F _java_completion java javac
   ```

   This script defines a function `_java_completion` that generates completion replies (`COMPREPLY`) for filenames ending with `.java` or `.class`. The `complete -F _java_completion java javac` line registers this function as the completion function for `java` and `javac` commands.

3. Save the file and exit the text editor.

4. Apply the changes by sourcing the bash-completion file:

   ```bash
   source /etc/bash_completion
   ```

Now, when you type `java ` or `javac ` and then start typing a filename and hit `Tab`, it should auto-complete filenames ending with `.java` or `.class`.

Please note that this is a very basic completion script. It only completes filenames, not command options or class names. Writing a script that completes command options or class names would be much more complex and beyond the scope of this guide.