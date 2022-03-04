# python-automation

## Install necessary packages

```Python
pip3 install -U python-dotenv
brew install chromedriver
pip3 install gitpython
pip3 install clipboard
pip3 install selenium  

```


### To count branches

```python
 git branch -a | wc -l

```

### Use show-branch

```python

git show-branch master main 

```

### use difftool

```python

git difftool master main 

```

### using graph

```python
git log --all --decorate --oneline --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(red) Message:  %S" --date=human

```
