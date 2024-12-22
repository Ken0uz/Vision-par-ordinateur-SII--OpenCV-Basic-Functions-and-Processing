import cv2
import numpy as np

img_color = cv2.imread(r'photos/cat.jpg', cv2.IMREAD_COLOR)

# 2. Vwrifier si le chargement s'est fait correctement
if img_color is None:
    print("Erreur: L'image couleur n'a pas pu être chargée.")
    exit(0)

#h,w,c = img_color.shape
#img_Res = np.zeros((h,w,c),np.uint8)
#img_Res = np.zeros(img_color.shape,np.uint8)
img_Res = np.zeros(img_color.shape,np.float32)  #float 16 n'est pas supportee par imshow  # pourquoi utiliser float32
#img_Res = np.zeros(img_color.shape,np.float64)
""" for y in range(h):
    for x in range(w):
        img_Res[y,x,0] = 255 - img_color[y,x,0]
        img_Res[y,x,1] = 255 - img_color[y,x,1]
        img_Res[y,x,2] = 255 - img_color[y,x,2] 

        img_Res[y,x,:] = 255 - img_color[y,x,:] """
#img_Res[:,:,:] = 255 - img_color[:,:,:]
img_Res = 255 - img_color
#img_Res = img_Res * 256 
#img_Res = img_Res/1.
img_Res = img_Res/255.      

cv2.imshow("image",img_color)
cv2.imshow("image2",img_Res)  # le fait de multiplier il change le type directement a 16 ( avant il etait 8 puisqueon lui a affecte les vals de img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# readaptation des valeurs genre changer l'intervalle des valeurs , le type des valeurs mais c'est pas un changement de valeurs donc l'image ne change pas , parce qu'on fait une normalisation donc litteralement ls valeu sont les memes