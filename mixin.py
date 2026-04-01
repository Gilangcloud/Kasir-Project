from datetime import datetime

class LogMixin:
    def log(self, pesan: str):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] LOG: {pesan}")

class ValidasiMixin:
    @staticmethod
    def validasi_jumlah(jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        return True