from git import Git
git = Git()

git.branch()
if 'master' in git.branch():
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        git.commit('-m "Initial commit"')
        git.push('origin', 'master')
        print('Pushed to master')
    else:
        print('No changes to commit! Switching to main branch')
        git.checkout('main')
        git.diff('main', 'origin/main')
        if '' in git.diff('main', 'origin/main'):
           print('No difference!')
           git.rebase('master')
           git.push('origin', 'main')
           print('main is now up to date')
        else:
            git.pull('origin', 'main')
            if 'fatal: refusing to merge unrelated histories' in git.pull('origin', 'main'):
                print('You have a conflict! Resolving using --allow-unrelated-histories')
                git.pull('origin', 'main -- allow-unrelated-histories')
            else:
                print('Pulled from main')

                git.rebase('master')
                git.push('origin', 'main')
                if 'error: failed to push some refs to' in git.push('origin', 'main'):
                    git.push('origin', 'main --force')
                    print('main is now up to date')
elif 'main' in git.branch():
    print('Already on main branch')
    git.status()
    if 'Changes not staged for commit' in git.status():
        git.add('.')
        git.commit('-m "update project files"')
        git.push('origin', 'main')
        print('Pushed to main')
    else:
        print('No changes to commit!')
        git.checkout('master')