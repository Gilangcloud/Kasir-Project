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
    print("🚀 KASIR ( KENDALI ASET STOK INVENTORI RETAIL )")
    print("="*70)

    toko = Toko()
    toko.tambah_barang(Makanan("001", "Indomie", 3000, 100, "2026-12-31"))
    toko.tambah_barang(Minuman("002", "Aqua", 5000, 50, 600))
    toko.tambah_barang(KebutuhanRumahTangga("003", "Sabun", 10000, 20))

    toko.tambah_member(Member("M001", "Budi Santoso"))
    toko.tambah_member(Member("M002", "Gilang"))

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

                    if input("\nApakah Punya Member? (y/n): ").lower() == "y":
                            print("\n=== DAFTAR MEMBER TERSEDIA ===")
                            for i, m in enumerate(toko.member_list, 1):
                                print(f"{i}. {m.id_member} - {m.nama} (Poin: {m.poin})")
                            print(f"{len(toko.member_list) + 1}. Tambah Member Baru")

                            pilih = int(input("\nPilih member: "))
                            
                            if pilih <= len(toko.member_list):
                                member = toko.member_list[pilih - 1]
                            else:
                                id_baru = input("ID Member baru: ").strip().upper()
                                nama_baru = input("Nama Member baru: ").strip()
                                member = Member(id_baru, nama_baru)
                                toko.tambah_member(member) 
                                print(f"✅ Member {nama_baru} tersimpan di sistem!")

                            trans.member = member

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
                            poin_transaksi_ini = total_bayar // 10000
                            print(f"Poin didapat : +{poin_transaksi_ini} poin")
                        
                        print("="*50)
                        
                        if trans.member:
                            print(f"👤 Member: {trans.member.nama}")
                            print(f"✨ Total Poin : {trans.member.poin} poin")
                            
                        toko.transaksi_list.append(trans)
                        toko.laporan_stok()
                        break

                    except Exception as e:
                        print(f"❌ Terjadi kesalahan: {e}")
                        if input("\nMau mencoba transaksi lagi? (y/n): ").lower() != "y":
                            break

            elif pilihan == "3" and current_user.role in ["Administrator", "Owner"]:
                print("\n📦 === KELOLA BARANG ===")
                print("1. Tambah Stok Barang (Yang Sudah Ada)")
                print("2. Tambah Jenis Barang Baru")
                sub_pilihan = input("Pilih (1/2): ").strip()

                if sub_pilihan == "1":
                    # --- LOGIKA LAMA (TAMBAH STOK) ---
                    nama = input("Nama barang: ").strip()
                    barang = toko.cari_barang(nama)
                    if barang:
                        try:
                            jumlah = int(input(f"Jumlah stok (stok saat ini: {barang.stok}): "))
                            if jumlah <= 0:
                                print("❌ Jumlah harus lebih dari 0!")
                            else:
                                barang.tambah_stok(jumlah)
                                print(f"✅ Stok {barang.nama} berhasil ditambah {jumlah} unit")
                        except ValueError:
                            print("❌ Input jumlah harus berupa angka!")
                    else:
                        print("❌ Barang tidak ditemukan!")

                elif sub_pilihan == "2":
                    print("\n === TAMBAH JENIS BARANG BARU ===")
                    print("Kategori Tersedia:")
                    print("1. Makanan")
                    print("2. Minuman")
                    print("3. Kebutuhan Rumah Tangga")
                    kat = input("Pilih Kategori (1/2/3): ").strip()

                    if kat in ["1", "2", "3"]:
                        id_baru = f"{(len(toko.barang_list) + 1):03d}" 
                        nama_baru = input("Nama Barang Baru: ").strip()
                        
                        try:
                            harga_baru = int(input("Harga Jual (Rp): "))
                            stok_baru = int(input("Stok Awal: "))
                            
                            if kat == "1":
                                exp = input("Tanggal Kadaluarsa (YYYY-MM-DD): ").strip()
                                barang_baru = Makanan(id_baru, nama_baru, harga_baru, stok_baru, exp)
                            elif kat == "2":
                                vol = int(input("Volume (ml): "))
                                barang_baru = Minuman(id_baru, nama_baru, harga_baru, stok_baru, vol)
                            elif kat == "3":
                                barang_baru = KebutuhanRumahTangga(id_baru, nama_baru, harga_baru, stok_baru)
                            
                            toko.tambah_barang(barang_baru)
                            print(f"✅ Barang '{nama_baru}' (ID: {id_baru}) berhasil ditambahkan ke sistem!")
                            
                        except ValueError:
                            print("❌ Error: Pastikan input Harga, Stok, dan Volume berupa ANGKA!")
                    else:
                        print("❌ Kategori tidak valid!")
                else:
                    print("❌ Pilihan tidak valid!")

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

