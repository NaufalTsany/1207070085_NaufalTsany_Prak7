import matplotlib.pyplot as plt
import cv2
import numpy as np

citra1 = cv2.imread("image/dodo.jfif", 0) # Membaca gambar1 dan convert ke grayscale
citra2 = cv2.imread("image/messi.jfif", 0) # Membaca gambar2 dan convert ke grayscale

print('Shape citra 1 : ', citra1.shape) # Menampilkan ukuran gambar1
print('Shape citra 2 : ', citra2.shape) # Menampilkan ukuran gambar2

fig, axes = plt.subplots(1, 2, figsize=(10, 10)) # Membuat subplot
ax = axes.ravel() # Mendeklarasikan axis pada plt

ax[0].imshow(citra1, cmap = 'gray') # Membuat subplot 1
ax[0].set_title("Citra 1") # Membuat judul subplot 1
ax[1].imshow(citra2, cmap = 'gray') # Membuat subplot 2
ax[1].set_title("Citra 2") # Membuat judul subplot 2

# Menampilkan grafik/subplot
fig.tight_layout()
plt.show()

copyCitra1 = citra1.copy().astype(float)
copyCitra2 = citra2.copy().astype(float)

m1,n1 = copyCitra1.shape # Memberikan variable baru untuk shape kolom dan baris gambar1
output1 = np.empty([m1, n1]) # Memberikan array kosong gambar1

m2,n2 = copyCitra2.shape # Memberikan variable baru untuk shape kolom dan baris gambar2
output2 = np.empty([m2, n2]) # Memberikan array kosong gambar2
print('Shape copy citra 1 : ', copyCitra1.shape) # Menampilkan ukuran copy gambar1
print('Shape output citra 1 : ', output1.shape) # Menampilkan ukuran output gambar1

print('m1 : ',m1) # Menampilkan ukuran baris gambar 1
print('n1 : ',n1) # Menampilkan ukuran kolom gambar 1
print() # Menampilkan baris kosong

print('Shape copy citra 2 : ', copyCitra2.shape) # Menampilkan ukuran copy gambar2
print('Shape output citra 3 : ', output2.shape) # Menampilkan ukuran output gambar1
print('m2 : ',m2) # Menampilkan ukuran baris gambar 2
print('n2 : ',n2) # Menampilkan ukuran kolom gambar 2
print() # Menampilkan baris kosong

for baris in range(0, m1-1): # Membaca baris pada matrix gambar1
    for kolom in range(0, n1-1): # Membaca kolom pada matrix gambar1
        a1 = baris # Mendklarasikan variable baris gambar1
        b1 = kolom # Mendklarasikan variable kolom gambar1
        # Perhitungan jumlah piksel sekitar pada citra yang disimpan dalam variabel arr
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        
        minPiksel = np.amin(arr); # Membuat batas minimum citra pada variable arr      
        maksPiksel = np.amax(arr); # Membuat batas maksimum citra pada variable arr    

        # Membuat kondisi untuk batas minimum dan maksimum    
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
        else :
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]

for baris1 in range(0, m2-1): # Membaca baris pada matrix gambar1
    for kolom1 in range(0, n2-1): # Membaca kolom pada matrix gambar1
        a1 = baris1 # Mendklarasikan variable baris gambar1
        b1 = kolom1 # Mendklarasikan variable kolom gambar1
        # Perhitungan jumlah piksel sekitar pada citra yang disimpan dalam variabel arr
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        minPiksel = np.amin(arr); # Membuat batas minimum citra pada variable arr        
        maksPiksel = np.amax(arr); # Membuat batas maksimum citra pada variable arr    

        # Membuat kondisi untuk batas minimum dan maksimum    
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]

fig, axes = plt.subplots(2, 2, figsize=(10, 10)) # Membuat subplot
ax = axes.ravel() # Mendeklarasikan axis pada plt

ax[0].imshow(citra1, cmap = 'gray') # Membuat subplot 1
ax[0].set_title("Input Citra 1") # Membuat judul subplot 1

ax[1].imshow(citra2, cmap = 'gray') # Membuat subplot 2
ax[1].set_title("Input Citra 1") # Membuat judul subplot 2

ax[2].imshow(output1, cmap = 'gray') # Membuat subplot 3
ax[2].set_title("Output Citra 1") # Membuat judul subplot 3

ax[3].imshow(output2, cmap = 'gray') # Membuat subplot 4
ax[3].set_title("Output Citra 2") # Membuat judul subplot 4

# Menampilkan grafik/subplot
fig.tight_layout()
plt.show()