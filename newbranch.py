from git import Git
git = Git()
import time

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
            git.checkout('main')
            git.merge(newbranch)
            git.push('origin', 'main')
            print('Merged ' + newbranch + ' into main!')
        else:
            print('No changes to commit')
            
else:
    print('You are not in main branch')
