import numpy as np # librari untuk komputasi numerik dan mengolah array
import tensorflow as tf # librari untuk deep learning dan evaluasi model
import cv2 # librari untuk pengolahan citra
from tensorflow.keras.models import load_model # librari untuk load model
import matplotlib.pyplot as plt # librari untuk visualisasi data

# 1. Load model
model = load_model('Model AI_Fix/U-Net.h5')

# 2. Fungsi preprocessing
def inisiasicitra(input_citra):
    img = cv2.imread(input_citra, cv2.IMREAD_GRAYSCALE)  # baca citra dalam grayscale
    img_array = img / 255.0 # normalisasi
    img_array = np.reshape(img_array, (1, 256, 256, 1)) # ubah menjadi bentuk 4 dimensi
    return img_array, img 

# 3. Path input dan mask ground truth
input_citra = r'Data Pengujian Komputasi_Resize\1 Data\X-Ray\Data  (1062).png'
input_mask  = r'Data Pengujian Komputasi_Resize\1 Data\Mask\mask_Data (1062).PNG'

# 4. Prediksi
data_citra, img = inisiasicitra(input_citra) # panggil fungsi preprocessing
prediction = model.predict(data_citra) # prediksi model
mask_pred = np.reshape(prediction, (256, 256)) # ubah bentuk prediksi menjadi 2 dimensi 
#mask_pred = np.squeeze(prediction)  # hilangkan dimensi channel dan jumlah batch    
mask_pred = (mask_pred > 0.5).astype(np.uint8) 
#cv2.imwrite('hasil_prediksi.png', mask_pred*255) # simpan hasil prediksi sebagai citra

# 5. Ground truth
mask_gt = cv2.imread(input_mask, cv2.IMREAD_GRAYSCALE) #membaca citra ground truth
mask_gt = (mask_gt / 255.0).astype(np.uint8) # normalisasi & binerisasi

# 6. Flatten data
y_true = mask_gt.flatten() # flatkan data ground truth menjadi 1D
y_pred = mask_pred.flatten() # flatkan data prediksi menjadi 1D

# 7. Hitung confusion matrix pakai TensorFlow
matrix_evaluasi_model = tf.math.confusion_matrix(y_true, y_pred, num_classes=2) #ekstrak confusion matrix untuk 2 kelas
matrix_evaluasi_model = matrix_evaluasi_model.numpy()  # ubah ke numpy array

TN, FP, FN, TP = matrix_evaluasi_model.ravel() # ekstrak nilai TP, TN, FP, FN

print("=== Confusion Matrix (TF-Keras) ===")
print(matrix_evaluasi_model)
print(f"TP: {TP}, FP: {FP}, TN: {TN}, FN: {FN}")

#8.visualisasi hasil 
plt.figure(figsize=(15, 5))
plt.title('Visualisasi Hasil', fontsize=16, loc='center')   
# Gambar asli
plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')
# Mask hasil segmentasi
plt.subplot(1, 4, 2)
plt.imshow(mask_pred, cmap='gray')
plt.title('Mask Hasil Segmentasi')
plt.axis('off')
# Mask ground truth
plt.subplot(1, 4, 3)
plt.imshow(mask_gt, cmap='gray')
plt.title('Mask Ground Truth')
plt.axis('off')
# Overlay mask pada gambar asli
plt.subplot(1, 4, 4)
plt.imshow(img, cmap='gray')
plt.imshow(mask_pred, cmap='Blues', alpha=0.5)
plt.title('Hasil Segmentasi pada Gambar Asli')
plt.axis('off')
plt.tight_layout()
plt.show()

iou= TP / (TP + FP + FN)
precision= TP / (TP + FP) 
akurasi= (TP + TN) / (TP + TN + FP + FN)

print ("nilai iou :", iou)
print ("nilai presisi :", precision)
print ("nilai akurasi :", akurasi)