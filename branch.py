from git import Git
git = Git()

branch =  git.branch()
if 'master' in branch:
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        git.commit('-m "Initial commit"')
        git.push('origin', 'master')
        print('Pushed to master')
    else:
        print('No changes to commit! Switching to main branch')
        git.checkout('main')
        git.rebase('master')
        git.push('origin', 'main')
        print('main is now up to date')
elif 'main' in branch:
    print('Already on main branch')


