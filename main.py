from makanan import Makanan
from minuman import Minuman
from kebutuhan_rumah_tangga import KebutuhanRumahTangga
from transaksi import Transaksi
from toko import Toko


def tambah_barang_interaktif(toko: Toko):
    jenis = input("Jenis barang (Makanan/Minuman/KebutuhanRumahTangga): ")
    kode = input("Kode barang: ")
    nama = input("Nama barang: ")

    try:
        harga = int(input("Harga barang: "))
        stok = int(input("Stok barang: "))
    except ValueError:
        print("Input harga/stok harus angka. Gagal menambah barang.")
        return

    jenis_normal = jenis.strip().lower().replace(" ", "")

    if jenis_normal == "makanan":
        kadaluarsa = input("Tanggal kadaluarsa (YYYY-MM-DD): ")
        toko.tambah_barang(Makanan(kode, nama, harga, stok, kadaluarsa))
    elif jenis_normal == "minuman":
        try:
            volume = int(input("Volume minuman (ml): "))
        except ValueError:
            print("Volume harus angka. Gagal menambah barang.")
            return
        toko.tambah_barang(Minuman(kode, nama, harga, stok, volume))
    elif jenis_normal in ("kebutuhanrumahtangga", "kebutuhanrumah" , "kebutuhanrumah tangga"):
        toko.tambah_barang(KebutuhanRumahTangga(kode, nama, harga, stok))
    else:
        print("Jenis barang tidak valid.")


def proses_transaksi_interaktif(toko: Toko):
    id_transaksi = input("ID transaksi: ")
    if not id_transaksi:
        print("ID transaksi tidak boleh kosong.")
        return

    barang_nama = input("Nama barang yang akan dibeli: ")
    barang = toko.cari_barang(barang_nama)
    if not barang:
        print("Barang tidak ditemukan.")
        return

    try:
        jumlah = int(input("Jumlah pembelian: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    transaksi = Transaksi(id_transaksi)

    try:
        transaksi.tambah_item(barang, jumlah)
    except ValueError as e:
        print("Transaksi gagal: ", e)
        return

    total = transaksi.proses_transaksi()
    toko.transaksi_list.append(transaksi)
    print(f"Transaksi berhasil. Total bayar: Rp{total:,}")


if __name__ == "__main__":
    print("selamat datang di toko kami")
    toko = Toko()

    toko.tambah_barang(Makanan("036355D", "Indomie", 5000, 80, "2026-12-31"))
    toko.tambah_barang(Makanan("036378G", "Intermi", 3000, 50, "2025-10-01"))
    toko.tambah_barang(Minuman("036378K", "Coca-Cola", 10000, 50, 330))
    toko.tambah_barang(KebutuhanRumahTangga("036789Y", "Sabun", 15000, 60))

    while True:
        print("\nMenu:")
        print("1. Lihat semua barang")
        print("2. Tambah barang")
        print("3. Lakukan transaksi")
        print("4. Laporan transaksi")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            toko.laporan_stok()
        elif pilihan == "2":
            tambah_barang_interaktif(toko)
        elif pilihan == "3":
            proses_transaksi_interaktif(toko)
        elif pilihan == "4":
            toko.laporan_transaksi()
        elif pilihan == "5":
            print("Terima kasih telah berbelanja di toko kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

