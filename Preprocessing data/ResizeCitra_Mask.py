import cv2
import os

input_dir = r'DATASET THORAX\Mask'
output_dir = r'DATASET THORAX_Resize\Mask'
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png')):
        img = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_NEAREST)
            ## meresize dengan interpolasi NEAREST untuk mask pada ukuran 256x256
            cv2.imwrite(os.path.join(output_dir, filename), resized)
            print(f"Sukses: {filename}")
        else:
            print(f"Gagal baca: {filename}")
