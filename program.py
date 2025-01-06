class Data:
    class Barang:
        def __init__(self, kode, nama, harga):
            self.kode = kode
            self.nama = nama
            self.harga = harga

        def __str__(self):
            return f"{self.kode} | {self.nama} | {self.harga}"

    class Keranjang:
        def __init__(self):
            self.barang_list = []

        def tambah_barang(self, barang, jumlah):
            for b in self.barang_list:
                if b['barang'].kode == barang.kode:
                    b['jumlah'] += jumlah
                    return
            self.barang_list.append({'barang': barang, 'jumlah': jumlah})

        def tampilkan_barang(self):
            if not self.barang_list:
                print("Keranjang kosong.")
            else:
                print("Daftar Barang dalam Keranjang:")
                print(f"{'Kode':<10} {'Nama':<20} {'Harga':<10} {'Jumlah':<10}")
                for b in self.barang_list:
                    barang = b['barang']
                    print(f"{barang.kode:<10} {barang.nama:<20} {barang.harga:<10} {b['jumlah']:<10}")

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

        def __str__(self):
            if not self.barang_list:
                return "Keranjang kosong."
            result = ["Daftar Barang dalam Keranjang:", f"{'Kode':<10} {'Nama':<20} {'Harga':<10} {'Jumlah':<10}"]
            for b in self.barang_list:
                barang = b['barang']
                result.append(f"{barang.kode:<10} {barang.nama:<20} {barang.harga:<10} {b['jumlah']:<10}")
            return "\n".join(result)


class View:
    @staticmethod
    def tampilkan_menu(barang_list):
        print("\nDaftar Barang yang Tersedia:")
        print("+", "=" * 44, "+")
        print(f"|{'Kode':<10} | {'Nama':<20} | {'Harga':<10}|")
        print("+", "=" * 44, "+")
        for barang in barang_list:
            print(f"|{barang.kode:<10} | {barang.nama:<20} | {barang.harga:<10}|")
        print("+", "-" * 44, "+")


class Process:
    @staticmethod
    def proses_pilih_barang(barang_list):
        kode_barang = input("\nMasukkan kode barang yang ingin dibeli (atau 'exit' untuk keluar): ")

        if kode_barang.lower() == 'exit':
            return None

        for barang in barang_list:
            if barang.kode == kode_barang:
                return barang

        print("Kode barang tidak ditemukan, coba lagi.")
        return Process.proses_pilih_barang(barang_list)

    @staticmethod
    def proses_tambah_ke_keranjang(keranjang, barang):
        try:
            jumlah = int(input(f"Masukkan jumlah {barang.nama} yang ingin dibeli: "))
            if jumlah <= 0:
                print("Jumlah barang harus lebih dari 0.")
                return Process.proses_tambah_ke_keranjang(keranjang, barang)
        except ValueError:
            print("Jumlah yang dimasukkan tidak valid, coba lagi.")
            return Process.proses_tambah_ke_keranjang(keranjang, barang)

        keranjang.tambah_barang(barang, jumlah)


def main():
    barang_list = [
        Data.Barang(kode="0011", nama="Adidas Manchester", harga=7000000),
        Data.Barang(kode="0012", nama="Adidas Spezial Handbal", harga=2500000),
        Data.Barang(kode="0013", nama="Adidas Bern", harga=4500000),
        Data.Barang(kode="0014", nama="Stone Island Crewneck", harga=5000000),
        Data.Barang(kode="0015", nama="Cargo Pants Napapijri", harga=3000000),
        Data.Barang(kode="0016", nama="Backpack Fjallraven Kanken", harga=1500000),
        Data.Barang(kode="0017", nama="Topi Barbour", harga=500000),
        Data.Barang(kode="0018", nama="Jaket James Boogie", harga=3500000),
        Data.Barang(kode="0019", nama="Polo Shirt Fred Perry", harga=750000),
        Data.Barang(kode="0020", nama="Duffle Bag Lonsdale", harga=1750000),
        Data.Barang(kode="0021", nama="New Balance x Stone Island", harga=9000000),
    ]

    keranjang = Data.Keranjang()

    while True:
        View.tampilkan_menu(barang_list)
        barang = Process.proses_pilih_barang(barang_list)

        if barang is None:
            break

        Process.proses_tambah_ke_keranjang(keranjang, barang)

        lanjut = input("Apakah Anda ingin menambah barang lain? (y/n): ").strip().lower()
        while lanjut not in ['y', 'n']:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
            lanjut = input("Apakah Anda ingin menambah barang lain? (y/n): ").strip().lower()

        if lanjut == 'n':
            break

    print(keranjang)

    total = keranjang.hitung_total()
    print(f"\nTotal Harga: {total}")

    keranjang.cetak_struk()


if __name__ == "__main__":
    main()