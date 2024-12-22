import cv2
import numpy as np

# Charger l'image en niveaux de gris
img = cv2.imread("group 1.jpg", cv2.IMREAD_GRAYSCALE)

# Calculer le gradient en X et Y sans boucle ni fonctions prédéfinies
grad_x = img[:, 1:] - img[:, :-1]         # Différence finie en X
grad_y = img[1:, :] - img[:-1, :]         # Différence finie en Y

# Adapter les dimensions pour correspondre a l'image originale genre pour assurer qu'ils ont la meme taille
grad_x = np.pad(grad_x, ((0, 0), (0, 1)), mode='constant', constant_values=0)   #(0,1) Ajout d'une colonne de zeros uniquement à droite de grad_x
grad_y = np.pad(grad_y, ((0, 1), (0, 0)), mode='constant', constant_values=0)   # en bas

# Calculer l'amplitude du gradient
grad_img = np.sqrt(grad_x**2 + grad_y**2).astype(np.uint8)

# Paramètres globaux pour le seuil et le type de seuillage
th = 100
type_th = 0

def afficher():
    # Initialiser une image de résultat vide
    imgRes = np.zeros_like(grad_img)
    
    # Appliquer les conditions de seuillage en fonction de `type_th`
    sup_th = grad_img > th
    inf_th = np.invert(sup_th)  # Inverser pour les valeurs inférieures au seuil

    if type_th == 0:  # THRESH_BINARY
        imgRes[sup_th] = 255
        imgRes[inf_th] = 0
    elif type_th == 1:  # THRESH_BINARY_INV
        imgRes[sup_th] = 0
        imgRes[inf_th] = 255
    elif type_th == 2:  # THRESH_TRUNC
        imgRes[sup_th] = th
        imgRes[inf_th] = grad_img[inf_th]
    elif type_th == 3:  # THRESH_TOZERO
        imgRes[sup_th] = grad_img[sup_th]
        imgRes[inf_th] = 0
    elif type_th == 4:  # THRESH_TOZERO_INV
        imgRes[sup_th] = 0
        imgRes[inf_th] = grad_img[inf_th]
    
    cv2.imshow("img", imgRes)

print (grad_img.max())

def change_th(x):
    global th
    th = x
    afficher()

def change_type(x):
    global type_th
    type_th = x
    afficher()


# il faut changer le type de donnees puis faire une normalisation
# Afficher l'image avec le seuillage initial
afficher()


# Créer les trackbars pour ajuster le seuil et le type de seuillage
cv2.createTrackbar("thresh", "img", 0, 255, change_th)   # 255 est la valeur max pour le seuil
cv2.createTrackbar("type", "img", 0, 4, change_type)     # Pour choisir entre les 5 types de seuillage
cv2.waitKey(0)
cv2.destroyAllWindows()
