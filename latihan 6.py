# Data autentikasi mahasiswa
# visca barca
data_mahasiswa = {
    "username": "ridwan daeng hanafi",
    "password": "24042003"
}

# Data mata kuliah dan dosen pengampuh
data_matkul = {
    "Pemrograman": "pak ysair",
    "logika matematika": "pak amal",
    "arsikom": "Pak cheko"
}

def autentikasi():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == data_mahasiswa["username"] and password == data_mahasiswa["password"]:
        return True
    else:
        return False

def main():
    if autentikasi():
        print("Autentikasi berhasil!")
        print("Silakan input mata kuliah dan dosen pengampuh:")
        
        mata_kuliah = input("Masukkan nama mata kuliah: ")

        if mata_kuliah in data_matkul:
            print(f"Dosen pengampuh mata kuliah {mata_kuliah} adalah {data_matkul[mata_kuliah]}")
        else:
            print("Mata kuliah tidak ditemukan.")
    else:
        print("Autentikasi gagal! Username atau password salah.")

if __name__ == "__main__":
    main()
