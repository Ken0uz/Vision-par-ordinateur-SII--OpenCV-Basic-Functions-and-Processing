import math
import numpy as np

def gauss(x, y, sigma):
    """
    Calcule la valeur d'une gaussienne en 2D en un point (x, y) donné.

    Args:
        x: Coordonnée x du point.
        y: Coordonnée y du point.
        sigma: Écart-type de la gaussienne.

    Returns:
        La valeur de la gaussienne au point (x, y).
    """
    # Partie de normalisation
    part1 = 1 / (2 * math.pi * sigma**2)
    # Partie exponentielle
    part2 = (x**2 + y**2) / (2 * sigma**2)
    return part1 * math.exp(-part2)


"""def print_gauss(sigma=1.4, vois_mat=5):
    vois=int(vois_mat/2)
    x,y=0.0
    som=0.0
    for i in range(-vois,vois+1):
        for j in range(-vois,vois+1):
            val=gauss(i,j,sigma)
            val=round(val*185,0)
            print('{:02.2f}'.format(val),'\t',end="")
            som +=val
        print(' ')
    print('somme;',som)
print_gauss()"""
#changer la fonction pour retourner la matrice de convolution

def get_gauss_matrix(sigma=1.4, vois_mat=5):    #sigma contrôle la largeur de la gaussienne :
                                                # plus sigma est grand, plus la gaussienne est large et plus le lissage sera important.
    """
    Crée une matrice de convolution gaussienne.

    Args:
        sigma: Écart-type de la gaussienne.
        vois_mat: Taille de la matrice (doit être impaire).

    Returns:
        Une matrice NumPy représentant le filtre gaussien.
    """
    vois = vois_mat // 2
    gauss_matrix = []
    for i in range(-vois, vois + 1):
        row = []
        for j in range(-vois, vois + 1):
            # Calcul de la valeur gaussienne en (i, j)
            val = gauss(i, j, sigma)
            # Scaling arbitraire (à comprendre)
            val = round(val * 185, 0)
            row.append(val)
        gauss_matrix.append(row)
    return np.array(gauss_matrix)

# Création de la matrice de convolution
gauss_matrix = get_gauss_matrix()
print("Matrice de convolution gaussienne :\n", gauss_matrix)
print("Somme des éléments :", np.sum(gauss_matrix))



""" Matrice de convolution:
Chaque élément de la matrice représente un poids qui sera utilisé pour calculer la nouvelle valeur d'un pixel en combinant linéairement les valeurs des pixels voisins.
Les pixels proches du centre auront un poids plus important que ceux éloignés, ce qui a pour effet de lisser l'image. """