def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        return diskon
    else:
        return None

def main():
    total_belanja = float(input("Masukkan total belanja: Rp "))
    diskon = hitung_diskon(total_belanja)

    if diskon:
        print("Diskon yang Anda dapatkan: Rp", diskon)
    else:
        print("Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000.")

if __name__ == "__main__":
    main()
