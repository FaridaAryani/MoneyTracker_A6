# tambahkan indeks untuk catatan
# tambahkan lihat catatan

class Saldo:
    """
    Class untuk mengelola saldo cash dan cashless, serta mencatat transaksi.
    """

    def __init__(self, cash=0, cashless=0):
        self.cash = cash
        self.cashless = cashless
        self.transactions = []

    def tambah_saldo(self, amount, metode_pembayaran):
        """
        Menambahkan saldo cash atau cashless.

        Args:
            amount (float): Jumlah saldo yang akan ditambahkan.
            metode_pembayaran (str): Jenis pembayaran ('cash' atau 'cashless').
        """
        if metode_pembayaran == "cash":
            self.cash += amount
        elif metode_pembayaran == "cashless":
            self.cashless += amount
        else:
            print("Metode pembayaran tidak valid.")

    def cek_saldo_cash(self):
        """
        Mengembalikan saldo cash saat ini.

        Returns:
            float: Saldo cash saat ini.
        """
        return self.cash

    def cek_saldo_cashless(self):
        """
        Mengembalikan saldo cashless saat ini.

        Returns:
            float: Saldo cashless saat ini.
        """
        return self.cashless

    def cek_saldo_keseluruhan(self):
        """
        Mengembalikan total saldo cash dan cashless.

        Returns:
            float: Total saldo cash dan cashless.
        """
        return self.cash + self.cashless


def print_login():
    """
    Mencetak logo program.
    """
    print("\t\t\t\t\t\t  _                 _       ")
    print("\t\t\t\t\t\t | |               (_)      ")
    print("\t\t\t\t\t\t | |     ___   __ _ _ _ __  ")
    print("\t\t\t\t\t\t | |    / _ \\ / _` | | '_ \\ ")
    print("\t\t\t\t\t\t | |___| (_) | (_| | | | | |")
    print("\t\t\t\t\t\t |______\\___/ \\__, |_|_| |_|")
    print("\t\t\t\t\t\t               __/ |        ")
    print("\t\t\t\t\t\t              |___/         ")
    print("\t\t\t\t\t\t    ==========================  \n\n")


def login():
    """
    Meminta input username dan password untuk login.
    """
    print_login()
    username = input("username:")
    password = input("password:")
    # Di sini bisa dilakukan validasi login, misalnya dengan database user, namun untuk tujuan contoh, saya biarkan saja.


def tambah_saldo(saldo):
    """
    Menambahkan saldo cash atau cashless.

    Args:
        saldo (Saldo): Objek Saldo.
    """
    is_saldo_valid = False

    while not is_saldo_valid:
        metode_pembayaran = input("Pilih metode pembayaran (cash/cashless): ").strip().lower().title()

        if metode_pembayaran == "Cash" or metode_pembayaran == "Cashless":
            is_saldo_valid = True
        else:
            print("Jenis tidak valid. Silakan masukkan 'Cash' atau 'Cashless'.")

    if metode_pembayaran == 'Cash':
        amount = float(input("Masukkan jumlah saldo cash yang ingin ditambahkan: "))
        saldo.tambah_saldo(amount, "cash")
        print("Saldo cash berhasil ditambahkan.")
    elif metode_pembayaran == 'Cashless':
        amount = float(input("Masukkan jumlah saldo cashless yang ingin ditambahkan: "))
        saldo.tambah_saldo(amount, "cashless")
        print("Saldo cashless berhasil ditambahkan.")


