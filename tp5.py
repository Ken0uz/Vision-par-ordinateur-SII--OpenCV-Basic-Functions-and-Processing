import cv2
import numpy as np

# Charger l'image en niveaux de gris
img = cv2.imread("group 2.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])/16  #Gauss pour eliminer le bruit  ( il la rend floue)
#kernel2 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])  #Laplacien pour detecter les contours
#kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])    # laplacien + noyau
#kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])  # un noyau qui garde l'image telle qu'elle est

""" 0 -1 0
    -1 0 1
    0 1 0 """  #celui la calcule le pixel suivant- le precedent de X et Y ( graident de X et Y)


# c'est deconseillee d'appliquer gauss puis laplacien
imgRes = cv2.filter2D(img,-1,kernel)
#imgRes = cv2.filter2D(imgRes,-1,kernel2)
cv2.normalize(imgRes,imgRes,0,255,cv2.NORM_MINMAX)  # on doit calculer toujours le min et max parce que la normalisation prends en parametres 0 min et 255 max comme dans cette exemple par exemple ( on doit verifier le type de l'image resultante)

cv2.imshow("image", img)
cv2.imshow("img", imgRes)
cv2.waitKey()
cv2.destroyAllWindows()

#l'image initiale + laplacien nous donne les contours = image initiale + contours
# un noyau de convolution ou on a partout des 0 a part 1 dans le noyau il garde l'image initiale  + laplacien  on va obtenir une image initiale avec contours