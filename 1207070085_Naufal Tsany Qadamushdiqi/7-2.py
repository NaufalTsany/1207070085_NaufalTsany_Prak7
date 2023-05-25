# Import library yang digunakan
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/img-doc2.png", 0) # Membaca gambar dan convert ke grayscale

row, column = img.shape # Memberikan variable baru untuk shape kolom dan baris

img1 = np.zeros((row,column),dtype = 'uint8') # Memberikan array kosong
 
min_range = 10 # Memberikan batas minimum slice
max_range = 60 # Memberikan batas maksimum slice

for i in range(row): # Deteksi baris
    for j in range(column): # Deteksi kolom
        if img[i,j]>min_range and img[i,j]<max_range: # Memberikan kondisi if untuk batas minimum dan maksimum
            img1[i,j] = 255 # Memberikan nilai i dan j = 255 jika kondisi if = true
        else:
            img1[i,j] = 0 # Memberikan nilai i dan J = 0 jika kondisi if = false

fig, axes = plt.subplots(2, 2, figsize=(10, 10)) # Membuat subplot
ax = axes.ravel() # Mendeklarasikan axis pada plt

ax[0].imshow(img, cmap=plt.cm.gray) # Membuat subplot 1
ax[0].set_title("Citra Input") # Membuat judul subplot 1
ax[1].hist(img.ravel(), bins=256) # Membuat subplot 2
ax[1].set_title('Histogram Input') # Membuat judul subplot 2

ax[2].imshow(img1, cmap=plt.cm.gray) # Membuat subplot 3
ax[2].set_title("Citra Output") # Membuat judul subplot 3
ax[3].hist(img1.ravel(), bins=256) # Membuat subplot 4
ax[3].set_title('Histogram Output') # Membuat judul subplot 4

# Menampilkan grafik/subplot
fig.tight_layout()
plt.show()