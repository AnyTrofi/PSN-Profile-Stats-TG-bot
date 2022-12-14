import reimport requests
from bs4 import BeautifulSoup
import re
import time

# Function with all received data
def description(soup):
    name = soup.find('span', class_='username').text
    level = int(soup.find('li', class_='icon-sprite level').text)
    total =  re.sub("\D", "", soup.find('li', class_='total').text)
    platinum = int(soup.find('li', class_='platinum').text)
    gold = re.sub("\D", "", soup.find('li', class_='gold').text)
    silver = re.sub("\D", "", soup.find('li', class_='silver').text)
    bronze = re.sub("\D", "", soup.find('li', class_='bronze').text)
    games = (soup.find('span', class_='stat grow').text)[:-12]
    avatar = soup.find('div', class_='avatar').find('img').get('src')

    data = {
        'name': name,
        'level': level,
        'total': total,
        'platinum': platinum,
        'gold': gold,
        'silver': silver,
        'bronze': bronze,
        'games': games,
        'avatar': avatar
    }
    return data

def main(nickname):
    try:
        requests.get(("https://psnprofiles.com/xhr/update/status?user=" + nickname))
        time.sleep(5)
        html = requests.get(("https://psnprofiles.com/" + nickname))
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            data = description(soup)
            return data
    except:
        return 'Wrong ID or psn profile is private'