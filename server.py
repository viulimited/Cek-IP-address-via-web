from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

# Daftar IP dan nama perangkat
devices = {
    "192.168.1.2": "Perangkat 1",
    "192.168.1.3": "Perangkat 2",
    "192.168.1.4": "Perangkat 3",
    "192.168.1.5": "Perangkat 4",
    "192.168.1.6": "Perangkat 5",
    "192.168.1.7": "Perangkat 6",
    "192.168.1.8": "Perangkat 7",
    "192.168.1.9": "Perangkat 8",
    "192.168.1.10": "Perangkat 9",
    "10.10.10.235": "Oppo", 
    "10.10.10.232": "Redmi",
    "10.10.10.234": "Poco",
    "10.10.10.236": "Tv",
    "192.168.12.1": "Garden",
    "192.168.12.154": "Shinobi"
}

def ping_ip(ip):
    """Fungsi untuk melakukan ping ke IP tertentu."""
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    return response == 0  # True jika berhasil, False jika gagal

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def get_status():
    """Mengembalikan status semua IP dalam bentuk JSON."""
    statuses = {ip: {"name": devices[ip], "status": ping_ip(ip)} for ip in devices}
    return jsonify(statuses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
