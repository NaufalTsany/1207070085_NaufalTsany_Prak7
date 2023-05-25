# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("image/img-doc2.png") # Membaca gambar dengan OpenCV

imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Mengubah format citra dari BGR menjadi RGB menggunakan fungsi cv2.cvtColor.

plt.imshow(imgrgb)
plt.title("Gambar Awal")
plt.axis("off")
plt.show()
# Menampilkan gambar awal (citra RGB) tanpa filter menggunakan plt.imshow, dengan judul "Gambar Awal" dan sumbu (axis) yang tidak ditampilkan.

kernel = np.ones((5,5),np.float32)/25
print(kernel)
# Membuat filter dengan matriks berukuran 5x5 yang berisi nilai 1 dan kemudian membaginya dengan 25. Nilai filter ini akan digunakan dalam operasi filtering.

img_filter = cv2.filter2D(img,-1,kernel)
# Melakukan operasi filtering pada citra asli (img) menggunakan filter yang telah dibuat sebelumnya (kernel)

plt.imshow(img_filter)
plt.title("Gambar Setelah Filtering")
plt.axis("off")
plt.show()
# Menampilkan citra setelah proses filtering menggunakan plt.imshow, dengan judul "Gambar Setelah Filtering" dan sumbu (axis) yang tidak ditampilkan.

data = np.random.normal(size=1000)

plt.rcParams["figure.figsize"] = (10,10)
# Mengatur ukuran plot 

plt.subplot(221), plt.imshow(imgrgb)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222)
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')


plt.subplot(223), plt.imshow(img_filter)
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(224)
hist_data = img_filter.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Setelah Filtering')

plt.suptitle('Gambar dan Histogram')
plt.show()

img_blur = cv2.blur(img,(5,5))
plt.imshow(img_blur)
# Melakukan operasi blurring pada citra asli (img) menggunakan cv2.blur dengan kernel 

kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)
# Membuat kernel dengan menggunakan np.matrix dengan matriks berukuran 3x3 yang memiliki pola tertentu, dan kemudian membaginya dengan 25. Nilai kernel ini akan digunakan dalam operasi filtering.

img_filter = cv2.filter2D(img,-1,kernel)

plt.imshow(img_filter)
plt.show()
# Melakukan operasi filtering pada citra asli (img) menggunakan kernel


# Highpass Filter

img = cv2.imread("image/img-doc2.png", 0)  # Membaca citra dan convert to greyscale

laplacian = cv2.Laplacian(img, cv2.CV_64F)  # Menerapkan algoritma high-pass filtering menggunakan operator Laplacian pada citra grayscale (`img`). Hasilnya disimpan dalam variabel `laplacian`.

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# Menerapkan algoritma high-pass filtering menggunakan operator Sobel pada citra grayscale (`img`). Operator Sobel digunakan untuk mendeteksi tepi vertikal (dalam `sobelx`) dan tepi horizontal (dalam `sobely`) pada citra. Kedua hasilnya disimpan dalam variabel `sobelx` dan `sobely`.

plt.rcParams["figure.figsize"] = (10, 10)  # Mengatur ukuran plot menjadi 20x20 untuk tampilan yang lebih besar.

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.figure(figsize=(10, 5))
plt.subplot(121)
hist_data = img.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram (Original)')

plt.subplot(122)
hist_data = laplacian.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram (Laplacian)')

plt.show()


img = cv2.imread("image/img-doc2.png", 0) # Membaca citra dan convert to greyscale

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
# Menampilkan citra asli dan citra hasil deteksi tepi menggunakan `plt.subplot`. Citra asli ditampilkan pada subplot pertama dengan judul "Original Image", sedangkan citra hasil deteksi tepi ditampilkan pada subplot kedua dengan judul "Edge Image". Sumbu x dan y tidak ditampilkan.


img = cv2.imread("image/img-doc2.png",0) # Membaca citra dan convert to greyscale

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# Melakukan thresholding pada citra grayscale (`img`) dengan nilai threshold 127. Hasilnya disimpan dalam variabel `thresh1`, `thresh2`, `thresh3`, `thresh4`, dan `thresh5` sesuai dengan jenis thresholding yang digunakan.

titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# Menyimpan judul dan citra hasil thresholding dalam bentuk list untuk keperluan plotting.

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# Menampilkan citra-citra hasil thresholding dalam satu plot menggunakan `plt.subplot`. Citra asli ditampilkan pada subplot pertama, sedangkan citra hasil thresholding ditampilkan pada subplot-subplot berikutnya sesuai dengan urutan yang telah ditentukan. Setiap subplot diberi judul dan sumbu x dan y tidak ditampilkan.

img = cv2.medianBlur(img,5) # Menggunakan median blur pada citra grayscale (`img`) dengan ukuran kernel 5. Hal ini dilakukan untuk menghaluskan tepi objek pada citra sebelum melakukan thresholding.

# Lakukan Thresholding
# Binary Threshold
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Melakukan thresholding binary menggunakan fungsi threshold dari OpenCV dengan nilai threshold 127.

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode mean menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode Gaussian menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
# Membuat list judul 'titles' yang akan digunakan untuk memberikan judul pada setiap gambar yang akan ditampilkan. Membuat list 'images' yang berisi citra asli dan hasil thresholding.

# menampilkan hasil
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# Melakukan iterasi untuk menampilkan gambar-gambar secara berurutan. Mengatur tata letak subplot dengan 2 baris dan 2 kolom. Menampilkan gambar pada subplot yang sesuai, memberikan judul menggunakan 'titles', dan menghilangkan label sumbu x dan y.

plt.tight_layout()
plt.show()
# Mengatur tata letak subplot agar lebih rapi dan menampilkan plot.

# Membuat histogram dari gambar asli
plt.subplot(2, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram Gambar asli')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Membuat histogram dari gambar setelah di filter
for i in range(1, 4):
    plt.subplot(2, 2, i + 1)
    plt.hist(images[i].ravel(), 256, [0, 256])
    plt.title('Histogram ' + titles[i])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
# Menampilkan citra-citra hasil thresholding dalam satu plot menggunakan `plt.subplot`. Citra asli ditampilkan pada subplot pert
