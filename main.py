from login import loginmain
from catatan import CatatanTransaksi
from saldo import Saldo
from rekap import rekap_harian, rekap_mingguan, rekap_bulanan, rekap_tahunan

def main():
    username = loginmain()
    saldo_obj = Saldo(username)
    catatan = CatatanTransaksi(username)
    catatan.muat_transaksi_dari_file()

    while True:
        print("\nPilih Operasi yang Ingin Dilakukan:")
        print("1. Tambah Saldo")
        print("2. Cek Saldo")
        print("3. Cek Saldo Keseluruhan")
        print("4. Tambah Catatan Transaksi")
        print("5. Tampilkan Riwayat Transaksi")
        print("6. Rekap Transaksi Harian")
        print("7. Rekap Transaksi Mingguan")
        print("8. Rekap Transaksi Bulanan")
        print("9. Rekap Transaksi Tahunan")
        print("10. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8/9/10): ")

        if pilihan == '1':
            amount = input("Masukkan jumlah saldo yang ingin ditambahkan: ")
            try:
                amount = float(amount)
                metode_pembayaran = input("Pilih metode pembayaran (cash/cashless): ").lower().strip()
                if metode_pembayaran == "cash":
                    saldo_obj.tambah_saldo_cash(amount)
                elif metode_pembayaran == "cashless":
                    saldo_obj.tambah_saldo_cashless(amount)
            except ValueError:
                print("Jumlah saldo tidak valid.")

        elif pilihan == '2':
            print("Saldo Cash:", saldo_obj.cek_saldo_cash())
            print("Saldo Cashless:", saldo_obj.cek_saldo_cashless())

        elif pilihan == '3':
            print("Saldo Keseluruhan:", saldo_obj.cek_saldo_keseluruhan())

        elif pilihan == '4':
            jenis = input("Jenis transaksi (Pemasukan/Pengeluaran): ")
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
                        catatan = CatatanTransaksi(username, {"Investasi", "Gaji", "Bonus", "Upah", "Hadiah"})
                        print("Pemasukan berhasil dicatat.")
                        saldo_obj.tambah_saldo_cash(amount)
                        is_valid = True
                        catatan.tambah_catatan(jenis, metode_pembayaran, amount, kategori)
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")
                elif metode_pembayaran == 'Cashless':
                    try:
                        amount = float(input("Masukkan jumlah pemasukan: "))
                        # Ubah bagian pembuatan objek catatan menjadi seperti berikut:
                        catatan = CatatanTransaksi(username, {"Investasi", "Gaji", "Bonus", "Upah", "Hadiah"})
                        print("Pemasukan berhasil dicatat.")
                        saldo_obj.tambah_saldo_cashless(amount)
                        is_valid = True
                        catatan.tambah_catatan(jenis, metode_pembayaran, amount, kategori)
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")

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
                        amount = float(input("Masukkan jumlah pengeluaran: "))
                        kategori = catatan.pilih_kategori(["Makanan", "Transportasi", "Hiburan", "Belanja", "Tagihan"])
                        print("Pengeluaran berhasil dicatat.")
                        saldo_obj.kurang_saldo_cash(amount)
                        is_valid = True
                        catatan.tambah_catatan(jenis, metode_pembayaran, amount, kategori)
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")
                elif metode_pembayaran == 'Cashless':
                    try:
                        amount = float(input("Masukkan jumlah pengeluaran: "))
                        kategori = catatan.pilih_kategori(["Makanan", "Transportasi", "Hiburan", "Belanja", "Tagihan"])
                        print("Pengeluaran berhasil dicatat.")
                        saldo_obj.kurang_saldo_cashless(amount)
                        is_valid = True
                        catatan.tambah_catatan(jenis, metode_pembayaran, amount, kategori)
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")

        elif pilihan == '5':
            catatan.tampilkan_riwayat_transaksi()

        elif pilihan == '6':
                # Meminta tanggal dari pengguna
                tanggal_str = input("Masukkan tanggal (format: YYYY-MM-DD), biarkan kosong untuk menggunakan tanggal saat ini: ")

                # Panggil fungsi rekap_harian dengan atau tanpa tanggal tergantung pada input pengguna
                if tanggal_str:
                    rekap_harian_result = rekap_harian(catatan.transactions, tanggal_str)
                else:
                    rekap_harian_result = rekap_harian(catatan.transactions)

                # Cetak hasil rekap harian
                print("Rekap Harian:")
                print(rekap_harian_result)

        elif pilihan == '7':
            rekap_mingguan_result = rekap_mingguan(catatan.transactions)
            print("Rekap Mingguan:")
            print(rekap_mingguan_result)

        elif pilihan == '8':
            rekap_bulanan_result = rekap_bulanan(catatan.transactions)
            print("Rekap Bulanan:")
            print(rekap_bulanan_result)

        elif pilihan == '9':
            rekap_tahunan_result = rekap_tahunan(catatan.transactions)
            print("Rekap Tahunan:")
            print(rekap_tahunan_result)

        elif pilihan == '10':
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 10.")

if __name__ == "__main__":
    main()
