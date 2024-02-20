# Install

```bash
sudo apt get install git 
sudo apt get install gh # Install Github CLI

gh auth login # authenticate with account - prefer HTTPS

git config --global user.name "Your Name" # Set-up local username and email
git config --global user.email "your-email@example.com" 

```

The `--global` option applies these settings to all repositories on your computer. If you want to set the username and email for a specific repository only, navigate to that repository in your command line and run the commands without the `--global` option.
# Basics

Here are some basic Git commands that every beginner should know:

1. `git init`: Initializes a new Git repository. This creates a new `.git` directory in your current directory.
2. `git clone <url>`: Clones a repository from the given URL, which can be a path on your local filesystem or a URL to a remote repository.
3. `git status`: Shows the status of changes in the current repository. This includes changes that are staged, not yet staged, and untracked.
4. `git add <file>`: Adds a file to the staging area in preparation for a commit. You can use `git add .` to add all changes in the directory.
5. `git commit -m "<message>"`: Commits the staged changes to the repository with a descriptive message.
6. `git push <remote> <branch>`: Pushes your commits to the specified remote repository and branch. If you cloned a repository, the remote is typically called `origin`.
7. `git pull <remote> <branch>`: Fetches changes from the specified remote repository and branch, and merges them into your current branch.
8. `git branch`: Lists all branches in your repository. The current branch is indicated with an asterisk.
9. `git checkout <branch>`: Switches to the specified branch. If the branch doesn't exist, you can create it with `git checkout -b <branch>`.
10. `git merge <branch>`: Merges the specified branch into the current branch.
11. `git log`: Shows a log of all commits in the current branch.
12. `git fetch`: Downloads commits, files and refs from remote repository into local repository. It fetches all the changes that have been made in the remote repository that do not yet exist in your local repository, without merging. 

In the context of Git, a `remote` is a version of your project that is hosted on the internet or network somewhere. It's "remote" in the sense that it's not on your local machine. When you clone a repository from a hosting service like GitHub, Git automatically names this remote repository `origin`.

A `branch` is a parallel version of a repository. It is contained within the repository, but does not affect the primary or `main` branch allowing you to work freely without disrupting the live version. When you've made the changes you want to make, you can merge your branch back into the `main` branch to publish your changes.


# Branches

In Git, a branch is essentially a unique set of code changes with a unique name. Each repository can have one or more branches. The main branch (historically known as `master`) is the "default" branch when you create a repository. Use other branches for development and merge them back to the main branch upon completion.

Here are a few more things to know about branches:

- **Creating branches**: Create a new branch and switch to it with `git checkout -b`.
- **Switching branches**: You can switch to an existing branch with `git checkout <branch>`.
- **Merging branches**: You can merge changes from one branch into another with `git merge <branch>`. This is typically done to merge changes from a development branch into the main branch.
- **Deleting branches**: You can delete an existing branch with `git branch -d your-branch-name` (`-D` is for force delete and `-d` is for safe delete)
- **Viewing branches**: You can view all branches in your repository with `git branch`. The current branch will be indicated with an asterisk

## Creating Branches

To create a new branch in Git and switch to it, you can use the `git checkout` command with the `-b` option. The `-b` option tells Git to create a new branch if it doesn't already exist.

## Deleting Branches

To delete a branch in Git, you can use the `git branch` command with the `-d` option for a safe delete or `-D` for a force delete.

Safe delete will only delete the branch if it has been fully merged in its upstream branch or in `HEAD`. If you're sure you want to delete the branch and you don't care about losing changes, you can use the `-D` option to force delete the branch:

Please note that you cannot delete a branch that you're currently on. You'll need to switch to a different branch before you can delete the branch. You can switch to the `main` branch with `git checkout main`.

# Fetching/Updating Branches

`git fetch` is a command used to download commits, files, and refs from a remote repository into your local repository. It fetches all the changes that have been made in the remote repository that do not yet exist in your local repository.

