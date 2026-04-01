from barang import Barang

class Makanan(Barang):
    def __init__(self, id_barang: str, nama: str, harga: int, stok: int, kadaluarsa: str):
        super().__init__(id_barang, nama, harga, stok, "Makanan")
        self.kadaluarsa = kadaluarsa

    def info(self):
        return f" Makanan: {self.nama} | Rp{self.harga:,} | Stok: {self.stok} | Kadaluarsa: {self.kadaluarsa}"