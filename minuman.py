from barang import Barang

class Minuman(Barang):
    def __init__(self, id_barang: str, nama: str, harga: int, stok: int, volume: int):
        super().__init__(id_barang, nama, harga, stok, "Minuman")
        self.volume = volume

    def info(self):
        return f" Minuman: {self.nama} | Rp{self.harga:,} | Stok: {self.stok} | {self.volume}ml"