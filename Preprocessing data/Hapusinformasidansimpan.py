import cv2 # Library OpenCV untuk pemrosesan gambar
import os # Library untuk operasi sistem seperti membaca file dan direktori
import numpy as np # Library untuk operasi numerik

# Koordinat area informasi pasien (ubah sesuai kebutuhan)
x1, y1 = 0, 0 # Koordinat kiri atas 
x2, y2 = 190, 80 # Koordinat kanan bawah

# Fungsi untuk menghapus informasi pasien
def hapus_Informasipasien(img_path): 
    img = cv2.imread(img_path) # Baca gambar dari path yang diberikan
    label_area = img[y1:y2+1, x1:x2+1] # Ekstrak area yang berisi informasi pasien
    avg_color = label_area.mean(axis=(0, 1)).astype(np.uint8) # Hitung warna rata-rata di area tersebut
    img[y1:y2+1, x1:x2+1] = avg_color # Ganti area informasi pasien dengan warna rata-rata
    return img  # simpan sebagai  gambar yang telah diproses

# Fungsi untuk memproses dan menyimpan gambar sebagai .PNG
def proses_dan_simpan_gambar(input_folder, output_folder): # fungsi untuk memproses dan menyimpan gambar
    counter = 1 # Inisialisasi counter untuk penomoran file output
    for filename in os.listdir(input_folder): # Loop melalui semua file dalam folder input
        # Hanya proses file dengan ekstensi .jpg atau .JPG
        if filename.lower().endswith('.jpg'):# Cek ekstensi file 
            input_path = os.path.join(input_folder, filename) # Dapatkan path lengkap file input
            output_filename = f"data ({counter}).PNG" # Buat nama file output dengan format "data (n).PNG"
            output_path = os.path.join(output_folder, output_filename) # Dapatkan path lengkap file output

            processed_img = hapus_Informasipasien(input_path) ## Simpan gambar yang telah diproses
            cv2.imwrite(output_path, processed_img) ## Simpan gambar yang telah diproses dalam format PNG

            print(f"Gambar diproses dan disimpan: {output_filename}")
            counter += 1

    print("Selesai! Semua file .JPG berhasil diproses dan disimpan sebagai .PNG.")


input_folder = r'Data Ori Thorax\01_01_2024'   # direktori input yang berisi gambar .JPG
output_folder = 'coba' # direktori output untuk menyimpan gambar yang telah diproses
proses_dan_simpan_gambar(input_folder, output_folder) #Panggil fungsi untuk memproses dan menyimpan gambar
