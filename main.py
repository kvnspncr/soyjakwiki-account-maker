import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
import time
#currently borked because logins are disabled :)
def get_account_creation_details(session):
    login_url = 'https://soyjakwiki.net/index.php?title=Special:CreateAccount&returnto=Main+Page'
    initial_response = session.get(login_url)
    new_cookie = session.cookies.get('wikisoy_session')
    time.sleep(1)
    soup = BeautifulSoup(initial_response.content, 'html.parser')
    wpEditToken = soup.find('input', {'id': 'wpEditToken'}).get('value')
    wpCreateaccountToken = soup.find('input', {'name': 'wpCreateaccountToken'}).get('value')
    captchaId = soup.find('input', {'id': 'mw-input-captchaId'}).get('value')
    
    
    print("Soyjak wiki account creator")
    print(f"=" *30)
    print(f"Obtained Cookie: {new_cookie}")
    print(f"wpEditToken: {wpEditToken}")
    print(f"wpCreateaccountToken: {wpCreateaccountToken}")
    print(f"captchaId: {captchaId}")
    print(f"=" *30)
    print("Written by kevin")
    #time.sleep(5) #for debugging decrease later
    time.sleep(2)
    
    return {
        'wpEditToken': wpEditToken,
        'wpCreateaccountToken': wpCreateaccountToken,
        'captchaId': captchaId
    }

def create_account(session, tokens):
    while True:
        random_number = random.randint(1000, 9999)
        #change these vars to your liking, i suggest not touching headers though
        random_username = f"KevinSpencer{random_number}"
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
        #do not change this
        data = {
            'title': 'Special:CreateAccount',
            'wpName': random_username,
            'wpPassword': password,
            'retype': password,
            'email': '',
            'realname': '',
            'captchaWord': captcha_word, 
            'wpCreateaccount': 'Create+your+account',
            'wpEditToken': tokens['wpEditToken'],
            'authAction': 'create',
            'force': '',
            'wpCreateaccountToken': tokens['wpCreateaccountToken'],
            'captchaId': tokens['captchaId']
        }
        login_url = 'https://soyjakwiki.net/index.php?title=Special:CreateAccount&returnto=Main+Page'
        response = session.post(login_url, headers=headers, data=data)
        response_title = BeautifulSoup(response.content, 'html.parser').title.text.strip()
        if 'Welcome' in response_title:
            print(f"Successfully made the account {random_username}")
            break #change to continue if you want to keep making accounts i might add a feature to save creds later!
        else:
            print(f"Failed making account {random_username}")
            #time.sleep(2) #in case you plan on persisting with the acc creation uncomment sleep to avoid rate limit
            break #change to continue instead of break if you want it to try again!

def main(): #main func i suggest not touching anything here
    session = requests.Session()
    print("Getting account creation details...\n")
    tokens = get_account_creation_details(session)
    print("\nCreating account...\n")
    create_account(session, tokens)
if __name__ == "__main__":
    main()

