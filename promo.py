class Promo:
    def __init__(self, kode_promo: str, diskon: float):
        self.kode_promo = kode_promo
        self.diskon = diskon
        self.aktif = True

    def hitung_diskon(self, total: int):
        return int(total * self.diskon) if self.aktif else 0
