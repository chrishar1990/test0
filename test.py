#!/usr/bin/env python3
from github import Github
import git
import subprocess
from datetime import datetime
from git import Repo

from git import Repo


repo = git.Repo('/Users/CH185222/practice/test0/')
repo.remote().fetch()

#repo = Repo('/Users/CH185222/practice/test0/')
repo.git.add('--all')
repo.git.commit('-m', 'updated list')
origin = repo.remote(name='https://github.com/chrishar1990/test0')
origin.push()




