from git import Git
git = Git()
import time

if 'main' in git.branch('--show-current'):
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        commit = input('Enter commit message: ')
        git.commit('-m ' + commit)
        git.push('origin', 'main')
        print('Pushed to main')
    else:
        newbranch = input('Enter new branch name: ')
        git.checkout('-b', newbranch)
        if 'Changes not staged for commit' in git.status():
            git.add('.')
            commit = input('Enter commit message: ')
            git.commit('-m ' + commit)
            git.push('origin', newbranch)
            print('Pushed to ' + newbranch)
        else:
            print('No changes to commit')
        if newbranch in git.branch('--show-current'):
            git.checkout('main')
            git.merge(newbranch)
            git.push('origin', 'main')
            print('Merged ' + newbranch + ' into main!')
            git.branch('-d', newbranch)
            print('Deleted ' + newbranch)
else:
    print('You are not in main branch')
