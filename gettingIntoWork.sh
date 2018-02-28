#!/bin/bash
# Stole the majority of this from this gist:
# https://gist.github.com/mnem/1438396
#

if [ "$1" == "--help" ]; then
  echo "Usage: `basename $0` call this in your 'git-repos' folder to pull in every repository you have"
  echo "This will go into each repository of the folder it is called in and first stash any non-commited"
  echo "work. Then checkout the 'develop' branch, and pull."
  exit 0
fi

REPOSITORIES=`pwd`

for REPO in `ls "$REPOSITORIES/"`
do
	if [ -d "$REPOSITORIES/$REPO" ]
	then
		echo "---------------------------------------"
		echo "Updating $REPOSITORIES/$REPO at `date`"
		if [ -d "$REPOSITORIES/$REPO/.git" ]
    	then
			# Go to git folder
			echo "---------------------------------------"
			echo "Found a git repo"
    		cd "$REPOSITORIES/$REPO"

			# Stash anything that was left over from last night
			# so we can checkout develop
			echo "---------------------------------------"
			echo "Stashing $REPOSITORIES/$REPO"
			git sfe git stash

			# Fetch for the heck of it
			git sfe git fetch

			# Checkout develop
			echo "---------------------------------------"
			echo "Checking out Develop $REPOSITORIES/$REPO"
			git sfe git co develop

			# Pull
			echo "---------------------------------------"
      		echo "Pulling in $REPOSITORIES/$REPO"
      		git sfe git pull
      	fi
	fi
done
