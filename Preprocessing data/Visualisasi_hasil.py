import os
import cv2
import json
import numpy as np
from matplotlib import pyplot as plt

# ========== KONFIGURASI ==========
input_folder = 'Visualisasi Hasil\Data dan JSON_THORAX'           # Folder input berisi .png dan .json
output_folder = 'Visualisasi Hasil\Hasil'        # Folder output visualisasi


# ========== PROSES SETIAP PASANG GAMBAR & JSON ==========
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # Cek apakah ada file JSON dengan nama yang sama
        base_name = os.path.splitext(filename)[0]
        image_path = os.path.join(input_folder, filename)
        json_path = os.path.join(input_folder, base_name + '.json')
        
        if not os.path.exists(json_path):
            print(f"[SKIP] File JSON tidak ditemukan untuk: {filename}")
            continue
        
        # Load gambar dan JSON
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        with open(json_path, 'r') as f:
            data = json.load(f)

        # Gambar anotasi polygon dan titik
        for shape in data.get('shapes', []):
            label = shape['label']
            points = shape['points']
            pts = np.array(points, np.int32).reshape((-1, 1, 2))
            
            # Gambar garis polygon
            cv2.polylines(image_rgb, [pts], isClosed=True, color=(200, 0, 0), thickness=2)
            
            # Gambar titik-titik
            for point in points:
                x, y = int(point[0]), int(point[1])
                cv2.circle(image_rgb, (x, y), radius=3, color=(139, 0, 0), thickness=-1)

        # Simpan hasil
        output_path = os.path.join(output_folder, base_name + '_visualisasi.PNG')
        cv2.imwrite(output_path, cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
        print(f"[SUKSES] Disimpan ke: {output_path}")
