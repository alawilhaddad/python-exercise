# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan


# Definisikan class Perusahaan
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []

    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.append(karyawan)

    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = nama_karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.pop(nama_karyawan)


CEP = Perusahaan("Catur Elang Perkasa", "Margasatwa", "081")
k1 = Karyawan("Haddad", 27,5000,4000)
CEP.aktifkan_karyawan(k1)
print(CEP.list_karyawan[0].nama)
