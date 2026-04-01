class Member:
    def __init__(self, id_member: str, nama: str):
        self.id_member = id_member
        self.nama = nama
        self.poin = 0

    def tambah_poin(self, jumlah: int):
        self.poin += jumlah
