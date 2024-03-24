from datetime import datetime, timedelta

# def rekap_harian(transactions, selected_date=None):
#     """
#     Merekap transaksi per hari.

#     Args:
#         transactions (list): Daftar transaksi.
#         selected_date (str, optional): Tanggal yang dipilih dalam format 'YYYY-MM-DD'. Jika tidak ditentukan, gunakan tanggal saat ini.

#     Returns:
#         dict: Rekap transaksi per hari.
#     """
#     rekap = {}
#     if selected_date is None:
#         selected_date = datetime.now().strftime('%Y-%m-%d')
    
#     selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    
#     valid_transactions_exist = False  # Flag untuk memeriksa apakah ada transaksi yang valid
    
#     for transaksi in transactions:
#         try:
#             tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
#             if tanggal == selected_date:
#                 jumlah = float(transaksi[3])  # Mengambil jumlah transaksi dari kolom keempat
#                 rekap[tanggal] = rekap.get(tanggal, 0) + jumlah
#                 valid_transactions_exist = True  # Setidaknya satu transaksi valid ada untuk tanggal yang dipilih
#         except ValueError:
#             print("Transaksi:", transaksi)
    
#     if not valid_transactions_exist:
#         print("Tidak ada transaksi yang terjadi pada tanggal", selected_date)
#     else:
#         print("Rekap Transaksi Harian untuk Tanggal", selected_date)
#         print("====================================")
#         for tanggal, total in rekap.items():
#             print(f"{tanggal.strftime('%Y-%m-%d')}: Rp{total:.2f}")

#     return rekap

# def rekap_mingguan(transactions):
#     """
#     Merekap transaksi per minggu.

#     Args:
#         transactions (list): Daftar transaksi.

#     Returns:
#         dict: Rekap transaksi per minggu.
#     """
#     rekap = {}
#     for transaksi in transactions:
#         try:
#             tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
#             minggu_awal = tanggal - timedelta(days=tanggal.weekday())
#             minggu_akhir = minggu_awal + timedelta(days=6)
#             minggu = (minggu_awal, minggu_akhir)
#             rekap[minggu] = rekap.get(minggu, 0) + float(transaksi[3])  # Konversi jumlah transaksi ke floating point
#         except ValueError:
#             print("Transaksi:", transaksi)
    
#     print("Rekap Transaksi Mingguan")
#     print("========================")
#     for minggu, total in rekap.items():
#         print(f"{minggu[0].strftime('%Y-%m-%d')} - {minggu[1].strftime('%Y-%m-%d')}: Rp{total:.2f}")

#     return rekap

# def rekap_bulanan(transactions):
#     """
#     Merekap transaksi per bulan.

#     Args:
#         transactions (list): Daftar transaksi.

#     Returns:
#         dict: Rekap transaksi per bulan.
#     """
#     rekap = {}
#     for transaksi in transactions:
#         try:
#             tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
#             bulan = tanggal.replace(day=1)
#             rekap[bulan] = rekap.get(bulan, 0) + float(transaksi[3])  # Konversi jumlah transaksi ke floating point
#         except ValueError:
#             print("Transaksi:", transaksi)
    
#     print("Rekap Transaksi Bulanan")
#     print("========================")
#     for bulan, total in rekap.items():
#         print(f"{bulan.strftime('%Y-%m')}: Rp{total:.2f}")

#     return rekap

# def rekap_tahunan(transactions):
#     """
#     Merekap transaksi per tahun.

#     Args:
#         transactions (list): Daftar transaksi.

#     Returns:
#         dict: Rekap transaksi per tahun.
#     """
#     rekap = {}
#     for transaksi in transactions:
#         try:
#             tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
#             tahun = tanggal.replace(month=1, day=1)
#             rekap[tahun] = rekap.get(tahun, 0) + float(transaksi[3])  # Konversi jumlah transaksi ke floating point
#         except  ValueError:
#             print("Transaksi:", transaksi)
    
#     print("Rekap Transaksi Tahunan")
#     print("========================")
#     for tahun, total in rekap.items():
#         print(f"Tahun {tahun.year}: Rp{total:.2f}")

#     return rekap


from collections import defaultdict

def rekap_harian(transactions, selected_date=None):
    rekap = defaultdict(float)
    if selected_date is None:
        selected_date = datetime.now().strftime('%Y-%m-%d')
    
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    
    for transaksi in transactions:
        try:
            tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
            if tanggal == selected_date:
                jumlah = float(transaksi[3])
                rekap[tanggal] += jumlah
        except ValueError:
            print("Transaksi tidak valid:", transaksi)
    
    if not rekap:
        print("Tidak ada transaksi yang terjadi pada tanggal", selected_date)
    else:
        print("Rekap Transaksi Harian untuk Tanggal", selected_date)
        print("====================================")
        for tanggal, total in rekap.items():
            print(f"{tanggal.strftime('%Y-%m-%d')}: Rp{total:.2f}")

    return dict(rekap)

def rekap_mingguan(transactions):
    rekap = defaultdict(float)
    for transaksi in transactions:
        try:
            tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
            minggu_awal = tanggal - timedelta(days=tanggal.weekday())
            minggu_akhir = minggu_awal + timedelta(days=6)
            minggu = (minggu_awal, minggu_akhir)
            rekap[minggu] += float(transaksi[3])
        except ValueError:
            print("Transaksi tidak valid:", transaksi)
    
    print("Rekap Transaksi Mingguan")
    print("========================")
    for minggu, total in rekap.items():
        print(f"{minggu[0].strftime('%Y-%m-%d')} - {minggu[1].strftime('%Y-%m-%d')}: Rp{total:.2f}")

    return dict(rekap)

def rekap_bulanan(transactions):
    rekap = defaultdict(float)
    for transaksi in transactions:
        try:
            tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
            bulan = tanggal.replace(day=1)
            rekap[bulan] += float(transaksi[3])
        except ValueError:
            print("Transaksi tidak valid:", transaksi)
    
    print("Rekap Transaksi Bulanan")
    print("========================")
    for bulan, total in rekap.items():
        print(f"{bulan.strftime('%Y-%m')}: Rp{total:.2f}")

    return dict(rekap)

def rekap_tahunan(transactions):
    rekap = defaultdict(float)
    for transaksi in transactions:
        try:
            tanggal = datetime.strptime(transaksi[0], "%Y-%m-%d %H:%M:%S").date()
            tahun = tanggal.replace(month=1, day=1)
            rekap[tahun] += float(transaksi[3])
        except ValueError:
            print("Transaksi tidak valid:", transaksi)
    
    print("Rekap Transaksi Tahunan")
    print("========================")
    for tahun, total in rekap.items():
        print(f"Tahun {tahun.year}: Rp{total:.2f}")

    return dict(rekap)
