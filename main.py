from toko import Toko
from makanan import Makanan
from minuman import Minuman
from kebutuhan_rumah_tangga import KebutuhanRumahTangga
from member import Member
from promo import Promo
from transaksi import Transaksi

if __name__ == "__main__":
    print("SELAMAT DATANG DI KASIR")
    toko = Toko()

    toko.tambah_barang(Makanan("001", "Indomie", 3000, 100, "2026-12-31"))
    toko.tambah_barang(Minuman("002", "Aqua", 5000, 50, 600))
    toko.tambah_barang(KebutuhanRumahTangga("003", "Sabun", 10000, 20))

    while True:
        print("\n" + "="*50)
        print("1. Lihat Stok Barang")
        print("2. Transaksi Baru")
        print("3. Tambah Stok Barang")
        print("4. Keluar")
        print("="*50)
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            toko.laporan_stok()

        elif pilihan == "2": 
            print("\n === TRANSAKSI BARU ===")
            trans = Transaksi(f"TRX-{len(toko.transaksi_list) + 1:04d}")

            # Tambah barang ke transaksi (bisa lebih dari 1 item)
            while True:
                nama = input("\nNama barang (kosong untuk selesai): ").strip()
                if not nama:
                    break

                barang = toko.cari_barang(nama)
                if not barang:
                    print(" Barang tidak ditemukan!")
                    continue

                try:
                    jumlah = int(input(f"Jumlah {barang.nama} (stok saat ini: {barang.stok}): "))
                    trans.tambah_item(barang, jumlah)
                    print(f" {jumlah} {barang.nama} ditambahkan ke keranjang")
                except ValueError as e:
                    print(f" Error: {e}")

            
            if input("\nApakah pelanggan member? (y/n): ").lower() == "y":
                member = Member("M001", "Budi Santoso")   
                trans.member = member
                print(f"Member {member.nama} terdaftar")

            if input("Gunakan promo? (y/n): ").lower() == "y":
                kode = input("Masukkan kode promo: ").strip().upper()
                if kode == "DISKON10":
                    promo = Promo("DISKON10", 0.10)
                    trans.apply_promo(promo)
                    print(" Promo 10% berhasil diterapkan")
                else:
                    print(" Kode promo tidak valid")

            try:
                total_bayar = trans.proses_transaksi()
                print("\n" + "="*40)
                print(" TRANSAKSI BERHASIL!")
                print(f"ID Transaksi : {trans.id_transaksi}")
                print(f"Total Bayar  : Rp{total_bayar:,}")
                if trans.member:
                    print(f"Poin didapat : {trans.member.poin}")
                print("="*40)

                toko.transaksi_list.append(trans)
                toko.laporan_stok()   # tampilkan stok setelah transaksi
            except Exception as e:
                print(f" Terjadi kesalahan: {e}")

        elif pilihan == "3":  # ==================== TAMBAH STOK ====================
            print("\n === TAMBAH STOK BARANG ===")
            nama = input("Nama barang yang akan ditambah stok: ").strip()
            barang = toko.cari_barang(nama)

            if not barang:
                print(" Barang tidak ditemukan!")
            else:
                try:
                    jumlah = int(input(f"Masukkan jumlah stok baru untuk {barang.nama} (stok saat ini: {barang.stok}): "))
                    barang.tambah_stok(jumlah)
                    print(f" Stok {barang.nama} berhasil ditambah {jumlah} unit")
                    print(f"   Stok sekarang: {barang.stok}")
                except ValueError as e:
                    print(f" Error: {e}")

        elif pilihan == "4":
            print("\n Terima kasih telah menggunakan Sistem Toko Swalayan OOP!")
            print("Semoga presentasi kalian mendapat nilai 100! 🎉")
            break

        else:
            print(" Pilihan tidak valid! Silakan pilih 1-4.")