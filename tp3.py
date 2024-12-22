import cv2
import numpy as np


vois = 3

def filtreMoy(img): 
    h,w= img.shape 
    imgMoy = np.zeros(img.shape,np.uint8)

    for y in range(h):
        for x in range(w):
            if y< vois/2 or x>(w-vois/2) or y > (h-vois/2) or x< vois/2:
                imgMoy[y,x]= img[y,x]
            else:
                imgVois = img[int(y-vois/2):int(y+vois/2)+1,int(x-vois/2):int(x+vois/2)+1] #moy = 0 #for yv in range(voisinage): # for xv in range(voisinage): moy += imgV[yv, xv] #moy / voisinage*voisinage imgMoy [y,x]= np.mean(imgV) #
                moy = 0
                for yv in range(imgVois.shape[0]):
                    for xv in range(imgVois.shape[1]):
                        moy += imgVois[yv,xv]
                moy /= vois*vois
                imgMoy[y,x] = moy
                imgMoy[y,x] = np.mean(imgVois)
    return imgMoy


img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
imgMoy = filtreMoy(img)
cv2.imshow("image source",img)
cv2.imshow("image moyenne", imgMoy)
cv2.waitKey(0)
cv2.destroyAllWindows()

