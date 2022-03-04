from git import Git
git = Git()
import time

branches = []
for branch in git.branch('--list'):
    branches.append(branch.strip())
    # check if a tracked branch exists
    trackbranch  = t.tracking_branch()
    if trackbranch:
        branches.append(trackbranch)
    