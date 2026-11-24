
# Program Pengelolaan Nilai Mahasiswa

data_mahasiswa = []


# Fungsi menambahkan data
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ").strip().title()
    nilai = int(input("Masukkan nilai mahasiswa: "))

    mahasiswa = (nama, nilai)
    data_mahasiswa.append(mahasiswa)

    print("Data berhasil ditambahkan!")


# Fungsi menampilkan data
def tampilkan_mahasiswa():
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print("\n=== DAFTAR MAHASISWA ===")

        for mahasiswa in data_mahasiswa:
            nama, nilai = mahasiswa
            print(f"Nama: {nama} | Nilai: {nilai}")


# Fungsi menghitung rata-rata
def hitung_rata_rata():
    if len(data_mahasiswa) == 0:
        print("Belum ada data untuk dihitung.")
    else:
        total = 0

        for mahasiswa in data_mahasiswa:
            total += mahasiswa[1]

        rata_rata = total / len(data_mahasiswa)

        print(f"Rata-rata nilai: {rata_rata:.2f}")


# Fungsi mencari nilai tertinggi
def nilai_tertinggi():
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        tertinggi = data_mahasiswa[0]

        for mahasiswa in data_mahasiswa:
            if mahasiswa[1] > tertinggi[1]:
                tertinggi = mahasiswa

        print(f"Nilai tertinggi: {tertinggi[0]} ({tertinggi[1]})")


# Menu utama
while True:
    print("\n===== PENGELOLAAN NILAI MAHASISWA =====")
    print("1. Tambah mahasiswa")
    print("2. Tampilkan mahasiswa")
    print("3. Hitung rata-rata nilai")
    print("4. Cari nilai tertinggi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan == "2":
        tampilkan_mahasiswa()
    elif pilihan == "3":
        hitung_rata_rata()
    elif pilihan == "4":
        nilai_tertinggi()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
