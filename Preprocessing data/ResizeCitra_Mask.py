import cv2 # library untuk pengolahan citra
import os # library untuk operasi sistem file

input_dir = r'DATASET THORAX\Mask' # direktori input mask
output_dir = r'DATASET THORAX_Resize\Mask' # direktori output mask yang sudah diresize
for filename in os.listdir(input_dir): #iterasi setiap file dalam direktori input
    if filename.lower().endswith(('.png')): # hanya proses file dengan ekstensi .png
        img = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_GRAYSCALE) # baca citra dalam mode grayscale
        if img is not None:# pastikan citra berhasil dibaca
            resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_NEAREST) 
            ## meresize dengan interpolasi NEAREST untuk mask pada ukuran 256x256
            cv2.imwrite(os.path.join(output_dir, filename), resized) # simpan citra yang sudah diresize ke direktori output
            print(f"Sukses: {filename}") # konfirmasi sukses
        else: #jika gagal membaca citra (None)
            print(f"Gagal baca: {filename}")
