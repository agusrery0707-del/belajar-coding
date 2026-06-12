import sqlite3
#buat/buaka database
conn = sqlite3.connect('data.db')
#buat tabel
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
             age INTEGER,
             hobi TEXT
);
""")

#masukkan data
cursor = conn.cursor()
cursor.execute("""INSERT INTO users (name, email, age, hobi) VALUES
('Agus Rery', 'agus.rery@example.com', 25, 'Fitnes, Travling, gaming, Tidur, makan enak')
""")
cursor.execute("""INSERT INTO users (name, email, age, hobi) VALUES
('Budi Santoso', 'budi.santoso@example.com', 30, 'Membaca, Menulis, Jalan-jalan')
""")
cursor.execute("""INSERT INTO users (name, email, age, hobi) VALUES
('Siti Aminah', 'siti.aminah@example.com', 28, 'Memasak, Menyanyi, Menonton Film')
""")
#sismpan perubahan dan tutup koneksi
conn.commit()
#ambil semua data
cursor.execute("SELECT * FROM users")
semua_user= cursor.fetchall()
print("Data User:")
for user in semua_user:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}, Hobi: {user[4]}")
    #tutup koneksi
conn.close()
print("Database berhasil dibuat dan data berhasil dimasukkan!")