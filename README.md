# Python untuk Pemula

Catatan dan latihan belajar Python mengikuti materi [Santrikoding](https://santrikoding.com).


## Tentang

Repo ini berisi latihan dari buku **Python untuk Pemula** di Santrikoding. Semua kode latihan ada di satu file, `latihan.py`, dan hasil outputnya ditulis di bagian "Hasil Output" di bawah.

## Progres Belajar

Keterangan: ✓ selesai, ○ belum

### Pengenalan dan Instalasi Python

| Status | Materi |
|:---:|---|
| ✓ | Pengenalan Python |
| ✓ | Instalasi Python |

### Dasar Pemrograman Python

| Status | Materi |
|:---:|---|
| ✓ | Dasar Pemrograman Python |
| ✓ | Variabel dan Tipe Data pada Python |
| ✓ | Operator pada Python |
| ✓ | Kondisi If Else pada Python |
| ✓ | Perulangan pada Python |
| ✓ | Lists dan Dictionaries pada Python |
| ✓ | Function |
| ✓ | Class dan Object |

### PIP dan Virtual Environments

| Status | Materi |
|:---:|---|
| ○ | PIP dan Virtual Environments |

> Materi sisanya ditambahkan seiring progres belajar.

---

## Ringkasan Materi

### 1. Dasar Pemrograman Python

Program pertama: menampilkan teks ke layar dengan `print()`.

```python
print("Halo Python")
```

### 2. Variabel dan Tipe Data

Tipe data yang dipelajari: angka (`int` dan `float`), teks (`str`), dan `bool`.

```python
x = 5            # integer
a = 7.5          # floating point
nama = "Python"  # string
benar = True     # boolean (harus diawali huruf besar)
```

### 3. Operator

| Jenis | Operator |
|---|---|
| Aritmatika | `+`  `-`  `*`  `/`  `%`  `**` |
| Perbandingan | `==`  `!=`  `<`  `<=`  `>`  `>=` |
| Logika | `and`  `or`  `not` |

### 4. Kondisi If Else

Blok kode di dalam `if` ditentukan oleh indentasi (spasi di awal baris).

```python
a = 60

if a > 90:
    print("Dapat nilai A.")
elif a > 70:
    print("Dapat nilai B.")
else:
    print("Dapat nilai C.")
```

### 5. Perulangan

```python
for x in range(5):
    print("Halo Python.")

counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

### 6. Lists dan Dictionaries

Menyimpan banyak nilai dalam satu variabel: list berdasarkan urutan, dictionary berdasarkan `key`.

### 7. Function

Function dengan argumen, arbitrary arguments (`*names`), keyword arguments, `**kwargs`, dan nilai default.

```python
def belajar_python(name="Alien"):
    print("Halo, Saya %s" % name)

belajar_python()          # Halo, Saya Alien
belajar_python("Rizqi")   # Halo, Saya Rizqi
```

### 8. Class dan Object

Class sebagai cetak biru objek, lengkap dengan property, constructor, dan method.

```python
class Cat:
    def __init__(self, color):
        self.color = color

    def say(self):
        print("Meong..meong")

cat1 = Cat("orange")
print(cat1.color)   # orange
cat1.say()          # Meong..meong
```

---

## Hasil Output

### Boolean (kesalahan penulisan)

```
c = true
NameError: name 'true' is not defined. Did you mean: 'True'?
```

### Operator aritmatika (a = 4, b = 2)

```
6      # a + b
2      # a - b
8      # a * b
2.0    # a / b
0      # a % b
16     # a ** b
```

### Operator perbandingan (a = 3, b = 5)

```
False  # a == b
True   # a != b
True   # a <  b
True   # a <= b
False  # a >  b
False  # a >= b
```

### Operator logika (a = 3, b = 9)

```
True   # a < 5 and b > 6
False  # a < 5 and b < 6
False  # a > 5 and b < 6
True   # a < 5 or  b > 6
True   # a < 5 or  b < 6
False  # a > 5 or  b < 6
False  # not(a < 5 or b > 6)
True   # not(a > 5 or b < 6)
```

### Kondisi If Else

```
Benar.
nilai x lebih kecil dari y.
Dapat nilai B.
Dapat nilai C.
```

### Perulangan

```
Halo Python.   (5 kali)
Apple
Banana
Mango
Durian
i n d o n e s i a   (satu huruf per baris)
0 1 2 3 4
```

### Function

```
Halo
Halo, Saya Rizqi
Halo, Saya Rizqi. Umur saya 30
Halo, Saya Rizqi
Halo, Saya Fika
Halo, Saya Yudi
Halo, Saya Rizqi. Umur Saya 30
Halo, Saya Fika. Umur Saya 25
Halo, Saya Rizqi. Umur Saya 20
Halo, Saya Alien
```

### Class dan Object

```
black
orange
Meong..meong
My color is black
```

---

## Kesalahan yang Pernah Ditemui

| Kode salah | Masalah | Yang benar |
|---|---|---|
| `c = true` | `NameError`, boolean harus huruf besar | `c = True` |
| `counter =+ 1` | Dibaca `counter = +1`, loop tidak pernah berhenti | `counter += 1` |
| `for (x in range(5)):` | `SyntaxError`, kata `in` tidak boleh dibungkus kurung | `for x in range(5):` |

---

## Cara Menjalankan

```bash
# 1. Clone repo
git clone https://github.com/syuketa/python-untuk-pemula.git
cd python-untuk-pemula

# 2. Buat dan aktifkan virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS

# 3. Pasang dependency
pip install -r requirements.txt

# 4. Jalankan
python latihan.py
```

## Struktur Folder

```
python-untuk-pemula/
├── latihan.py          kode latihan semua materi
├── requirements.txt    daftar dependency
├── screenshots/        screenshot hasil output
├── .gitignore
└── README.md
```

## Konvensi Commit

Pesan commit memakai format [Conventional Commits](https://www.conventionalcommits.org) dalam bahasa Inggris:

```
feat(basics): add for and while loop examples
docs: update README with course progress
```

## Referensi

- Santrikoding: Python untuk Pemula, https://santrikoding.com
- Dokumentasi resmi Python, https://docs.python.org/3/





## Pengenalan dan Instalasi Python

Python adalah bahasa pemrograman tingkat tinggi yang mudah dibaca dan dipakai untuk web, otomasi, data, dan banyak bidang lain.

Cek versi Python yang terpasang:

```bash
python --version
```

Contoh hasil: `Python 3.14.7`

Jalankan program Python:

```bash
python latihan.py
```
