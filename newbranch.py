from git import Git
git = Git()
import time

git.fetch()
# if there are changes to commit, create a new branch and push it and merge to main.
if 'main' in git.branch('--show-current'):
    if 'Changes not staged for commit' in git.status():
        newbranch = input('Enter new branch name: ')
        git.checkout('-b', newbranch)
        if 'Changes not staged for commit' in git.status():
            git.add('.')
            commit = input('Enter commit message: ')
            git.commit('-m ' + commit)
            git.push('origin', newbranch)
            print('Pushed to ' + newbranch)
            time.sleep(3)
            # merge to main from new branch
            git.checkout('main')
            git.merge(newbranch)
            git.push('origin', 'main')
            print('Merged ' + newbranch + ' into main!')

        else:
            print('No changes to commit')
            # merge to main from new branch
    git.checkout('master')
    git.merge('main')
    git.push('origin', 'master')
    print('Merged ' + newbranch + ' into master!')  
            
elif 'master' in git.branch('--show-current'):
    print('You are not in main branch')
