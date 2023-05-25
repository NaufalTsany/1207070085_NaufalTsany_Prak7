# Import library yang digunakan
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("image/img-doc2.png", 0) # Membaca gambar dan convert ke grayscale
image_equalized = cv2.equalizeHist(img) # Menambahkan histogram

# Membuat objek CLAHE dengan batas keterbatasan kontras sebesar 2 dan ukuran grid tile 8x8
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))
# Mengaplikasikan CLAHE ke gambar asli
image_clahe = clahe.apply(img)

# Membuat array kosong untuk gambar
image_cs = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')

min = np.min(img) # Minimum contrass
max = np.max(img) # Maksimum contrass

for i in range(img.shape[0]): # Deteksi baris
    for j in range(img.shape[1]): # Deteksi kolom
        image_cs[i,j] = 255*(img[i,j]-min)/(max-min) # Melakukan contrass stretching

copyCamera = img.copy().astype(float)

m1,n1 = copyCamera.shape # Memberikan variable baru untuk shape kolom dan baris
output1 = np.empty([m1, n1]) # Memberikan array kosong

for baris in range(0, m1-1): # Membaca baris pada matrix
    for kolom in range(0, n1-1): # Membaca kolom pada matrix
        a1 = baris # Mendklarasikan variable baris
        b1 = kolom # Mendeklarasikan variable kolom
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9 # Dikalikan dengan nilai konstanta

fig, axes = plt.subplots(5, 2, figsize=(10, 10)) # Membuat subplot
ax = axes.ravel() # Mendeklarasikan axis pada plt

ax[0].imshow(img, cmap=plt.cm.gray) # Membuat subplot 1
ax[0].set_title("Citra Input") # Membuat judul subplot 1
ax[1].hist(img.ravel(), bins=256) # Membuat subplot 2
ax[1].set_title('Histogram Input') # Membuat judul subplot 2

ax[2].imshow(image_equalized, cmap=plt.cm.gray) # Membuat subplot 3
ax[2].set_title("Citra Output HE") # Membuat judul subplot 3
ax[3].hist(image_equalized.ravel(), bins=256) # Membuat subplot 4
ax[3].set_title('Histogram Output HE Method') # Membuat judul subplot 4

ax[4].imshow(image_cs, cmap=plt.cm.gray) # Membuat subplot 5
ax[4].set_title("Citra Output CS") # Membuat judul subplot 5
ax[5].hist(image_cs.ravel(), bins=256) # Membuat subplot 6
ax[5].set_title('Histogram Output CS Method') # Membuat judul subplot 6

ax[6].imshow(image_clahe, cmap=plt.cm.gray) # Membuat subplot 7
ax[6].set_title("Citra Grayscale CLAHE") # Membuat judul subplot 7
ax[7].hist(image_clahe.ravel(), bins=256) # Membuat subplot 8
ax[7].set_title('Histogram Output CLAHE Method') # Membuat judul subplot 8

ax[8].imshow(output1, cmap=plt.cm.gray) # Membuat subplot 9
ax[8].set_title("Citra Grayscale Perkalian Konstanta") # Membuat judul subplot 9
ax[9].hist(output1.ravel(), bins=256) # Membuat subplot 10
ax[9].set_title('Histogram Output Perkalian Konstanta Method') # Membuat judul subplot 10

# Menampilkan grafik/subplot
fig.tight_layout()
plt.show()