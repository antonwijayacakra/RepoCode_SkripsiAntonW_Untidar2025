import json # library untuk mengolah file JSON
import cv2 # library untuk mengolah citra
import numpy as np # library untuk mengolah citra
import matplotlib.pyplot as plt # library untuk mengolah citra
import os # untuk mengakses sistem file 
import re # library untuk  mencari pola dalam string


base_dir = r'Coba' # direktori tempat menyimpan file JSON dan PNG
mask_dir = r'Mask' # direktori untuk menyimpan mask
xray_dir = r'X-Ray' # direktori untuk menyimpan gambar X-Ray


# Fungsi untuk membuat nama file mask dengan mengganti awalan dengan "mask" dan mempertahankan nomornya
def buat_nama_mask(nama_file_json): 
    match = re.search(r'\((\d+)\)', nama_file_json) # mencari pola nomor dalam tanda kurung
    if match: # jika ditemukan nomor dalam tanda kurung
        nomor = match.group(1) # ambil nomor tersebut
        return f'mask_Data ({nomor}).PNG' # buat nama file mask dengan format "mask_Data (nomor).PNG"
    else: 
        return 'mask.PNG' # jika tidak ditemukan nomor, gunakan nama default 'mask.PNG'

# Ambil semua file dari folder yang ditentukan
daftar_file = os.listdir(base_dir)

# Pisahkan file berdasarkan ekstensi
file_json = {nama: os.path.join(base_dir, nama) for nama in daftar_file if nama.endswith('.json')} # file_JSON sebagai dictionary
file_gambar = {nama: os.path.join(base_dir, nama) for nama in daftar_file if nama.endswith('.png')}

# Proses setiap pasangan file JSON dan PNG
for nama_json, path_json in file_json.items():
    # Nama file gambar yang terkait
    nama_gambar = nama_json.replace('.json', '.png')

    if nama_gambar in file_gambar: # jika file gambar yang sesuai ditemukan
        # Buat nama file mask keluaran
        nama_mask = buat_nama_mask(nama_json)
        path_mask_lengkap = os.path.join(mask_dir, nama_mask)

        # Cek apakah file mask sudah ada
        if os.path.exists(path_mask_lengkap):
            print(f'Dilewati {nama_json}: Mask sudah ada di {path_mask_lengkap}.')
            continue

        try:
            # Baca file JSON
            with open(path_json, 'r') as file_json_obj:
                anotasi = json.load(file_json_obj) # memuat konten file JSON

            # Baca file gambar
            gambar = cv2.imread(file_gambar[nama_gambar]) # membaca gambar X-Ray
            if gambar is None: #jika tidak berhasil di baca
                print(f"Kesalahan: Gagal memuat gambar {file_gambar[nama_gambar]}. Lewati file ini.")  # jika gambar tidak ditemukan
                continue # tetap lanjutkan ke iterasi berikutnya

            # Ambil dimensi gambar
            tinggi, lebar, _ = gambar.shape

            # Inisialisasi mask kosong
            mask = np.zeros((tinggi, lebar), dtype=np.uint8)

            # Proses setiap bentuk di file JSON
            for bentuk in anotasi['shapes']:
                if bentuk['shape_type'] == 'polygon':
                    titik = bentuk['points']
                    titik = np.array(titik, dtype=np.int32).reshape((-1, 1, 2))
                    # Isi area poligon di dalam mask dengan warna putih (1)
                    cv2.fillPoly(mask, [titik], color=1)

            # Simpan file mask ke folder yang ditentukan
            plt.imsave(path_mask_lengkap, mask, cmap='gray', format='png')

            # Simpan gambar asli ke folder X-ray
            path_gambar_asli = os.path.join(xray_dir, nama_gambar)
            cv2.imwrite(path_gambar_asli, gambar) # Simpan gambar asli ke folder X-ray

            print(f'Mask disimpan di: {path_mask_lengkap}')
            print(f'Gambar asli disimpan di: {path_gambar_asli}')
        except Exception as e:
            print(f"Terjadi kesalahan saat memproses {nama_json}: {e}")
    else:
        print(f"Peringatan: Tidak ditemukan gambar yang cocok untuk {nama_json}. Lewati file JSON ini.")