#le probleme de RVB la couleur et l'intensite sont raparees et representees simultanement avec la luminance
import cv2
import numpy as np

image_path = r'C:\M2\vision\photos\park.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
img_b=np.zeros(img.shape,img.dtype)
img_g=np.zeros(img.shape,img.dtype)
img_r=np.zeros(img.shape,img.dtype)

h,w,c = img.shape  #c ici est 0 pour B , 1 pour G et 2 pour R , h et w sont les dimensions 
""" for y in range(h):
    for x in range(w):
        img_b[y,x,0]=img[y,x,0]
        img_g[y,x,1]=img[y,x,1]
        img_r[y,x,2]=img[y,x,2] """

img_b[:, :, 0], img_g[:, :, 1], img_r[:, :, 2] = img[:, :, 0], img[:, :, 1], img[:, :, 2]
#img_gray=(img_b[...,0]+img_g[...,1]+img_r[...,2])/(3*255)  # les trois points pour les autres dimensions ( les ignorer) a part la derniere ou j'ai mit 0 1 2
#img_gray=(img_b+img_g+img_r)/(3*255) # le type est float entre 0 et 1
img_gray=np.uint8((np.float32(img_b[...,0])+np.float32(img_g[...,1])+np.float32(img_r[...,2]))/3)  # si on somme directement les trois images en 255 on aura une image qui depasse 255 donc quand on force a etre en uint8 donc on perds des infos de l'image on peut soit diviser soit forcer a le changer le type en float
""" img_gray=(np.float32(img_b[...,0])+np.float32(img_g[...,1])+np.float32(img_r[...,2]))/3
img_gray=img_gray/255 """

#si le type est float on divise sur 255 soit on garde le type de int8 

#si on utilise un seul canal elle sera consideree comme une image en niveau de gris donc on cree des images en 3 canaux et on affiche juste le rouge / bleu ou veut dependant de ce qu'on veut

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_float32=np.float32(img)/255
img_flt= np.float32(img/255)
img_uint16=np.uint16(img_float32*(2**16-1))

cv2.imshow("image B", img_b)
cv2.imshow("image G", img_g)
cv2.imshow("image R", img_r)
cv2.imshow("image Gris", img_gray)
cv2.imshow("image float", img_float32)
cv2.imshow("image flt", img_flt)
cv2.imshow("image int", img_uint16)
cv2.imshow("image Gris", img_hsv)   #avec imshow et ainsi : img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) on ne peut pas afficher en image en hsv parce que meme si les dimensions sont les memes et tout parce que il prends h comme b ,s comme g , et v comme r directement d'ou l'affichage d'une image m3ewqa pour l'affichage on utilise juste le BGR et hsv pour les traitement calculs et tt
cv2.waitKey(0)
cv2.destroyAllWindows()