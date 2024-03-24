import datetime
from saldo import Saldo
from kategori import pilih_kategori

class CatatanTransaksi:
    def __init__(self, username):
        self.username = username
        self.saldo = Saldo(username)
        self.transactions = []
        self.filepath = f"{self.username}_transaksi.txt"

    def tambah_catatan(self, jenis, metode_pembayaran, jumlah):

        tanggal_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if jenis == "Pemasukan":
            daftar_kategori_Pemasukan = ["Investasi", "Gaji", "Upah", "Hadiah"]
            kategori_pemasukan = pilih_kategori(daftar_kategori_Pemasukan)
            self.transactions.append((tanggal_transaksi, jumlah, jenis, metode_pembayaran, kategori_pemasukan))
            self.saldo.tambah_saldo(jumlah, metode_pembayaran)
            self.saldo.simpan_saldo_ke_file()
        elif jenis == "Pengeluaran":
            daftar_kategori_Pengeluaran = ["Makanan", "Belanja", "Transportasi", "Hiburan"]
            kategori_pengeluaran = pilih_kategori(daftar_kategori_Pengeluaran)
            self.transactions.append((tanggal_transaksi, -jumlah, jenis, metode_pembayaran, kategori_pengeluaran))
            self.saldo.kurangi_saldo(jumlah, metode_pembayaran)
            self.saldo.simpan_saldo_ke_file()
        self.simpan_transaksi_ke_file(tanggal_transaksi, jenis, metode_pembayaran, jumlah, kategori_pengeluaran if jenis == "Pengeluaran" else kategori_pemasukan)

    def simpan_transaksi_ke_file(self, tanggal_transaksi, jenis, metode_pembayaran, jumlah, kategori):
        with open(self.filepath, "a") as file:
            file.write(f"{tanggal_transaksi}, {jenis}, {metode_pembayaran}, {jumlah}, {kategori}\n")

    def tampilkan_riwayat_transaksi(self):
        try:
            with open(self.filepath, "r") as file:
                print("Riwayat Transaksi:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("Tidak ada riwayat transaksi untuk pengguna ini.")

    def muat_transaksi_dari_file(self):
        try:
            with open(self.filepath, "r") as file:
                for line in file:
                    data_transaksi = line.strip().split(", ")
                    self.transactions.append(data_transaksi)
        except FileNotFoundError:
            print("File transaksi tidak ditemukan.")
