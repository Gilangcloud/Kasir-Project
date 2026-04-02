import unittest
from makanan import Makanan

class TestOOP(unittest.TestCase):
    def setUp(self):
        self.barang = Makanan("001", "Indomie", 3000, 100, "2026-12-31")

    def test_encapsulation(self):
        with self.assertRaises(AttributeError):
            _ = self.barang.__harga
        with self.assertRaises(AttributeError):
            _ = self.barang.__stok

    def test_transaksi_stok_berkurang(self):
        self.barang.kurangi_stok(10)
        self.assertEqual(self.barang.stok, 90)

    def test_info_polymorphism(self):
        self.assertIn("Makanan", self.barang.info())

if __name__ == "__main__":
    unittest.main(verbosity=2)