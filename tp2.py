import cv2
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread("group 2.jpg",cv2.IMREAD_GRAYSCALE)
#img[:] = img[:]/2  #pour preparer une image sombre
if img is None:
    print("erreur de chargement")
    exit(0)

#initialisation de l'image normalisee
imgNorm = np.zeros(img.shape,np.uint8)   # 0 a 255  on divise sur 2^nbBit -1

h,w = img.shape   # recupere la hauteur et la largeur de l'image
min = 255
max = 0

for y in range(h):
    for x in range (w):
       if(img[y,x] > max):
           max = img[y,x]
       if(img[y,x] < min):
           min = img[y,x]    


# normalisation des pixels
""" (img[y, x] - min) : Décale les valeurs de pixel pour que le minimum soit 0.
* 255 / (max - min) : Échelle les valeurs pour que le maximum soit 255. """
for y in range(h): 
    for x in range (w):
        imgNorm[y,x]=(img[y,x] - min) * 255 / (max - min) # c'est quoi la diff entre mettre la multi a la fin et au debut ( par rapport au noir)

print("min :",min,"max :",max)

cv2.imshow("Image avant",img)
cv2.imshow("image apres",imgNorm)
cv2.waitKey()   # puisqu'on l'utilise pour enlever les images on tape sur une touche clavier pas sur x rouge 

# histogrammes
hist_avant = np.zeros((256,1),np.uint16)  #uint16 parce que c'est le nombre de pixels non vas les valeurs des pixels (ca depends de la taille de l'image) 
# il y a 256 niveaux de gris possibles 

for y in range(h):
    for x in range (w):
        hist_avant[img[y,x],0] += 1  #on incremente la valeur a chaque fois qu'on trouve un pixel de la valeur correspondante genre te7seb
        
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
