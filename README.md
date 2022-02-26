# python-automation

## Install using

```Python
pip install -U python-dotenv

```

## To count branches

```python
 git branch -a | wc -l

```

## Use show-branch

```python

git show-branch master main 

```

## use difftool

```python

git difftool master main 

```

## using graph

```python
git log --all --decorate --oneline --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(red) Message:  %S" --date=human

```
