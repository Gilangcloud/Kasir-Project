from toko import Toko
from makanan import Makanan
from minuman import Minuman
from kebutuhan_rumah_tangga import KebutuhanRumahTangga
from member import Member
from promo import Promo
from transaksi import Transaksi
from auth import login

if __name__ == "__main__":
    print("="*70)
    print("🚀 SISTEM TOKO SWALAYAN OOP + LOGIN + ROLE + ENKRIPSI")
    print("="*70)

    current_user = login()
    if not current_user:
        print("❌ Login gagal. Program dihentikan.")
        exit()

    toko = Toko()
    toko.tambah_barang(Makanan("001", "Indomie", 3000, 100, "2026-12-31"))
    toko.tambah_barang(Minuman("002", "Aqua", 5000, 50, 600))
    toko.tambah_barang(KebutuhanRumahTangga("003", "Sabun", 10000, 20))

    print(f"\n✅ Selamat datang, {current_user.role} {current_user.username.upper()}!")

    while True:
        print("\n" + "="*70)
        print(f"👤 ROLE: {current_user.role} | USER: {current_user.username.upper()}")
        print("="*70)

        print("1. Lihat Stok Barang")
        
        if current_user.role in ["Administrator", "Owner", "Kasir"]:
            print("2. Transaksi Baru")
        
        if current_user.role in ["Administrator", "Owner"]:
            print("3. Tambah Stok Barang")
        
        if current_user.role == "Owner":
            print("4. Lihat Harga Modal (Enkripsi)")
            print("5. Keluar")
        elif current_user.role == "Administrator":
            print("4. Keluar")
        else:  
            print("3. Keluar")

        pilihan = input("\nPilih menu (1-5): ").strip()

        if pilihan == "1":
            toko.laporan_stok()

        elif pilihan == "2":
            print("\n💰 === TRANSAKSI BARU ===")
            trans = Transaksi(f"TRX-{len(toko.transaksi_list) + 1:04d}")

            while True:
                nama = input("\nNama barang (kosong = selesai): ").strip()
                if not nama:
                    break

                barang = toko.cari_barang(nama)
                if not barang:
                    print("❌ Barang tidak ditemukan!")
                    continue

                try:
                    jumlah = int(input(f"Jumlah {barang.nama} (stok saat ini: {barang.stok}): "))
                    trans.tambah_item(barang, jumlah)
                    print(f"✅ {jumlah} {barang.nama} ditambahkan ke keranjang")
                except ValueError as e:
                    print(f"❌ Error: {e}")

            if input("\nApakah pelanggan member? (y/n): ").lower() == "y":
                member = Member("M001", "Budi Santoso")
                trans.member = member
                print(f"✅ Member {member.nama} aktif")

            if input("Gunakan promo? (y/n): ").lower() == "y":
                kode = input("Masukkan kode promo: ").strip().upper()
                if kode == "DISKON10":
                    promo = Promo("DISKON10", 0.10)
                    trans.apply_promo(promo)
                    print("✅ Promo 10% diterapkan")
                else:
                    print("❌ Kode promo tidak valid")

            try:
                total_bayar = trans.proses_transaksi()
                print("\n" + "="*50)
                print("✅ TRANSAKSI BERHASIL!")
                print(f"ID Transaksi : {trans.id_transaksi}")
                print(f"Total Bayar  : Rp{total_bayar:,}")
                if trans.member:
                    print(f"Poin didapat : {trans.member.poin}")
                print("="*50)

                toko.transaksi_list.append(trans)
                toko.laporan_stok()   
            except Exception as e:
                print(f"❌ Terjadi kesalahan: {e}")

        elif pilihan == "3" and current_user.role in ["Administrator", "Owner"]:
            print("\n📦 === TAMBAH STOK ===")
            nama = input("Nama barang: ").strip()
            barang = toko.cari_barang(nama)
            if barang:
                try:
                    jumlah = int(input(f"Jumlah stok yang ditambahkan (stok saat ini: {barang.stok}): "))
                    barang.tambah_stok(jumlah)
                    print(f"✅ Stok {barang.nama} berhasil ditambah {jumlah} unit")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            else:
                print("❌ Barang tidak ditemukan!")

        elif pilihan == "4" and current_user.role == "Owner":
            print("\n🔑 === HARGA MODAL (TERENKRIPSI) ===")
            for b in toko.barang_list:
                print(f"{b.nama:15} → Harga Modal: Rp{b.get_harga_modal():,}")

        elif (pilihan == "5" and current_user.role == "Owner") or \
            (pilihan == "4" and current_user.role == "Administrator") or \
            (pilihan == "3" and current_user.role == "Kasir"):
            print(f"\n👋 Logout berhasil. Terima kasih, {current_user.role}!")
            break

        else:
            print("❌ Pilihan tidak valid atau tidak diizinkan untuk role anda.")

    print("\nProgram selesai. Semoga presentasi kalian mendapat nilai 100! 🎉")