import cv2 # librari untuk mengolah citra   
import os # untuk mengakses  sistem file

input_dir = r'DATASET THORAX\X-Ray' # direktori input citra X-Ray
output_dir = r'DATASET THORAX_Resize\X-Ray' # direktori output citra X-Ray yang sudah diresize
for filename in os.listdir(input_dir): #iterasi setiap file dalam direktori input
    if filename.lower().endswith(('.png')): # hanya memproses file dengan ekstensi .png
        img = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_GRAYSCALE) # membaca citra dalam mode grayscale
        if img is not None: # fungsi jika citra berhasil dibaca
            resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR) # 
            ## meresize dengan interpolasi Linear untuk citra X-Ray pada ukuran 256x256
            cv2.imwrite(os.path.join(output_dir, filename), resized) # menyimpan citra yang sudah diresize ke direktori output
            print(f"Sukses: {filename}") #konfirmasi bahwa citra berhasil diproses
        else: # fungsi jika citra gagal dibaca
            print(f"Gagal baca: {filename}")