def tambah_catatan(saldo):
    """
    Menambahkan catatan pemasukan atau pengeluaran.

    Args:
        saldo (Saldo): Objek Saldo.
    """
    is_valid = False

    while not is_valid:
        jenis = input("Masukkan jenis (Pemasukan/Pengeluaran): ").strip().lower().title()

        if jenis == "Pemasukan" or jenis == "Pengeluaran":
            is_valid = True
        else:
            print("Jenis tidak valid. Silakan masukkan 'Pemasukan' atau 'Pengeluaran'.")

    if jenis == "Pemasukan":
        is_valid = False
        while not is_valid:
            metode_pembayaran = input("Pilih metode pembayaran (cash/cashless): ").strip().lower().title()
            if metode_pembayaran == "Cash" or metode_pembayaran == "Cashless":
                is_valid = True
            else:
                print("Metode tidak valid. Silakan masukkan 'Cash' atau 'Cashless'.")

        if metode_pembayaran == 'Cash':
            try:
                amount = float(input("Masukkan jumlah pemasukan: "))
                saldo.tambah_saldo(amount, "cash")
                kategori = pilih_kategori(["Investasi", "Gaji", "Bonus", "Upah", "Hadiah"])
                saldo.transactions.append((amount, "Pemasukan - Cash", metode_pembayaran, kategori))  # Menyimpan kategori produk dalam transaksi
                print("Pemasukan berhasil dicatat.")
                is_valid = True
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif metode_pembayaran == 'Cashless':
            try:
                amount = float(input("Masukkan jumlah pemasukan: "))
                saldo.tambah_saldo(amount, "cashless")
                kategori = pilih_kategori(["Investasi", "Gaji", "Bonus", "Upah", "Hadiah"])
                saldo.transactions.append((amount, "Pemasukan - Cashless", metode_pembayaran, kategori))  # Menyimpan kategori produk dalam transaksi
                print("Pemasukan berhasil dicatat.")
                is_valid = True
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

    elif jenis == "Pengeluaran":
        is_valid = False

    while not is_valid:
        jenis = input("Masukkan jenis (Pemasukan/Pengeluaran): ").strip().lower().title()

        if jenis == "Pemasukan" or jenis == "Pengeluaran":
            is_valid = True
        else:
            print("Jenis tidak valid. Silakan masukkan 'Pemasukan' atau 'Pengeluaran'.")

    if jenis == "Pengeluaran":
        is_valid = False
        while not is_valid:
            metode_pembayaran = input("Pilih metode pembayaran (cash/cashless): ").strip().lower().title()
            if metode_pembayaran == "Cash" or metode_pembayaran == "Cashless":
                is_valid = True
            else:
                print("Metode tidak valid. Silakan masukkan 'Cash' atau 'Cashless'.")

        if metode_pembayaran == 'Cash':
            try:
                amount = float(input("Masukkan jumlah pemasukan: "))
                saldo.tambah_saldo(amount, "cash")
                kategori = pilih_kategori(["Makanan", "Transportasi", "Hiburan", "Belanja", "Tagihan"])
                saldo.transactions.append((amount, "Pemasukan - Cash", metode_pembayaran, kategori))  # Menyimpan kategori produk dalam transaksi
                print("Pemasukan berhasil dicatat.")
                is_valid = True
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif metode_pembayaran == 'Cashless':
            try:
                amount = float(input("Masukkan jumlah pemasukan: "))
                saldo.tambah_saldo(amount, "cashless")
                kategori = pilih_kategori(["Makanan", "Transportasi", "Hiburan", "Belanja", "Tagihan"])
                saldo.transactions.append((amount, "Pemasukan - Cashless", metode_pembayaran, kategori))  # Menyimpan kategori produk dalam transaksi
                print("Pemasukan berhasil dicatat.")
                is_valid = True
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")


def hapus_catatan(saldo):
    """
    Menghapus catatan transaksi berdasarkan ID.

    Args:
        saldo (Saldo): Objek Saldo.
    """
    try:
        entry_id = int(input("Masukkan ID: "))
        if entry_id <= 0 or entry_id > len(saldo.transactions):
            print("ID tidak valid.")
        else:
            entry_id -= 1
            del saldo.transactions[entry_id]
            print("Catatan telah dihapus.")
            print_semua_transaksi(saldo)
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")


