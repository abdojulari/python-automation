from git import Git
git = Git()
import time

print(git.log('--oneline'))