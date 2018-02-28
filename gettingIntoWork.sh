#!/bin/bash
# Stole the majority of this from this gist:
# https://gist.github.com/mnem/1438396
#

if [ "$1" == "--help" ]; then
  echo "Usage: `basename $0` [branchname] call this in your 'git-repos' folder to pull in every repository you have"
  echo "This will go into each submodule of each repository it can find and first stash any non-commited work."
  echo "Then checkout the 'develop' branch, and pull if no branchname is supplied. If you add a branchname it"
  echo "will checkout the branchname you need. "
  echo "If you have a lot of repos with a lot of submodules this will take a while, but it's quicker then doing"
  echo "it yourself."
  exit 0
fi

BRANCHNAME=$1
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

			if [ -n $BRANCHNAME ]
				# Checkout supplied branch name
				echo "---------------------------------------"
				echo "Checking out $BRANCHNAME in $REPOSITORIES/$REPO"
				git sfe git co $BRANCHNAME
			then
			else
				# Checkout develop if no branch name supplied
				echo "---------------------------------------"
				echo "Checking out develop in $REPOSITORIES/$REPO"
				git sfe git co develop
			fi

			# Pull
			echo "---------------------------------------"
      		echo "Pulling in $REPOSITORIES/$REPO"
      		git sfe git pull
      	fi
	fi
done