def print_semua_transaksi(saldo):
    """
    Mencetak semua catatan transaksi.

    Args:
        saldo (Saldo): Objek Saldo.
    """
    if not saldo.transactions:
        print("Tidak ada catatan transaksi.")
    else:
        for i, (amount, jenis, metode_pembayaran, kategori) in enumerate(saldo.transactions, start=1):
            print(f"ID: {i}, Jumlah saldo: {amount}, Jenis: {jenis}, Metode Pembayaran:{metode_pembayaran}, Kategori Produk: {kategori}")

def grup_transaksi_per_tahun():
    try:
        with open('transaction.txt', 'r') as file:
            total_year = [0] * 100

            for line in file:
                day, month, year, amount = map(int, line.strip().split(','))
                total_year[year % 100] += amount
            
            print("Rekap Transaksi per Tahun:")
            for i, total in enumerate(total_year):
                if total > 0:
                    print(f"Tahun 20{i:02d}: {total}")
    
    except FileNotFoundError:
        print(f"Error: Tidak bisa membuka file!")

def grup_transaksi_per_bulan():
    try:
        with open('transaction.txt', 'r') as file:
            total_month = [0] * 12

            for line in file:
                day, month, year, amount = map(int, line.strip().split(','))
                total_month[month - 1] += amount

            print("Rekap Transaksi per Bulan:")
            for i, total in enumerate(total_month):
                if total > 0:
                    print(f"Bulan {i + 1}: {total}")

    except FileNotFoundError:
        print(f"Error: Tidak bisa membuka file!")

def grup_transaksi_per_hari():
    try:
        with open('transaction.txt', 'r') as file:
            total_day = [0] * 31

            for line in file:
                day, month, year, amount = map(int, line.strip().split(','))
                total_day[day - 1] += amount

            print("Rekap Transaksi per Hari:")
            for i, total in enumerate(total_day):
                if total > 0:
                    print(f"Hari {i + 1}: {total}")

    except FileNotFoundError:
        print(f"Error: Tidak bisa membuka file!")

def pilih_kategori(kategori_produk):
    """
    Prosedur untuk meminta pengguna memilih kategori produk dari daftar kategori yang tersedia.
    
    Args:
        kategori_produk (dict): Dictionary yang berisi daftar kategori produk.
    """
    # Menampilkan daftar kategori
    print("Daftar Kategori Produk:")
    for kategori in kategori_produk:
        print("-", kategori)

    while True:
        # Meminta pengguna untuk memilih kategori
        kategori_input = input("Pilih kategori produk: ")

        # Memvalidasi input pengguna
        if kategori_input in kategori_produk:
            print("Kategori yang dipilih:", kategori_input)
            return kategori_input
        else:
            print("Kategori tidak valid. Silakan pilih dari daftar kategori yang tersedia.")


def main():
    login()
    saldo = Saldo()

    while True:
        print("\nPilih Operasi yang Ingin Dilakukan:")
        print("1. Tambah Saldo")
        print("2. Cek Saldo")
        print("3. Cek Saldo Keseluruhan")
        print("4. Tambah Catatan")
        print("5. Lihat Catatan")
        print("6. Hapus Catatan")
        print("7. Rekap per Tahun")
        print("8. Rekap per Bulan")
        print("9. Rekap per Hari")
        print("10. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8/9/10): ")

        if pilihan == '1':
            tambah_saldo(saldo)
        elif pilihan == '2':
            print("Saldo Cash:", saldo.cek_saldo_cash())
            print("Saldo Cashless:", saldo.cek_saldo_cashless())
        elif pilihan == '3':
            print("Saldo Keseluruhan:", saldo.cek_saldo_keseluruhan())
        elif pilihan == '4':
            tambah_catatan(saldo)
        elif pilihan == '5':
            print_semua_transaksi(saldo)
        elif pilihan == '6':
            hapus_catatan(saldo)
        elif pilihan == '7':
            grup_transaksi_per_tahun()
        elif pilihan == '8':
            grup_transaksi_per_bulan()
        elif pilihan == '9':
            grup_transaksi_per_hari()
        elif pilihan == '10':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 10.")


if __name__ == "__main__":
    main()