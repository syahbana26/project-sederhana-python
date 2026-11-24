# Pengelolaan Nilai Mahasiswa

Program **Pengelolaan Nilai Mahasiswa** adalah aplikasi sederhana
berbasis Python untuk menyimpan dan mengelola nilai mahasiswa melalui
menu pada terminal.

Program ini dibuat sebagai latihan penerapan dasar-dasar Python,
khususnya string, list, tuple, fungsi, perulangan, dan percabangan.

## Fitur Program

1.  **Tambah mahasiswa** --- memasukkan nama dan nilai mahasiswa.
2.  **Tampilkan mahasiswa** --- menampilkan seluruh data yang sudah
    dimasukkan.
3.  **Hitung rata-rata nilai** --- menghitung rata-rata dari seluruh
    nilai mahasiswa.
4.  **Cari nilai tertinggi** --- mencari mahasiswa dengan nilai paling
    tinggi.
5.  **Keluar** --- menghentikan program.

## Konsep Python yang Digunakan

  -----------------------------------------------------------------------
  Konsep                              Penjelasan dalam Program
  ----------------------------------- -----------------------------------
  String                              Menyimpan nama mahasiswa dan
                                      pilihan menu.

  List                                Variabel `data_mahasiswa` digunakan
                                      untuk menampung banyak data
                                      mahasiswa.

  Tuple                               Setiap mahasiswa disimpan sebagai
                                      pasangan `(nama, nilai)`.

  Fungsi                              Fitur program dipisahkan ke dalam
                                      fungsi `tambah_mahasiswa()`,
                                      `tampilkan_mahasiswa()`,
                                      `hitung_rata_rata()`, dan
                                      `nilai_tertinggi()`.

  Perulangan `for`                    Mengakses data mahasiswa untuk
                                      ditampilkan dan dihitung.

  Perulangan `while`                  Menjaga menu utama tetap berjalan
                                      sampai pengguna memilih keluar.

  Percabangan `if`, `elif`, dan       Menentukan tindakan berdasarkan
  `else`                              pilihan pengguna dan memeriksa
                                      apakah data tersedia.
  -----------------------------------------------------------------------

## Penjelasan Alur Kode

### 1. Menyiapkan tempat penyimpanan data

``` python
data_mahasiswa = []
```

List kosong ini digunakan untuk menyimpan data mahasiswa yang dimasukkan
selama program berjalan.

### 2. Menambahkan data mahasiswa

Fungsi `tambah_mahasiswa()` meminta pengguna memasukkan nama dan nilai.
Nama dirapikan menggunakan `strip()` dan `title()`, kemudian nama dan
nilai digabungkan menjadi tuple dan ditambahkan ke dalam list dengan
`append()`.

### 3. Menampilkan data mahasiswa

Fungsi `tampilkan_mahasiswa()` memeriksa apakah list masih kosong. Jika
ada data, program menggunakan perulangan `for` untuk menampilkan nama
dan nilai setiap mahasiswa.

### 4. Menghitung rata-rata nilai

Fungsi `hitung_rata_rata()` menjumlahkan seluruh nilai mahasiswa,
kemudian membaginya dengan jumlah data mahasiswa. Hasil ditampilkan
dengan dua angka di belakang koma.

### 5. Mencari nilai tertinggi

Fungsi `nilai_tertinggi()` menggunakan data pertama sebagai nilai
tertinggi sementara. Program kemudian membandingkan nilai setiap
mahasiswa dan memperbarui data tertinggi jika menemukan nilai yang lebih
besar.

### 6. Menjalankan menu utama

Perulangan `while True` menampilkan menu secara berulang. Pengguna
memilih fitur dengan memasukkan angka 1 sampai 5. Jika memilih angka 5,
perintah `break` menghentikan perulangan dan mengakhiri program.

## Cara Menjalankan Program

1.  Pastikan Python sudah terpasang di komputer.
2.  Simpan kode program dalam file bernama `main.py`.
3.  Buka terminal pada folder tempat file disimpan.
4.  Jalankan perintah berikut:

``` bash
python main.py
```

5.  Pilih menu sesuai fitur yang ingin digunakan.

## Contoh Penggunaan

``` text
===== PENGELOLAAN NILAI MAHASISWA =====
1. Tambah mahasiswa
2. Tampilkan mahasiswa
3. Hitung rata-rata nilai
4. Cari nilai tertinggi
5. Keluar

Pilih menu (1-5): 1
Masukkan nama mahasiswa: budi
Masukkan nilai mahasiswa: 85
Data berhasil ditambahkan!

Pilih menu (1-5): 3
Rata-rata nilai: 85.00
```

## Catatan

-   Data hanya disimpan sementara di dalam list selama program berjalan.
-   Ketika program ditutup, data yang dimasukkan akan hilang karena
    program belum menggunakan database atau penyimpanan file.
-   Program ini merupakan proyek latihan dasar Python dan dapat
    dikembangkan lebih lanjut, misalnya dengan fitur pencarian nama,
    pengubahan data, penghapusan data, dan penyimpanan permanen.

## Tujuan Pembelajaran

Melalui program ini, pembuat berlatih menggabungkan beberapa konsep
dasar Python menjadi sebuah aplikasi sederhana yang memiliki fungsi dan
alur penggunaan yang jelas.
