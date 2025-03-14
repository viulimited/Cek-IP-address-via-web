# Cek-IP-address-via-web
Ping IP lewat web 

Menggunakan Init Script (Lebih Stabil)

Jika ingin solusi lebih baik dan dapat dikelola oleh OpenWrt (start/stop otomatis), gunakan procd init script.

Langkah 1: Buat File Init Script

# Buat file baru:

nano /etc/init.d/flask-server

# Tambahkan isi berikut:

#!/bin/sh /etc/rc.common
#OpenWrt Init Script untuk Flask Server

START=99
STOP=10

start() {
    echo "Menjalankan Flask Server..."
    python3 /path/ke/server.py > /tmp/server.log 2>&1 &
    echo $! > /var/run/flask-server.pid
}

stop() {
    echo "Menghentikan Flask Server..."
    kill $(cat /var/run/flask-server.pid) || true
    rm -f /var/run/flask-server.pid
}

Simpan file (CTRL+X, lalu Y, lalu Enter).

# Langkah 2: Beri Izin Eksekusi

chmod +x /etc/init.d/flask-server

# Langkah 3: Aktifkan & Jalankan

# Agar otomatis saat booting
/etc/init.d/flask-server enable 

# Jalankan manual sekarang
/etc/init.d/flask-server start  

# Cek status:

ps | grep server.py

# Hentikan manual:

/etc/init.d/flask-server stop
