import cv2
import os

# Ganti dengan path folder input dan output kamu
input_folder = 'X-ray'
output_folder = 'X-Ray Grayscale'

# Buat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Loop semua file PNG
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Baca gambar
        img = cv2.imread(input_path)

        if img is not None:
            # Ubah ke grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Simpan ke folder output
            cv2.imwrite(output_path, gray)
        else:
            print(f"Gagal membaca: {input_path}")

print("Semua gambar berhasil diubah ke grayscale dan disimpan di folder output.")