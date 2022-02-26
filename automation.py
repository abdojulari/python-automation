
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()   
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time
import os

def user_account():
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return email, password
user_account = user_account()


repository = input('Enter repository name: ')

driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
driver.get('https://github.com/login')

user = driver.find_element_by_id('login_field')
user.send_keys(user_account[0])

user = driver.find_element_by_id('password')
user.send_keys(user_account[1])

sign = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]')
sign.submit()

time.sleep(5)

new = driver.find_element_by_xpath('/html/body/div[6]/div/aside/div[2]/div[2]/div/h2/a')
new.click()

time.sleep(5)
new = driver.find_element_by_xpath('/html/body/div[6]/main/div/form/div[4]/auto-check/dl/dd/input')
new.send_keys(repository)

# check Add a README file
check = driver.find_element_by_xpath('/html/body/div[6]/main/div/form/div[6]/div[5]/div[1]/label/input[2]')
check.click()

# create repository
create = driver.find_element_by_xpath('/html/body/div[6]/main/div/form/div[6]/button')
create.submit()

time.sleep(2)
# clone a repository
clone = driver.find_element_by_xpath('/html/body/div[6]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary')
clone.click()

clone = driver.find_element_by_xpath('/html/body/div[6]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/ul/li[1]/tab-container/div[3]/div/div/clipboard-copy')
clone.click()

time.sleep(2)
git_url = clipboard.paste()
print(git_url)

os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial commit"')
if 'error: remote origin already exists' in os.system('git remote add origin ' + git_url):
    #os.system('git remote set-url origin ' + git_url)
    os.system('git push -u origin main')
print('\n Task Completed Successfully...')

#os.system('git push -f origin main')


