#!/bin/bash
# Stole the majority of this from this gist:
# https://gist.github.com/mnem/1438396
#

if [ "$1" == "--help" ]; then
  echo "Usage: `basename $0` [branchname] call this in your 'git-repos' folder to pull in every repository you have"
  echo "This will go into each repository of the folder it is called in and call the 'git branch'"
  echo "command. This will help when you need to see what branch every repo is on."
  exit 0
fi

REPOSITORIES=`pwd`

for REPO in `ls "$REPOSITORIES/"`
do
	if [ -d "$REPOSITORIES/$REPO" ]
	then
		if [ -d "$REPOSITORIES/$REPO/.git" ]
    	then
			# Go to git folder
    		cd "$REPOSITORIES/$REPO"
    		git sfe git branch
      	fi
	fi
done
