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