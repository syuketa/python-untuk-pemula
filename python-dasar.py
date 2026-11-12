# Bab 1: Pengenalan & Instalasi Python
# Program pertama: menampilkan teks ke layar
print("Hello, World!")

# Menampilkan versi Python yang terpasang
import sys
print("Versi Python:", sys.version)






# Bab 2: Struktur Dasar Program Python

# Ini adalah komentar satu baris
"""
Ini adalah komentar
beberapa baris (docstring)
"""

# Menampilkan output dengan print()
print("Halo, Python!")
print("Belajar", "Python", "Dasar", sep=" - ")

# Indentasi menentukan blok kode
if True:
    print("Indentasi itu penting")

# Meminta input dari pengguna
# nama = input("Siapa namamu? ")
# print("Halo,", nama)





# Bab 3: Tipe Data Dasar
nama = "Budi"          # str (teks)
umur = 17              # int (bilangan bulat)
tinggi = 170.5         # float (bilangan desimal)
siswa = True           # bool (benar/salah)

print(nama, type(nama))
print(umur, type(umur))
print(tinggi, type(tinggi))
print(siswa, type(siswa))

# Konversi tipe data (casting)
angka_teks = "25"
angka = int(angka_teks)
print(angka + 5)
print(str(umur) + " tahun")
print(float(umur))
print(bool(0), bool(1))





# Bab 4: Variable
# Membuat variable dan mengisi nilainya
nama_depan = "Budi"
usia = 17
print(nama_depan, usia)

# Mengubah nilai variable
usia = 18
print("Usia sekarang:", usia)

# Mengisi beberapa variable sekaligus
x, y, z = 1, 2, 3
a = b = c = 0
print(x, y, z, a, b, c)

# Aturan penamaan: huruf, angka, underscore; tidak boleh diawali angka
nama_lengkap = "Budi Santoso"
_rahasia = "boleh diawali underscore"
print(nama_lengkap, _rahasia)

# Python peka huruf besar-kecil (case sensitive)
kota = "Subang"
Kota = "Bandung"
print(kota, Kota)

# Menukar nilai dua variable
p, q = 10, 20
p, q = q, p
print("p =", p, "q =", q)





# Bab 5: Konstanta
# Python tidak punya konstanta sungguhan.
# Konvensinya: nama ditulis HURUF BESAR dan nilainya tidak diubah.
PI = 3.14159
GRAVITASI = 9.8
NAMA_APLIKASI = "Belajar Python"
MAKS_PERCOBAAN = 3

print(PI)
print(GRAVITASI)
print(NAMA_APLIKASI)
print(MAKS_PERCOBAAN)

# Contoh pemakaian konstanta dalam perhitungan
jari_jari = 7
luas_lingkaran = PI * jari_jari ** 2
print("Luas lingkaran:", luas_lingkaran)

massa = 5
berat = massa * GRAVITASI
print("Berat benda:", berat)






# Bab 6: Operator
a = 10
b = 3

# Operator aritmatika
print("Tambah:", a + b)
print("Kurang:", a - b)
print("Kali:", a * b)
print("Bagi:", a / b)
print("Bagi bulat:", a // b)
print("Sisa bagi:", a % b)
print("Pangkat:", a ** b)

# Operator perbandingan
print("Sama dengan:", a == b)
print("Tidak sama:", a != b)
print("Lebih besar:", a > b)
print("Lebih kecil atau sama:", a <= b)

# Operator logika
print("and:", a > 5 and b < 5)
print("or:", a > 5 or b > 5)
print("not:", not (a > b))

# Operator assignment
c = 5
c += 2
c *= 3
print("Nilai c:", c)






# Bab 7: Control Flow
nilai = 80

# Percabangan if, elif, else
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
else:
    print("Grade C")

# Perulangan for
for i in range(1, 6):
    print("Perulangan ke-", i)

# Perulangan while
n = 1
while n <= 3:
    print("While:", n)
    n += 1

# break dan continue
for i in range(1, 10):
    if i == 3:
        continue
    if i == 6:
        break
    print("Angka:", i)
    
    
    
    
    
    
    # Bab 8: Function
# Function tanpa parameter
def sapa():
    print("Halo, selamat belajar Python!")

sapa()

# Function dengan parameter
def sapa_nama(nama):
    print("Halo,", nama)

sapa_nama("Budi")

# Function dengan return
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil tambah:", hasil)

# Parameter default
def perkenalan(nama, kota="Subang"):
    print(f"Nama saya {nama}, dari {kota}")

perkenalan("Budi")
perkenalan("Ani", "Bandung")

# Function dengan banyak return value
def hitung(a, b):
    return a + b, a * b

jumlah, kali = hitung(4, 5)
print("Jumlah:", jumlah, "Kali:", kali)






# Bab 9: List, Tuple, dan Set
# List: berurutan, bisa diubah
buah = ["apel", "jeruk", "mangga"]
print(buah)
print(buah[0])
buah.append("pisang")
buah.remove("jeruk")
buah[0] = "anggur"
print(buah)
print("Jumlah:", len(buah))

# Tuple: berurutan, TIDAK bisa diubah
koordinat = (10, 20)
print(koordinat)
print(koordinat[0])

# Set: tidak berurutan, tidak ada duplikat
himpunan = {1, 2, 3, 3, 2}
print(himpunan)
himpunan.add(4)
print(himpunan)

# Operasi set
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Gabungan:", set_a | set_b)
print("Irisan:", set_a & set_b)
print("Selisih:", set_a - set_b)





# Bab 10: Dictionary
# Dictionary menyimpan data dalam pasangan key: value
siswa = {
    "nama": "Budi",
    "umur": 17,
    "jurusan": "RPL"
}
print(siswa)

# Mengakses nilai
print(siswa["nama"])
print(siswa.get("umur"))

# Menambah dan mengubah data
siswa["kelas"] = "XI"
siswa["umur"] = 18
print(siswa)

# Menghapus data
del siswa["kelas"]
print(siswa)

# Mengambil keys, values, dan items
print(siswa.keys())
print(siswa.values())
print(siswa.items())

# Perulangan pada dictionary
for key, value in siswa.items():
    print(key, "=", value)

# Mengecek key
print("nama" in siswa)





# Bab 11: Class & Object (OOP Dasar)
# Class adalah cetak biru, object adalah hasil cetakannya
class Siswa:
    # Atribut class (dimiliki semua object)
    sekolah = "SMK Negeri"

    # Constructor: dipanggil otomatis saat object dibuat
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    # Method: function di dalam class
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari kelas {self.kelas}")

# Membuat object dari class
siswa1 = Siswa("Budi", "XI RPL")
siswa2 = Siswa("Ani", "XI RPL")

# Mengakses atribut dan memanggil method
print(siswa1.nama, siswa1.kelas)
siswa1.perkenalan()
siswa2.perkenalan()
print("Sekolah:", Siswa.sekolah)

# Mengubah nilai atribut
siswa1.kelas = "XII RPL"
siswa1.perkenalan()