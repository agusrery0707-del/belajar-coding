# ============================================
# RANGKUMAN BELAJAR CODING - AGUS RERY
# ============================================

print("=" * 45)
print("   RANGKUMAN BELAJAR CODING - AGUS RERY")
print("=" * 45)

# PHASE 2 - PYTHON
print("\n📌 PHASE 2 - PYTHON DASAR")
print("-" * 45)

nama = "Agus Rery"
umur = 29
tinggi = 170.5
hobi = ["Fitnes", "Travling", "Gaming", "Tidur", "Makan Enak"]

print(f"Nama    : {nama}")
print(f"Umur    : {umur}")
print(f"Tinggi  : {tinggi}")
print(f"Hobi    : {', '.join(hobi)}")

# Kondisi
print("\n✅ Kondisi:")
if umur >= 17:
    print(f"{nama} sudah dewasa")

# Loop - custom sendiri jadi 1-10!
print("\n✅ For Loop (custom 1-10):")
for i in range(1, 11):
    print(f"  nomor {i}")

# Functions
print("\n✅ Functions:")
def sapa(nama):
    return f"Halo, {nama}! Selamat datang!"

def hitung_luas(panjang, lebar):
    return panjang * lebar

print(sapa("Agus"))
print(f"Luas 10x5 = {hitung_luas(10, 5)}")

# Kalkulator - tambah pangkat sendiri!
print("\n✅ Kalkulator (+ pangkat custom sendiri!):")
def kalkulator(a, b, op):
    if op == "tambah":   return a + b
    elif op == "kurang": return a - b
    elif op == "kali":   return a * b
    elif op == "bagi":   return a / b if b != 0 else "Error!"
    elif op == "pangkat": return a ** b  # ditambah sendiri!

print(f"10 + 5  = {kalkulator(10, 5, 'tambah')}")
print(f"10 - 5  = {kalkulator(10, 5, 'kurang')}")
print(f"10 x 5  = {kalkulator(10, 5, 'kali')}")
print(f"10 / 5  = {kalkulator(10, 5, 'bagi')}")
print(f"2 ^ 8   = {kalkulator(2, 8, 'pangkat')}")

# PHASE 3 - FRONTEND
print("\n📌 PHASE 3 - FRONTEND")
print("-" * 45)
print("✅ HTML  - Struktur website pribadi")
print("✅ CSS   - Background kuning, heading merah (custom!)")
print("✅ JS    - Tombol interaktif & mode gelap")
print("✅ Live  - https://agusrery0707-del.github.io/belajar-coding/")

# PHASE 4 - BACKEND
print("\n📌 PHASE 4 - BACKEND")
print("-" * 45)
print("✅ Flask  - Web server & routing")
print("✅ API    - REST API dengan JSON")
print("✅ SQLite - Database dengan kolom email (custom!)")
print("✅ Live   - https://web-production-d6c55.up.railway.app")

routes = [
    "GET /            → Halaman utama",
    "GET /tentang     → Info server",
    "GET /api/profil  → Data profil JSON",
    "GET /api/users   → Data users dari database",
    "GET /api/hitung  → Kalkulator API",
]
print("\n  Routes:")
for r in routes: print(f"  • {r}")

# PHASE 5 - PRO LEVEL
print("\n📌 PHASE 5 - PRO LEVEL")
print("-" * 45)
print("✅ README.md  - Dokumentasi lengkap")
print("✅ Railway    - Backend live di internet")
print("✅ Portfolio  - GitHub lengkap")

# Interview prep
print("\n✅ Soal Interview:")

print("\n  FizzBuzz:")
for i in range(1, 16):
    if i % 15 == 0: print(f"  {i} → FizzBuzz")
    elif i % 3 == 0: print(f"  {i} → Fizz")
    elif i % 5 == 0: print(f"  {i} → Buzz")

print("\n  Palindrome:")
def cek_palindrome(kata):
    return kata == kata[::-1]
for kata in ["radar", "hello", "kasur rusak"]:
    print(f"  '{kata}' → {cek_palindrome(kata)}")

print("\n  Filter Genap:")
def filter_genap(lst):
    return [x for x in lst if x % 2 == 0]
print(f"  {filter_genap([1,2,3,4,5,6,7,8])}")

# Penutup
print("\n" + "=" * 45)
print("🏆 PENCAPAIAN AGUS RERY:")
print("=" * 45)
for item in [
    "Terminal & PowerShell",
    "Git & GitHub",
    "Python Dasar",
    "HTML + CSS + JavaScript",
    "Flask & REST API",
    "SQLite Database",
    "Deploy ke Internet",
    "Siap Interview Kerja!"
]:
    print(f"  ✅ {item}")
print("\n🚀 Dari nol jadi Software Engineer!")
print("=" * 45)