class Member:
    def _init_(self, id_member: str, nama: str):
        self.id_member = id_member
        self.nama = nama
        self.poin = 0

    def tambah_poin(self, jumlah: int):
        self.poin += jumlah