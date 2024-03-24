class Saldo:
    def __init__(self, username):
        self.username = username
        self.filepath = f"{self.username}_saldo.txt"
        self.saldo_cash = 0
        self.saldo_cashless = 0
        self.muat_saldo_dari_file()

    def tambah_saldo(self, jumlah, metode_pembayaran):
        if metode_pembayaran == "cash":
            self.saldo_cash += jumlah
        elif metode_pembayaran == "cashless":
            self.saldo_cashless += jumlah
        else:
            print("Metode pembayaran tidak valid.")
        self.simpan_saldo_ke_file()

    def cek_saldo_keseluruhan(self):
        return self.saldo_cash + self.saldo_cashless
    
    def cek_saldo_cash(self):
        return self.saldo_cash

    def cek_saldo_cashless(self):
        return self.saldo_cashless

    def kurangi_saldo(self, jumlah, metode_pembayaran):
        if metode_pembayaran == "cash":
            self.saldo_cash -= jumlah
        elif metode_pembayaran == "cashless":
            self.saldo_cashless -= jumlah
        else:
            print("Jenis saldo tidak valid.")
        self.simpan_saldo_ke_file()

    def simpan_saldo_ke_file(self):
        with open(self.filepath, "w") as file:
            file.write(f"cash: {self.saldo_cash}\n")
            file.write(f"cashless: {self.saldo_cashless}\n")

    def muat_saldo_dari_file(self):
        try:
            with open(self.filepath, "r") as file:
                for line in file:
                    jenis, jumlah = line.strip().split(': ')
                    if jenis == "cash":
                        self.saldo_cash = float(jumlah)
                    elif jenis == "cashless":
                        self.saldo_cashless = float(jumlah)
        except FileNotFoundError:
            print("File saldo tidak ditemukan.")
