#Nama   : Reksi Hendra Pratama
#NPM    : G1A022032
#Kelas  : B

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.nama_jurusan)
# Kode diatas adalah kode yang untuk membuat class Mahasiswa beserta atributnya, atributnya ada nama, nim/npm an ada juga jurusan.
# Function tampilkan_info digunakan untuk menampilkan info mahasiswa.

class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa Jurusan", self.nama_jurusan)
        for mahasiswa in self.daftar_mahasiswa:
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)
            print("-----------------------")

# Kode diatas adalah kode yang untuk membuat class jurusan beserta atributnya, atributnya ada nama jurusan, dan daftar mahasiswa
# Function tampilkan_daftar_mahasiswa unutuk menampilkan daftar mahasiswa di suatu jurusan.
# Function tambah_mahasiswa digunakan untuk menambahkan mahasiswa di sebuah jurusan


class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print("Nama Jurusan: ", jurusan.nama_jurusan)
            print("-----------------------")

# Kode diatas adalah kode yang untuk membuat class jurusan beserta atributnya, atributnya ada nama universitas ,dan daftar jurusan.
# Function tampilkan_daftar_jurusan untuk menampilkan daftar jurusan di universitas.
# Function tambah_jurusan digunakan untuk menambah jurusan di class universitas


# Membuat objek Universitas
universitas = Universitas("XYZ University")

# Membuat objek Jurusan
jurusan_TI = Jurusan("Teknik Informatika")

# Menambahkan jurusan ke daftar jurusan pada objek Universitas
universitas.tambah_jurusan(jurusan_TI)

# Membuat objek Mahasiswa
mahasiswa_1 = Mahasiswa("Reksi Hendra Pratama", "G1A022032", jurusan_TI)

# Menambahkan mahasiswa ke daftar mahasiswa pada objek Jurusan
jurusan_TI.tambah_mahasiswa(mahasiswa_1)

# Menampilkan daftar jurusan pada objek Universitas XYZ
universitas.tampilkan_daftar_jurusan()

# Menampilkan informasi mahasiswa yang terdaftar di jurusan Teknik Informatika
jurusan_TI.tampilkan_daftar_mahasiswa()
