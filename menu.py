def tampilkan_menu(barang_list):
        print("\nDaftar Barang yang Tersedia:")
        print("+", "=" * 44, "+")
        print(f"|{'Kode':<10} | {'Nama':<20} | {'Harga':<10}|")
        print("+", "=" * 44, "+")
        for barang in barang_list:
            print(f"|{barang.kode:<10} | {barang.nama:<20} | {barang.harga:<10}|")
        print("+", "-" * 44, "+")