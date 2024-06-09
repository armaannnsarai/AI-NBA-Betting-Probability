import pandas as pd
import requests
from bs4 import BeautifulSoup

def getPlayerData(url, page, soup):
    return

def searchForPlayer(first, last):
    while True:
        if len(last) < 5:
            last = last[0:3]
        url = f'https://www.basketball-reference.com/players/{last[0]}/{last}{first[0:2]}01/gamelog/2024'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        if soup.title.text == 'Page Not Found (404 error) | Basketball-Reference.com':
            print("Player does not have records.")
            return False
        else:
            print(f"Player found: {soup.title.text}")
            getPlayerData(url, page, soup)

def queueExit():
    exit_opt = input("Do you want to exit? [Yes/No]: ")
    return exit_opt.lower() == "yes"

main = True 
while main:
    first_name = input("Enter Player First Name: ").lower()
    last_name = input("Enter Player Last Name: ").lower()
    searchForPlayer(first_name, last_name)
    if queueExit():
        main = False
