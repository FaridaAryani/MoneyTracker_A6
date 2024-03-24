def pilih_kategori(daftar_kategori):
    """
    Meminta pengguna untuk memilih kategori dari daftar yang disediakan.

    Args:
        daftar_kategori (list): Daftar kategori yang tersedia.

    Returns:
        str: Kategori yang dipilih oleh pengguna.
    """
    print("Pilih Kategori:")
    for i, kategori in enumerate(daftar_kategori, 1):
        print(f"{i}. {kategori}")

    while True:
        pilihan = input("Masukkan nomor kategori: ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar_kategori):
                return daftar_kategori[pilihan - 1]
        print("Pilihan tidak valid. Silakan masukkan nomor kategori yang benar.")
