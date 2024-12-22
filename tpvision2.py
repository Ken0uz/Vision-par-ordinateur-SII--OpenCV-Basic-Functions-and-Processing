import cv2
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)

if img is None:
    print("erreur de chargement")
    exit(0)

imgNorm = np.zeros((img.shape),np.uint8)

h,w = img.shape
min = 255
max = 0

for y in range(h):
    for x in range (w):
       if(img[y,x] > max):
           max = img[y,x]
       if(img[y,x] < min):
           min = img[y,x]    

for y in range(h): 
    for x in range (w):
        imgNorm[y,x]=(img[y,x] - min) * 255 / (max - min) 

print("min :",min,"max :",max)

cv2.imshow("Image avant",img)
cv2.imshow("image apres",imgNorm)

# histogrammes
hist_avant = np.zeros((256,1),np.uint16)

for y in range(h):
    for x in range (w):
        hist_avant[img[y,x],0] += 1
        
hits_apers=cv2.calcHist([imgNorm],[0],None,[256],[0,255])

plt.figure()
plt.title("image normalisée")
plt.xlabel("NG")
plt.ylabel("NG_pixel")
plt.plot(hist_avant)
plt.plot(hits_apers)
plt.xlim([0,255])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