However, `git fetch` does not merge any changes into your current working branch. It only downloads the changes. This allows you to review the changes before integrating them into your local branches.

You should use `git fetch` when you want to see if there have been any updates to the remote repository without making any changes to your local working directory. This is useful when you're working in a team and want to get the latest changes that your teammates have pushed, or when you want to check the status of your remote branches.

Here's how you can use `git fetch`:

```bash
git fetch origin
```

This command fetches all the changes from the `origin` remote. You can then inspect the changes with `git log` or `git diff`.

If you want to integrate the changes into your local branch, you can use `git merge` or `git pull` (which is a combination of `git fetch` and `git merge`).

## Merging Branches
Merging is a common practice when working with Git and it's used to integrate changes from one branch into another. Here's a typical workflow for merging:

1. **Check out the branch you want to merge into**: This will usually be your main or master branch.

   ```bash
   git checkout main
   ```

2. **Pull the latest changes from the remote repository**: This ensures you're working with the latest code.

   ```bash
   git pull origin main
   ```

3. **Merge the branch you want**: Replace `<branch-name>` with the name of the branch you want to merge.

   ```bash
   git merge <branch-name>
   ```

4. **Resolve any merge conflicts**: If there are conflicts between the branches, Git will tell you and you'll need to resolve them manually. Open the files with conflicts, look for the conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`), decide which changes to keep, and remove the conflict markers.

5. **Commit the merge**: If there were conflicts, you'll need to commit the merge manually.

   ```bash
   git commit -m "Merged <branch-name> into main"
   ```

6. **Push the merge to the remote repository**: This updates the remote repository with the merge.

   ```bash
   git push origin main
   ```

> [!NOTE]
> Note: It's a good practice to pull the latest changes from the remote repository before starting a merge to minimize the chances of conflicts.


The `git merge` command is a local operation. It merges changes from one branch in your local repository into another branch in your local repository. If you want to merge changes from a remote branch, you would typically `git fetch` or `git pull` the changes from the remote repository to your local repository first, and then perform the merge.

## Undoing a Merge
If you've recently merged a branch in Git and want to undo it, you can use the `git reset` command if you want to completely discard the merge, or the `git revert` command if you want to keep the history of the merge but undo the changes it introduced.

Remember, both of these options will alter your local repository. If you've already pushed the merge to a remote repository, you'll need to force push your changes with `git push -f`. Be careful with this, as it can overwrite changes in the remote repository.

### Git Reset

   - **Use `git reset` to move your `HEAD` pointer back to the commit before the merge**. This effectively "undoes" the merge, but it also discards all commits that were made after the specified commit. Here's how you can do it:

     ```bash
     git reset --hard <commit-hash>
     ```

 Replace `<commit-hash>` with the hash of the commit before the merge. You can find this hash with `git log`.

- This command will move the `HEAD` pointer back to the commit before the merge. This effectively "undoes" the merge, but it also discards the merge from the history.

```bash
git reset --hard HEAD~1
```

This command moves the `HEAD` and the branch pointer to the commit before the current one (indicated by `HEAD~1`).

### ### Git Revert

   - **Use `git revert` to create a new commit that undoes the merge**. This is a safer option because it doesn't alter the existing commit history. Here's how you can do it:

     ```bash
     git revert -m 1 <merge-commit-hash>
     ```

 Replace `<merge-commit-hash>` with the hash of the merge commit. The `-m 1` option tells Git to revert to the state of the repository before the merge. You can find the merge commit hash with `git log`.

- This command will create a new commit that undoes the merge. This is a safer option because it doesn't alter the existing commit history.

```bash
git revert -m 1 HEAD
```

This command creates a new commit that undoes the changes made by the merge commit (indicated by `HEAD`). The `-m 1` option tells Git to revert to the state of the repository before the merge.

### Head vs Commit Hash

Whether to use `git reset/revert` with a merge commit hash or `HEAD` depends on your specific situation and what you want to achieve.

