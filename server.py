from flask import Flask,jsonify,request 
import sqlite3
import os

app = Flask(__name__)

@app.route("/")
def halaman_utama():
    return "Halo! Server Agus sedang berjalan! 🚀"

@app.route("/tentang")
def tentang():
    return "Ini adalah server pertama saya, dibuat dengan Flask!"

@app.route("/hitung")
def hitung():
    hasil = 10 + 20
    return "Hasil 10 + 20 = " + str(hasil)

@app.route("/api/hitung")
def api_hitung():
    angka1 = request.args.get("a", 0)
    angka2 = request.args.get("b", 0)
    operasi = request.args.get("op", "tambah")
    
    a = float(angka1)
    b = float(angka2)
    
    if operasi == "tambah":
        hasil = a + b
    elif operasi == "kurang":
        hasil = a - b
    elif operasi == "kali":
        hasil = a * b
    elif operasi == "bagi":
        if b == 0:
            return jsonify({"error": "Tidak bisa bagi 0!"})
        hasil = a / b
    else:
        return jsonify({"error": "Operasi tidak valid!"})
    
    return jsonify({
        "angka1": a,
        "angka2": b,
        "operasi": operasi,
        "hasil": hasil
    })
from flask import Flask, jsonify

@app.route("/api/profil")
def profil():
    data = {
        "nama": "Agus Rery",
        "umur": 29,
        "pekerjaan": "Software Engineer (in progress!)",
        "skills": ["Terminal", "Git", "Python", "HTML", "CSS", "JavaScript", "Flask"],
        "hobi": ["Fitnes", "Travling","gaming", "Tidur","makan enak"]
    }
    return jsonify(data)

@app.route("/api/users")
def get_users():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    hasil = []
    for user in users:
        hasil.append({
            "id": user[0],
            "nama": user[1],
            "umur": user[2],
            "hobi": user[3]
        })
    return jsonify(hasil)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
