from makanan import Makanan
from minuman import Minuman
from kebutuhan_rumah_tangga import KebutuhanRumahTangga
from transaksi import Transaksi

class Toko:
    def __init__(self):
        self.barang_list = []      
        self.transaksi_list = []   

    def tambah_barang(self, barang):
        """Menambahkan barang baru ke toko"""
        self.barang_list.append(barang)

    def cari_barang(self, nama: str):
        """Mencari barang berdasarkan nama (case insensitive)"""
        for barang in self.barang_list:
            if barang.nama.lower() == nama.lower():
                return barang
        return None

    def laporan_stok(self):
        """Menampilkan laporan stok semua barang"""
        print("\n" + "="*60)
        print("📦 LAPORAN STOK BARANG")
        print("="*60)
        if not self.barang_list:
            print("Belum ada barang di toko.")
            return

        for b in self.barang_list:
            print(b)   

    def laporan_transaksi(self):
        """Menampilkan laporan semua transaksi"""
        print("\n" + "="*60)
        print("📋 LAPORAN TRANSAKSI")
        print("="*60)
        if not self.transaksi_list:
            print("Belum ada transaksi.")
            return

        for t in self.transaksi_list:
            print(f"ID: {t.id_transaksi} | Total: Rp{t.total:,}")