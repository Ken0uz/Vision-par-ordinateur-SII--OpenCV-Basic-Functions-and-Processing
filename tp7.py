import cv2
import numpy as np

image_path = r'C:\M2\vision\photos\park.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
img_b=np.zeros(img.shape,img.dtype)
img_g=np.zeros(img.shape,img.dtype)
img_r=np.zeros(img.shape,img.dtype)

h,w,c = img.shape
for y in range(h):
    for x in range(w):
        img_b[y,x,0]=img[y,x,0]
        img_g[y,x,1]=img[y,x,1]
        img_r[y,x,2]=img[y,x,2]
#un code avec le probleme de type dans l'examen
#pour remplacer les deux boucles precedantes
#img_b[:, :, 0], img_g[:, :, 1], img_r[:, :, 2] = img[:, :, 0], img[:, :, 1], img[:, :, 2]
#convertion d'une image de RGB en niveau de gris sans utiliser de fonction predifinies
#on prend juste la derniere dimenseion
#img_gray=(img_b[...,0]*0.33+img_g[...,1]0.33+img_r[...,2]*0.33)/3. 
#img_gray=np.int8(img_b[...,0]/3+img_g[...,1]/3+img_r[...,2])/3 
img_gray=(np.float16(img_b[...,0])+np.float16(img_g[...,1])+np.float16(img_r[...,2]))/3 
img_gray=np.uint8(img_gray)#imshow n'affiche pas floeat
#changer l'image initial comme  de types float 32 divier sur 255
img_float32=np.float32(img)/255
img_uint16=np.uint16(img_float32*(2**16-1))
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
"""cv2.imshow("image",img)
cv2.imshow("image",img_gray)
cv2.imshow("image green",img_g)
cv2.imshow("image bleu",img_b)
cv2.imshow("image red",img_r)"""
cv2.imshow("image hsv ",img_hsv)#hsv juste pour le calcul seulement avec m'afichage de imshow  il fait utiliser bgr
cv2.imshow("image floeat32",img_float32)
cv2.imshow("image unit16",img_uint16)
cv2.waitKey(0)
cv2.destroyAllWindows()