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

    toko = Toko()
    toko.tambah_barang(Makanan("001", "Indomie", 3000, 100, "2026-12-31"))
    toko.tambah_barang(Minuman("002", "Aqua", 5000, 50, 600))
    toko.tambah_barang(KebutuhanRumahTangga("003", "Sabun", 10000, 20))

    while True:
        current_user = None

        while current_user is None:
            current_user = login()

            if not current_user:
                print("\n❌ Username atau password salah!")

                pilihan = input("\nMau coba login lagi? (y/n): ").strip().lower()

                if pilihan == "y":
                    continue
                else:
                    print("\nAnda memilih untuk tidak login lagi.")
                    konfirmasi = input("Apakah Anda yakin ingin keluar dari program? (y/n): ").strip().lower()
                    
                    if konfirmasi == "y":
                        print("👋 Terima kasih telah menggunakan sistem. Sampai jumpa!")
                        exit()
                    else:
                        print("🔄 Kembali ke halaman login...")
                        continue  

            else:
                print(f"\n✅ Login berhasil! Selamat datang, {current_user.role.upper()} {current_user.username.upper()}")
                break   

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
                print("5. Logout")
            elif current_user.role == "Administrator":
                print("4. Logout")
            else:  
                print("3. Logout")

            pilihan = input("\nPilih menu (1-5): ").strip()

            if pilihan == "1":
                toko.laporan_stok()

            elif pilihan == "2":
                while True:
                    print("\n💰 === TRANSAKSI BARU ===")
                    trans = Transaksi(f"TRX-{len(toko.transaksi_list) + 1:04d}")
                    item_count = 0

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
                            if jumlah <= 0:
                                print("❌ Jumlah harus lebih dari 0!")
                                continue
                            trans.tambah_item(barang, jumlah)
                            print(f"✅ {jumlah} {barang.nama} ditambahkan ke keranjang")
                            item_count += 1
                        except ValueError:
                            print("❌ Input jumlah harus berupa angka!")

                    if item_count == 0:
                        print("❌ Transaksi dibatalkan karena tidak ada barang yang dimasukkan.")
                        if input("\nMau membuat transaksi baru lagi? (y/n): ").lower() != "y":
                            break
                        continue

                    if input("\nApakah pelanggan member? (y/n): ").lower() == "y":
                        print("\nDaftar Member Tersedia:")
                        print("1. M001 - Budi Santoso")
                        print("2. M002 - Gilang")
                        print("3. Tambah Member Baru")

                        pilihan_member = input("\nPilih member (1/2/3): ").strip()

                        if pilihan_member == "1":
                            member = Member("M001", "Budi Santoso")
                        elif pilihan_member == "2":
                            member = Member("M002", "Gilang")
                        elif pilihan_member == "3":
                            id_baru = input("Masukkan ID Member baru: ").strip().upper()
                            nama_baru = input("Masukkan Nama Member: ").strip()
                            member = Member(id_baru, nama_baru)
                            print(f"✅ Member baru {nama_baru} berhasil dibuat")
                        else:
                            print("❌ Pilihan tidak valid, menggunakan default.")
                            member = Member("M001", "Budi Santoso")

                        trans.member = member
                        print(f"✅ Member aktif: {member.nama} (ID: {member.id_member})")

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
                        break

                    except Exception as e:
                        print(f"❌ Terjadi kesalahan: {e}")
                        if input("\nMau mencoba transaksi lagi? (y/n): ").lower() != "y":
                            break

            elif pilihan == "3" and current_user.role in ["Administrator", "Owner"]:
                print("\n📦 === TAMBAH STOK ===")
                nama = input("Nama barang: ").strip()
                barang = toko.cari_barang(nama)
                if barang:
                    try:
                        jumlah = int(input(f"Jumlah stok yang ditambahkan (stok saat ini: {barang.stok}): "))
                        if jumlah <= 0:
                            print("❌ Jumlah harus lebih dari 0!")
                        else:
                            barang.tambah_stok(jumlah)
                            print(f"✅ Stok {barang.nama} berhasil ditambah {jumlah} unit")
                    except ValueError:
                        print("❌ Input jumlah harus berupa angka!")
                else:
                    print("❌ Barang tidak ditemukan!")

            elif pilihan == "4" and current_user.role == "Owner":
                print("\n🔑 === HARGA MODAL (TERENKRIPSI) ===")
                for b in toko.barang_list:
                    print(f"{b.nama:15} → Harga Modal: Rp{b.get_harga_modal():,}")

            elif (pilihan == "5" and current_user.role == "Owner") or \
                (pilihan == "4" and current_user.role == "Administrator") or \
                (pilihan == "3" and current_user.role == "Kasir"):
                
                print(f"\n👋 Logout berhasil, {current_user.role} {current_user.username.upper()}!")
                
                pilihan_logout = input("\nApa yang ingin Anda lakukan?\n1. Ganti Akun\n2. Keluar Program\nPilih (1/2): ").strip()
                
                if pilihan_logout == "1":
                    print("\n🔄 Mengalihkan ke halaman login...")
                    break   
                else:
                    print("👋 Terima kasih telah menggunakan sistem. Sampai jumpa!")
                    exit()

            else:
                print("❌ Pilihan tidak valid atau tidak diizinkan untuk role anda.")