- **Using `HEAD`**: This refers to the latest commit on the current branch. If you've just performed a merge and haven't made any other commits since then, using `HEAD` with `git reset` or `git revert` will undo that merge. This is a quick way to undo a recent merge.
- **Using a specific merge commit hash**: This is useful if you've made several commits after the merge and you want to undo a specific merge. You can find the commit hash of the merge using `git log`, and then use that hash with `git reset` or `git revert`.

In general, if you're undoing a recent merge and you haven't made any other commits since then, using `HEAD` is simpler and quicker. If you're undoing an older merge, or if you've made other commits after the merge, you'll need to use the specific merge commit hash.



#  Workflow
## Typical Repo Set-up/Staging

```bash
git init # Set-up git hidden files in current dir.
git add . # Add everything in directory to config - stage everything
git status # View files/changes that need to be based/added
git commit -m 'Commit Details Message' # Commit the files to the base
```
## Creating a New Repo

You have two options, you can either create the repo over the client in browser or use a CLI too i.e. GitHub CLI

```bash
gh auth login
cd your_project_directory
git init
gh repo create
```

## Cloning an existing repo

A typical Git workflow for a beginner might look something like this:

1. **Clone the repository**: This downloads a copy of the code onto your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate into the repository**: Change your current directory to the repository's directory.

   ```bash
   cd <repository-name>
   ```

3. **Create a new branch**: It's a good practice to create a new branch for each new feature or bug fix.

   ```bash
   git checkout -b <branch-name>
   ```

4. **Make changes**: Edit the code in your preferred text editor.

5. **Check the status of your changes**: This shows you which changes are staged, unstaged, and untracked.

   ```bash
   git status
   ```

6. **Stage your changes**: This adds your changes to the staging area in preparation for a commit.

   ```bash
   git add .
   ```

7. **Commit your changes**: This saves your changes to the local repository.

   ```bash
   git commit -m "<commit-message>"
   ```

8. **Push your changes to the remote repository**: This uploads your changes to the remote repository.

   ```bash
   git push origin <branch-name>
   ```

9. **Open a pull request**: This is typically done in the web interface of the platform you're using (like GitHub, GitLab, etc.). It requests that your changes be merged into the main branch.

10. **Merge your pull request**: After your pull request has been reviewed and approved, you can merge your changes into the main branch. This is also typically done in the web interface.

11. **Pull the latest changes from the main branch**: This ensures your local copy of the main branch is up to date.

    ```bash
    git checkout main
    git pull origin main
    ```

12. **Repeat steps 3-11** for each new feature or bug fix.

Remember to replace `<repository-url>`, `<repository-name>`, `<branch-name>`, and `<commit-message>` with your actual values.

## Pushing to a newly created repo

If you're creating a new repository and pushing to it, here's a typical Git workflow:

1. **Create a new directory**: This will be your project directory.

   ```bash
   mkdir <directory-name>
   ```

2. **Navigate into the directory**: Change your current directory to the new directory.

   ```bash
   cd <directory-name>
   ```

3. **Initialize a new Git repository**: This creates a new Git repository in your current directory.

   ```bash
   git init
   ```

4. **Create or modify files**: Add or edit files in your project directory as needed.

5. **Check the status of your changes**: This shows you which changes are staged, unstaged, and untracked.

   ```bash
   git status
   ```

6. **Stage your changes**: This adds your changes to the staging area in preparation for a commit.

   ```bash
   git add .
   ```

7. **Commit your changes**: This saves your changes to the local repository.

   ```bash
   git commit -m "<commit-message>"
   ```

8. **Link your local repository to the remote repository**: This sets the remote repository that your local repository will push to.

   ```bash
   git remote add origin <repository-url>
   ```

9. **Push your changes to the remote repository**: This uploads your changes to the remote repository.

   ```bash
   git push -u origin main
   ```

