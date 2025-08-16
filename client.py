# istemci tarafı başlatmak için Python3 client.py
# çıkmak için ise q harfini kullanın. 
import sys
import requests
import tty                                             import termios

SERVER_URL = 'http://127.0.0.1:5000/log'

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)  # Tek karakter oku         finally:
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
