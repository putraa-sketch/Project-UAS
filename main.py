from data.barang import Barang
from data.keranjang import Keranjang
from view.menu import tampilkan_menu
from view.keranjang_view import tampilkan_keranjang, tampilkan_total

def proses_pilih_barang(barang_list):
    kode_barang = input("\nMasukkan kode barang yang ingin dibeli (atau 'exit' untuk keluar): ")

    if kode_barang.lower() == 'exit':
        return None

    for barang in barang_list:
        if barang.kode == kode_barang:
            return barang

    print("Kode barang tidak ditemukan, coba lagi.")
    return proses_pilih_barang(barang_list)


def proses_tambah_ke_keranjang(keranjang, barang):
    try:
        jumlah = int(input(f"Masukkan jumlah {barang.nama} yang ingin dibeli: "))
        if jumlah <= 0:
            print("Jumlah barang harus lebih dari 0.")
            return proses_tambah_ke_keranjang(keranjang, barang)
    except ValueError:
        print("Jumlah yang dimasukkan tidak valid, coba lagi.")
        return proses_tambah_ke_keranjang(keranjang, barang)

    keranjang.tambah_barang(barang, jumlah)


def main():
    barang_list = [
        Barang(kode="0011", nama="Adidas Manchester", harga=7000000),
        Barang(kode="0012", nama="Adidas Spezial Handbal", harga=2500000),
        Barang(kode="0013", nama="Adidas Bern", harga=4500000),
        Barang(kode="0014", nama="Stone Island Crewneck", harga=5000000),
        Barang(kode="0015", nama="Cargo Pants Napapijri", harga=3000000),
        Barang(kode="0016", nama="Backpack Fjallraven Kanken", harga=1500000),
        Barang(kode="0017", nama="Topi Barbour", harga=500000),
        Barang(kode="0018", nama="Jaket James Boogie", harga=3500000),
        Barang(kode="0019", nama="Polo Shirt Fred Perry", harga=750000),
        Barang(kode="0020", nama="Duffle Bag Lonsdale", harga=1750000),
        Barang(kode="0021", nama="New Balance x Stone Island", harga=9000000),
    ]

    keranjang = Keranjang()

    while True:
        tampilkan_menu(barang_list)
        barang = proses_pilih_barang(barang_list)

        if barang is None:
            break

        proses_tambah_ke_keranjang(keranjang, barang)

        lanjut = input("Apakah Anda ingin menambah barang lain? (y/n): ").strip().lower()
        while lanjut not in ['y', 'n']:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
            lanjut = input("Apakah Anda ingin menambah barang lain? (y/n): ").strip().lower()

        if lanjut == 'n':
            break

    tampilkan_keranjang(keranjang)
    tampilkan_total(keranjang)
    keranjang.cetak_struk()


if __name__ == "__main__":
    main()
