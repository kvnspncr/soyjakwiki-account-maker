import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
import time
while True:
    try:
        session = requests.Session()
        url = 'https://soyjakwiki.net/index.php?title=Special:CreateAccount&returnto=Main+Page'
        response = session.get(url)
        cookie = session.cookies.get('wikisoy_session')
        soup = BeautifulSoup(response.content, 'html.parser')
        title = BeautifulSoup(response.content, 'html.parser').title.text.strip()
        if 'Just a moment' in title:
            print("Blocked by cloudflare, change your exit node!")
            break
        wpEditToken = soup.find('input', {'id': 'wpEditToken'}).get('value')
        wpCreateaccountToken = soup.find('input', {'name': 'wpCreateaccountToken'}).get('value')
        captchaId = soup.find('input', {'id': 'mw-input-captchaId'}).get('value')
        print("Soyjak wiki account creator")
        print(f"=" *30)
        print(f"Obtained Cookie: {cookie}")
        print(f"wpEditToken: {wpEditToken}")
        print(f"wpCreateaccountToken: {wpCreateaccountToken}")
        print(f"captchaId: {captchaId}")
        print(f"=" *30)
        #time.sleep(2)
        wpEditToken=wpEditToken
        wpCreateaccountToken=wpCreateaccountToken,
        captchaId=captchaId
        global captcha
        captcha="KolymaNET"
        print("Getting account creation details...\n")
        number = random.randint(1000, 9999)
        username = f"KevinSpencer{number}"
        password = "p@55w0rd"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://soyjakwiki.net/index.php?title=Special:CreateAccount&returnto=Main+Page',
            'Cookie': f'wikisoy_session={session.cookies.get("wikisoy_session")}'
        }
        data = {
            'title': 'Special:CreateAccount',
            'wpName': username,
            'wpPassword': password,
            'retype': password,
            'email': '',
            'realname': '',
            'captchaWord': captcha,
            'wpCreateaccount': 'Create+your+account',
            'wpEditToken': wpEditToken,
            'authAction': 'create',
            'force': '',
            'wpCreateaccountToken': wpCreateaccountToken,
            'captchaId': captchaId,
        }
        login_url = 'https://soyjakwiki.net/index.php?title=Special:CreateAccount&returnto=Main+Page'
        response = session.post(login_url, headers=headers, data=data)
        response_title = BeautifulSoup(response.content, 'html.parser').title.text.strip()
        if 'Welcome' in response_title:
            print(f"Successfully made the account {username}")
            print(f"=" *30)
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"=" *30)
            print("Written by Kevin!")
            break
        else:
            print(f"Failed making account {username}")
            captcha="Froot"
            time.sleep(2)
            continue
    except KeyboardInterrupt:
        print("Exiting!")
        break
