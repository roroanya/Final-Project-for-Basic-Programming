#Aureoliena Gainer 12024003124
#Linda Wati Purba 12024002321
#Raden Roro Anindya 12024002536

def tambah_siswa(data_siswa): 
    print("\n=== Tambah Data Siswa ===")
    while True:
        nama = input("Masukkan nama: ")
        if nama.isalpha():
            break
        else:
            print("Input tidak valid. Hanya boleh menggunakan huruf!")
    
    while True:
        Student_id = input("Masukkan Student id (hanya angka, 11 digit): ")
        if Student_id.isdigit() and 11 <= len(Student_id) <= 11:
            if any( siswa["Student_id"] == Student_id for siswa in data_siswa):
                print(f"Data dengan Student ID '{Student_id}' sudah ada. Tidak dapat menambahkan data yang sama.")        
                return
            break
        else:
            print("Student id harus berupa angka dengan panjang 11 digit.")
    
    print(f"Student id: {Student_id}")

    print("Pilihan Jurusan:")
    print("1. Teknik Mesin\n2. Teknik Industri\n3. Teknik Elektro\n4. Sistem Informasi")
    while True:
        pilihan_jurusan = input("Pilih jurusan (1-4): ")
        prodi = {
            "1": "Teknik Mesin",
            "2": "Teknik Industri",
            "3": "Teknik Elektro",
            "4": "Sistem Informasi"
        }
        jurusan = prodi.get(pilihan_jurusan)
        if jurusan:
            break
        else:
            print("Pilihan tidak valid, masukkan angka 1-4.")

    while True:
        try:
            semester = int(input("Semester: "))
            if semester < 1:
                print("Semester harus berupa angka positif.")
            elif semester > 14:
                print("Semester maksimal adalah 14.")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid untuk semester.")
    
    data_siswa.append({
        "Nama": nama,
        "Student_id": Student_id,
        "Jurusan": jurusan,
        "Semester": semester
    })

    print(f"Data siswa '{nama}' berhasil ditambahkan!")

def tampilkan_siswa(data_siswa):
    print("\n=== Data Siswa ===")
    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        i = 1  
        for siswa in data_siswa:
            print(f"{i}. Nama: {siswa['Nama']}, Student ID: {siswa['Student_id']}, "
                  f"Jurusan: {siswa['Jurusan']}, Semester: {siswa['Semester']}")
            i += 1  

def hapus_siswa(data_siswa):
    print("\n=== Hapus Data Siswa ===")
    Student_id = input("Masukkan Student ID  yang ingin dihapus: ")
    
    data_siswa_baru = [siswa for siswa in data_siswa if siswa["Student_id"] != Student_id]
    
    if len(data_siswa_baru) == len(data_siswa):
        print(f"Siswa dengan nama '{Student_id}' tidak ditemukan.")
    else:
        data_siswa[:] = data_siswa_baru 
        print(f"Data siswa '{Student_id}' berhasil dihapus!")

def cari_siswa(data_siswa):
    print("\n=== Cari Data Siswa ===")
    Student_id = input("Masukkan Student ID siswa yang ingin dicari: ")
    for siswa in data_siswa:
        if siswa["Student_id"] == Student_id:
            print(f"Data ditemukan:\n"
                  f"Nama: {siswa['Nama']}\n"
                  f"Student ID: {siswa['Student_id']}\n"
                  f"Jurusan: {siswa['Jurusan']}\n"
                  f"Semester: {siswa['Semester']}\n")
            return
    print(f"Siswa dengan Student ID '{Student_id}' tidak ditemukan.")

def main():
    data_siswa = []
    while True:
        print("\n=== Menu Data Siswa ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Cari Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa(data_siswa)
        elif pilihan == "2":
            tampilkan_siswa(data_siswa)
        elif pilihan == "3":
            hapus_siswa(data_siswa)
        elif pilihan == "4":
            cari_siswa(data_siswa)
        elif pilihan == "5":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()