Remember to replace `<directory-name>`, `<commit-message>`, and `<repository-url>` with your actual values. The `-u` option in the `git push` command sets the upstream repository for your local repository, which makes Git remember your preferences for pushing and pulling in this repository.


# Details about Remote Working

The term `origin` is just a convention and it's the default name Git gives to the server from where you cloned the repository. However, it's not the only name you can use. You can name your remote anything you want. 

For example, if you're working with multiple remotes such as one for the original repository and one for your fork, you might name them differently for clarity:

```bash
git remote add original <original-repository-url>
git remote add fork <fork-repository-url>
```

In this case, `original` and `fork` are the names of the remotes. You would use these names when pushing (`git push original main`) or pulling (`git pull fork main`) changes.

Remember, the names you choose are local to your repository and do not affect the remote repositories in any way. It's best to choose names that make sense to you and your workflow.

- **Verify the remote repository**: You can check that the remote repository has been added correctly with the `git remote -v` command. This will list all remote repositories for your local repository.

```bash
git remote -v
```

## Upstream (Default Push/Pull Parameters)

The `-u` option in `git push` stands for "upstream". When you use this option, Git will remember the parameters you've used with `git push`, specifically the remote repository (like `origin`) and the branch name (like `main` or `master`).

For example, if you use:

```bash
git push -u origin main
```

Git will remember that `origin` is the default remote and `main` is the default branch for this repository. 

After setting the upstream branch with `-u`, you can simply use `git push` or `git pull` in the future, and Git will know that you mean `git push origin main` or `git pull origin main`. 

This can save you some typing in the future and helps to avoid mistakes.

A typical optimal workflow using `-u` could be:

1. Clone a repository or create a new one and make some changes.

   ```bash
   git clone <repository-url>
   ```

   or

   ```bash
   git init
   ```

2. Stage and commit your changes.

   ```bash
   git add .
   git commit -m "Your commit message"
   ```

3. Push your changes to the remote repository and set the upstream branch.

   ```bash
   git push -u origin main
   ```

4. In the future, simply use `git push` or `git pull` to push or pull changes and it will default to said branch on the origin remote repo.

   ```bash
   git push
   git pull
   ```


# Git Logs

`git log` and `git reflog` are both used to view the history of your Git repository, but they show different types of history:

- `git log` shows the commit history in the current branch. The commits are shown in reverse chronological order (most recent commits first). It's a way to see what changes have been made to the code over time.

- `git reflog` shows a list of all actions that have moved the `HEAD` pointer. This includes commits, checkouts, merges, and other actions. It's a way to see all the actions you've performed in your repository, not just the commits.

To restore a deleted branch, you can use `git reflog` to find the commit hash of the last commit on the branch before it was deleted, and then create a new branch with that commit. Here's a typical workflow:

1. Run `git reflog` to see the history of your actions.

   ```bash
   git reflog
   ```

2. Look for the commit hash of the last commit on the branch before it was deleted. It will be listed in the left column of the `git reflog` output.

3. Create a new branch with that commit.

   ```bash
   git checkout -b <branch-name> <commit-hash>
   ```

To exit the `git log` view in bash, you can press `q`. This will return you to your normal command line prompt. This works because `git log` uses a pager (like `less` or `more`) to display the log, and `q` is the standard command to quit those pagers.

# HEAD Pointer
In Git, `HEAD` is a reference (or pointer) to the latest commit in the currently checked-out branch. It's essentially a way for Git to know what the current working commit is, and thus, what the current state of your files should be.

When you make a new commit, the `HEAD` pointer moves to point to that new commit. When you switch branches with `git checkout`, the `HEAD` pointer moves to the latest commit on the new branch.

In most cases, `HEAD` points to the tip of the current branch. However, it can also point to a previous commit, which puts your repository in a "detached HEAD" state. This can be useful for exploring old commits, but any changes you make won't belong to any branch and will be lost when you checkout a branch again.