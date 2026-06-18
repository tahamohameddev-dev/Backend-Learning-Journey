# Linux and Git Learning 

## Linux Commands

* `sudo apt update` : Refreshes the list of available software.
* `sudo apt upgrade` : Installs updates for the software.

* `apt show <package>` : Show Einformation about a software package.

* `mkdir <folder-name>` : Creates a new folder.
* `touch <file-name>` : Creates a new empty file.

* `cp <source> <destination>` : Copies files or folders.
* `mv <source> <destination>` : Moves or renames files or folders.

* `chown <user> <file>` : Changes the owner fo a file or folder.
* `chmod <permissions> <file>` : Changes the read, write and execute permissions of a file.

* `find` : Searches for files and folders based on size , type, or permissions.

* `grep <word> <file>` : Serches for a specific word or inside a file.

* `rm <file>` Deletes a file.
* `rm -rf <folder>` : Deletes a folder and everything inside it without asking

# Git Commands

## Setting Up a Repository
* `git init` : Creates a new local Git repository.
* `git clone <repository-url>` : Copies an existing repository from GitHub to your computer.
* `git remote add origin <repository-url>` : Links your local repository to a GitHub repository.
* `git remote -v` : Shows all remote repositories linked to your project.

## Tracking and Saving Changes
* `git status` : Shows the current state of your files (Red = untracked, Green = staged).
* `git add .` : Stages all new and modified files for the next commit.
* `git add <file-name>` : Stages a specific file only.
* `git commit -m "title" -m "description"` : Saves your staged changes locally with a title and description.
* `git log` : Shows the history of all commits with their dates and IDs.

## Pushing to GitHub
* `git branch -M main` : Renames the default branch to main.
* `git push origin -u main` : Pushes your project to GitHub for the first time and sets the default branch.
* `git push` : Pushes your new saved changes to GitHub.

## Branching and Collaboration
* `git branch` : Lists all local branches and shows your current branch.
* `git checkout -b <branch-name>` : Creates a new branch and switches to it immediately.
* `git checkout <branch-name>` : Switches from your current branch to another branch.
* `git diff <branch-name>` : Shows the code differences between your branch and another branch.
* `git merge <branch-name>` : Merges changes from another branch into your current branch.
* `git push --set-upstream origin <branch-name>` : Pushes a newly created local branch to GitHub for the first time.
* `git branch -D <branch-name>` : Deletes a branch locally after merging it.

## Undoing Mistakes and Reverting
* `git reset <file-name>` : Unstages a file but keeps your code changes safe.
* `git reset HEAD~1` : Undoes the last commit and brings files back to the staging area.
* `git reset --hard <commit-id>` : Reverts the entire project to a specific commit and deletes all changes after it.