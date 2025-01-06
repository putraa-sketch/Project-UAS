class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.kode} | {self.nama} | {self.harga}"