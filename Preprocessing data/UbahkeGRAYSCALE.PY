import cv2 # library untuk mengolah citra
import os # untuk mengakses sistem file

# Ganti dengan path folder input dan output kamu
input_folder = 'X-ray' # Folder input yang berisi gambar X-Ray
output_folder = 'X-Ray Grayscale' # Folder output untuk menyimpan gambar grayscale

# Buat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True) 

# Loop semua file PNG
for filename in os.listdir(input_folder): # iterasi setiap file dalam direktori input
    if filename.lower().endswith('.png'): # hanya memproses file dengan ekstensi .png
        input_path = os.path.join(input_folder, filename) # path lengkap file input yang diakses 
        output_path = os.path.join(output_folder, filename) # path lengkap file output yang diakses
        # Baca gambar
        img = cv2.imread(input_path) # membaca citra

        if img is not None: # fungsi jika citra berhasil dibaca
            # Ubah ke grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Simpan ke folder output
            cv2.imwrite(output_path, gray)
        else: # fungsi jika citra gagal dibaca
            print(f"Gagal membaca: {input_path}") 

print("Semua gambar berhasil diubah ke grayscale dan disimpan di folder output.")