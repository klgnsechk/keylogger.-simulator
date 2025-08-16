# İstemci tarafını başlatmak için: python3 client.py
# Çıkmak için 'q' tuşuna basın

import sys
import requests
import tty
import termios

SERVER_URL = 'http://127.0.0.1:5000/log'

def get_key():
    """Terminalden tek karakter okur (anlık tuş algılama)"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Tuşları yazın (çıkmak için 'q'):")

while True:
    key = get_key()
    if key == 'q':
        print("Çıkılıyor...")
        break
    try:
        response = requests.post(SERVER_URL, json={'key': key})
        print(f"Gönderildi: {key}")
    except Exception as e:        
        print(f"Hata: {e}")
