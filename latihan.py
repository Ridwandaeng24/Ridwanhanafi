def integer_to_binary(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

angka = int(input("masukkan angka bulat: "))
hasil = integer_to_binary(angka)
print("representasi biner dari", angka, "adalah", hasil)