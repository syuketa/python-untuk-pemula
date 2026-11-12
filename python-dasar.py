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






# Bab 12: Encapsulation
# Encapsulation: membatasi akses langsung ke data di dalam class
class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik      # public
        self._cabang = "Subang"     # protected (konvensi: satu underscore)
        self.__saldo = saldo        # private (dua underscore)

    # Getter: membaca atribut private
    def get_saldo(self):
        return self.__saldo

    # Setter/method dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setoran harus lebih dari 0")

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

akun = Rekening("Budi", 100000)
print(akun.pemilik)
print("Saldo awal:", akun.get_saldo())
akun.setor(50000)
akun.tarik(30000)
print("Saldo akhir:", akun.get_saldo())
akun.tarik(1000000)

# Atribut private tidak bisa diakses langsung
try:
    print(akun.__saldo)
except AttributeError:
    print("Error: __saldo bersifat private")

# Cara lain: decorator @property
class Suhu:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, nilai):
        if nilai < -273.15:
            print("Suhu tidak valid")
        else:
            self.__celsius = nilai

suhu = Suhu(30)
print("Suhu:", suhu.celsius)
suhu.celsius = 35
print("Suhu baru:", suhu.celsius)
suhu.celsius = -500




# Bab 13: Inheritance
# Inheritance: class turunan mewarisi atribut dan method dari class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

    def suara(self):
        print("Hewan ini mengeluarkan suara")

# Class turunan: Kucing mewarisi Hewan
class Kucing(Hewan):
    def suara(self):
        print(self.nama, "berkata: Meong")

# Class turunan dengan constructor sendiri, memakai super()
class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def suara(self):
        print(f"{self.nama} ({self.ras}) berkata: Guk guk")

kucing = Kucing("Mimi")
anjing = Anjing("Doggo", "Golden Retriever")

kucing.makan()      # method warisan dari Hewan
kucing.suara()
anjing.makan()
anjing.suara()

# Mengecek hubungan class
print(isinstance(kucing, Hewan))
print(issubclass(Anjing, Hewan))





# Bab 14: Polymorphism
# Polymorphism: method dengan nama sama, tetapi perilakunya berbeda
class Burung(Hewan):
    def suara(self):
        print(self.nama, "berkata: Cuit cuit")

# Satu perulangan, banyak perilaku berbeda
daftar_hewan = [Kucing("Mimi"), Anjing("Doggo", "Pug"), Burung("Kiki")]
for hewan in daftar_hewan:
    hewan.suara()

# Function yang menerima object apa pun yang punya method suara()
def bunyikan(hewan):
    hewan.suara()

bunyikan(Kucing("Tom"))
bunyikan(Burung("Beo"))

# Polymorphism juga ada pada function bawaan Python
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))

# Operator + berperilaku berbeda sesuai tipe datanya
print(5 + 3)
print("Halo, " + "Python")
print([1, 2] + [3, 4])





# Bab 15: Abstraction
# Abstraction: menyembunyikan detail, hanya menampilkan kerangkanya
from abc import ABC, abstractmethod

# Abstract class: tidak bisa dibuat object langsung
class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

    # Method biasa tetap boleh ada
    def info(self):
        print("Luas:", self.luas(), "| Keliling:", self.keliling())

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari ** 2

    def keliling(self):
        return 2 * 3.14 * self.jari_jari

persegi = Persegi(5)
lingkaran = Lingkaran(7)
persegi.info()
lingkaran.info()

# Abstract class tidak bisa langsung dibuat object
try:
    bentuk = BangunDatar()
except TypeError as e:
    print("Error:", e)
    
    
    
    
    
    
    # Bab 16: Exception Handling
# try-except menangani error agar program tidak berhenti mendadak
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: tidak bisa dibagi dengan nol")

# Menangani beberapa jenis error
try:
    angka = int("abc")
except ValueError:
    print("Error: teks tidak bisa diubah menjadi angka")

# try, except, else, finally
try:
    angka = int("42")
except ValueError:
    print("Input bukan angka")
else:
    print("Berhasil, angkanya:", angka)
finally:
    print("Blok finally selalu dijalankan")

# Menangkap pesan error
try:
    data = [1, 2, 3]
    print(data[10])
except IndexError as e:
    print("Terjadi error:", e)

# Memunculkan error sendiri dengan raise
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    return umur

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)

# Exception buatan sendiri
class SaldoKurangError(Exception):
    pass

try:
    raise SaldoKurangError("Saldo kamu tidak cukup")
except SaldoKurangError as e:
    print("Error:", e)