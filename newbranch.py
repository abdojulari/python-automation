from git import Git
git = Git()
import time

if 'main' in git.branch('--show-current'):
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        git.commit('-m "update project files"')
        git.push('origin', 'main')
        print('Pushed to main')
    else:
        newbranch = input('Enter new branch name: ')
        git.checkout('-b', newbranch)
        git.add('.')
        git.commit('-m "create a new branch"')
        git.push('origin', newbranch)
        print('Pushed to ' + newbranch)
        
        if newbranch in git.branch('--show-current'):
            git.checkout('main')
            git.merge(newbranch)
            git.push('origin', 'master')
            print('Merged ' + newbranch + ' into master')
            git.branch('-d', newbranch)
            print('Deleted ' + newbranch)
else:
    print('You are not in main branch')
