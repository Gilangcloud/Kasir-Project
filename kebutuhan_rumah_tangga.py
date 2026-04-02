from barang import Barang

class KebutuhanRumahTangga(Barang):
    def __init__(self, id_barang: str, nama: str, harga: int, stok: int):
        super().__init__(id_barang, nama, harga, stok, "Kebutuhan Rumah Tangga")

    def info(self):
        return f"Kebutuhan Rumah Tangga: {self.nama} | Rp{self.harga:,} | Stok: {self.stok}"