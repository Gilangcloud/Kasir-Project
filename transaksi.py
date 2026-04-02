from barang import Barang
from member import Member
from promo import Promo

class Transaksi:
    def __init__(self, id_transaksi: str):
        self.id_transaksi = id_transaksi
        self.daftar_item = []   
        self.total = 0
        self.member: Member | None = None
        self.promo: Promo | None = None

    def tambah_item(self, barang: Barang, jumlah: int):
        barang.kurangi_stok(jumlah)
        subtotal = barang.harga * jumlah
        self.daftar_item.append((barang, jumlah, subtotal))
        self.total += subtotal

    def apply_promo(self, promo: Promo):
        self.promo = promo

    def proses_transaksi(self) -> int:
        if self.promo:
            self.total -= self.promo.hitung_diskon(self.total)
        if self.member:
            self.member.tambah_poin(self.total // 10000)
        return self.total