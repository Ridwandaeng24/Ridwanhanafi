nama = (input("Masukkan Nama Karyawan : "))
gaji_pokok = int(input("Masukkan Gaji Pokok : "))
jam_kerja = int(input("Masukkan Jam Kerja Harian: "))

print("\n")

print("NAMA KARYAWAN :",(nama))
print("GAJI POKOK :",(gaji_pokok))
print("JAM KERJA HARIAN :",(jam_kerja))

print("\n")

pilihan = int(input("Pilih Rincian Gaji harian / mingguan [1/2] : "))

print("\n")

if pilihan == 1 :
    gaji_harian = gaji_pokok / jam_kerja
    print("GAJI HARIAN : ",(gaji_harian))

elif pilihan == 2 :
    jam_kerja_per_minggu = int(input("Jumlah jam Kerja per Minggu: "))
    gaji_mingguan = gaji_pokok / (jam_kerja * jam_kerja_per_minggu)
    print("GAJI MINGGUAN : ",(gaji_mingguan ))

else:
    print("Pilihan tidak ada!")

print("\nTerima Kasih telah menggunakan program saya\n")
print("          NAMA : RIDWAN DAENG HANAFI             ")
print("          NPM  : 07352311113        \n")
