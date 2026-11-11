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
nama = input("Siapa namamu? ")
print("Halo,", nama)





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