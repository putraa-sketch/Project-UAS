class Keranjang:
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, barang, jumlah):
        for b in self.barang_list:
            if b['barang'].kode == barang.kode:
                b['jumlah'] += jumlah
                return
        self.barang_list.append({'barang': barang, 'jumlah': jumlah})

    def hitung_total(self):
        total = 0
        for b in self.barang_list:
            total += b['barang'].harga * b['jumlah']
        return total

    def cetak_struk(self):
        print("\n==== STRUK BELANJA ====")
        for b in self.barang_list:
            barang = b['barang']
            total_harga = barang.harga * b['jumlah']
            print(f"{barang.nama:<20} x {b['jumlah']} = {total_harga}")
        print(f"\nTotal: {self.hitung_total()}")
        print("=======================")