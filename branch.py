from git import Git
git = Git()

branch =  git.branch()
if 'master' in branch:
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        git.commit('-m "Initial commit"')
        git.push('origin', 'master')
    else:
        print('No changes to commit')
elif 'main' in branch:
    print('Already on main branch')


