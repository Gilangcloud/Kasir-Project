from abc import ABC, abstractmethod
from mixin import LogMixin, ValidasiMixin

class Barang(ABC, LogMixin, ValidasiMixin):
    def __init__(self, id_barang: str, nama: str, harga: int, stok: int, kategori: str, harga_modal=None):
        self.__id_barang = id_barang
        self.nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__harga_modal = harga_modal or int(harga * 0.7)
        self.kategori = kategori

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai: int):
        if nilai <= 0:
            raise ValueError("Harga harus positif")
        self.__harga = nilai
        self.log(f"Harga {self.nama} diupdate menjadi Rp{nilai:,}")

    @property
    def stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah: int):
        self.validasi_jumlah(jumlah)
        if jumlah > self.__stok:
            raise ValueError(f"Stok {self.nama} tidak cukup!")
        self.__stok -= jumlah
        self.log(f"Stok {self.nama} berkurang {jumlah}, sisa {self.__stok}")

    def tambah_stok(self, jumlah: int):
        self.validasi_jumlah(jumlah)
        self.__stok += jumlah

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return self.info()