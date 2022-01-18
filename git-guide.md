Command Line Git
- status 
	- Shows status of the local repository. This status includes:
		- number of local commits that have not been synced with remote (GitHub)
		- list of files in local folder than are NOT being tracked by git
		- list of files in local folder that have changes that need to be committed
	- git status
- clone
	- This is used to create a copy or clone of an existing target repository in a new directory
	- git clone file.txt
- add
	- adds a change in the working directory to the staging area
	- git add file.txt
- rm
	- removes a file from a Git repository
	- git rm file.txt
- commit
	- The git commit command captures a snapshot of the project's currently staged changes
	- git commit -n "..."
- push
	- The git push command is used to upload local repository content to a remote repository
	- git push orgin master
- fetch
	- The git fetch command downloads commits, files, and refs from a remote repository into your local repo
	- git fetch --all
- merge 
	- The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch
	- git branch 
- pull
	- The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content
	- git pull
- branch 
	- The git branch command lets you create, list, rename, and delete branches
	- git branch
- checkout
	- The git checkout command lets you navigate between the branches created by git branch
	- git checkout master 

Git files & folders
- .git folder
	- The . git folder contains all the information that is necessary for your project in version control and all the information about commits, remote repository address, etc.
- gitignore folder
	- gitignore file is a plain text file where each line contains a pattern for files/directories to ignore

GitHub
- Pull requests 
	- Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub
- SSH authentication to repositories
	- SSH keys are an authentication method used to gain access to an encrypted connection between systems and then ultimately use that connection to manage the remote system

Resource
	- google.com
	- geeksforgeeks.com
	- docs.github.com
