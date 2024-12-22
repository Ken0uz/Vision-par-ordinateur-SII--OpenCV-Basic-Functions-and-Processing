# Binarisation & seuillage  
# il y a plusieurs algos de seuillage   

# type de seuillage est une constante THRESH_BINARY = 0 # s'il est inferieur au seuil ywelli blanc sinon noir   
# seuillage inverse c'est le contraire  THRESH_BINARY_INV = 1
# THRESH_TRUNC = 2 si > = seuil sinon on garde la mm valeur srx(x,y)
# THRESH_TOZERO = 3 SI > Src sinon = 0
#THRESH_TOZERO = 4 contraire du dernier

#Trackbar est une fonction createTrackbar creer un objet graphique (pointeur) pour changer une valeur donnee d'une variable

import cv2
import numpy as np
img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

th = 0
type_th = 0
def afficher():
    #th = 128
    imgRes = np.zeros_like(img)
    #grad_x = img[:,:img.shape[1]-1] - img[:,1:]  #exemple de comment calculer grad de X
    """ sup_th_bool = img > th
    imgRes[sup_th_bool] = 255 """
    sup_th = img > th
    inf_th = np.invert(sup_th)  # donc si la val= vrai mettre faux , si faux inverser aussi

    """ if(type_th == 0):
        #imgRes [img>th] = 255
        imgRes [sup_th] = 255
        #imgRes[img<=th] = 0
        imgRes[inf_th] = 0
    elif(type_th == 1):
        imgRes[sup_th] = 0
        imgRes[inf_th] = 255
    elif(type_th == 2):
        imgRes[sup_th] = th
        imgRes[inf_th] = img [inf_th]
    elif(type_th == 3):
        imgRes[sup_th] = img [sup_th]
        imgRes[inf_th] = 0
    elif(type_th == 4):
        imgRes[sup_th] = 0
        imgRes[inf_th] = img[inf_th] """
    cv2.threshold(img,th,255,type_th,imgRes)
    cv2.imshow("img",imgRes)
    #cv2.imshow("img",img)
def change_th(x):
    global th
    th= x
    afficher()

def change_type(x):
    global type_th
    type_th = x
    afficher()
afficher()

cv2.createTrackbar("thresh", "img",0,255,change_th)   # 255 est la valeur max
cv2.createTrackbar("type","img",0,4,change_type)
cv2.waitKey(0)
cv2.destroyAllWindows()


# devoir : realiser le meme travail sur  une image en niveau de gris , lui appliquer le gradient par rapport a X ( la difference par rapport a X) et par rapport a Y ( la difference par rapport a Y) ensuite faire la racine des carres et appliquer le seuillage sur l'image gradient
# sans boucle ni fonctions predefinis ( avec calcul matriciel)



