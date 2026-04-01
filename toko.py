from makanan import Makanan
from minuman import Minuman
from kebutuhan_rumah_tangga import KebutuhanRumahTangga
from transaksi import Transaksi

class Toko:
    def __init__(self):
        self.barang_list = []
        self.transaksi_list = []

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    def cari_barang(self, nama: str):
        for b in self.barang_list:
            if b.nama.lower() == nama.lower():
                return b
        return None

    def laporan_stok(self):
        print("\n=== LAPORAN STOK BARANG ===")
        for b in self.barang_list:
            print(b)

    def laporan_transaksi(self):
        print("\n=== LAPORAN TRANSAKSI ===")
        for t in self.transaksi_list:
            print(f"ID: {t.id_transaksi} | Total: Rp{t.total:,}")
