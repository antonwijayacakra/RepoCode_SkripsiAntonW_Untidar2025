import cv2
import os
import numpy as np

# Koordinat area informasi pasien (ubah sesuai kebutuhan)
x1, y1 = 0, 0
x2, y2 = 190, 80

# Fungsi untuk menghapus informasi pasien
def hapus_Informasipasien(img_path):
    img = cv2.imread(img_path)
    label_area = img[y1:y2+1, x1:x2+1]
    avg_color = label_area.mean(axis=(0, 1)).astype(np.uint8)
    img[y1:y2+1, x1:x2+1] = avg_color
    return img

# Fungsi untuk memproses dan menyimpan gambar sebagai .PNG
def proses_dan_simpan_gambar(input_folder, output_folder):
    counter = 1
    for filename in os.listdir(input_folder):
        # Hanya proses file dengan ekstensi .jpg atau .JPG
        if filename.lower().endswith('.jpg'):
            input_path = os.path.join(input_folder, filename)
            output_filename = f"data ({counter}).PNG"
            output_path = os.path.join(output_folder, output_filename)

            processed_img = hapus_Informasipasien(input_path) ## Simpan gambar yang telah diproses
            cv2.imwrite(output_path, processed_img) ## Simpan gambar yang telah diproses dalam format PNG

            print(f"Gambar diproses dan disimpan: {output_filename}")
            counter += 1

    print("Selesai! Semua file .JPG berhasil diproses dan disimpan sebagai .PNG.")


input_folder = r'Data Ori Thorax\01_01_2024'   
output_folder = 'coba'
proses_dan_simpan_gambar(input_folder, output_folder) #Panggil fungsi untuk memproses dan menyimpan gambar
