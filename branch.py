from git import Git
git = Git()
import time

git.branch()
print(git.branch())
if 'master' in git.branch('--show-current'):
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        commit = input('Enter commit message: ')
        git.commit('-m ' + commit)
        git.push('origin', 'master')
        print('Pushed to master')
    else:
        print('No changes to commit! Switching to main branch')
        git.checkout('main')
        git.rebase('master')
        git.push('origin', 'main')
    
elif 'main' in git.branch('--show-current'):
    print('Already on main branch')
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        commit = input('Enter commit message: ')
        git.commit('-m ' + commit)
        git.push('origin', 'main')
        print('Pushed to main')
    else:
        print('No changes to commit!')
        git.checkout('master')
        git.merge('main')
        git.push('origin', 'master')
       