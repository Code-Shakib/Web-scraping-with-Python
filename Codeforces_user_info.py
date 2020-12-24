""" This code is developed by Mohammad Shakib """

from bs4 import BeautifulSoup #importing BeautifulSoup
import requests #importing requests

def codeforcesProfileData(userName):
    url = f'http://codeforces.com/profile/{userName}' #placeing the username
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    user_info = soup.find_all('span', style="font-weight:bold;")
    userData = {}
    userData['Current title    '] = user_info[1].string
    userData['Contest rating   '] = user_info[0].string
    userData['Max rating       '] = user_info[2].string
    
    print('============Codeforces Profile Data================')
    print(f'Username: {userName}')
    for i, j in userData.items():
        print(i,':',j)
    
userName = input('Enter codeforces username: ')
try:
    codeforcesProfileData(userName)
except:
    print('Something went wrong!\nTry again.')
