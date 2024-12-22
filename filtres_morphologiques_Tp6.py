import cv2
import numpy as np


DelateSize = 1
ErodeSize = 1
MorphSize = 1

cv2.namedWindow("erosion")
cv2.namedWindow("dilatation")
cv2.namedWindow("morph")

img = cv2.imread("group 1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.threshold(img,128,255,0,img)

""" cv2.namedWindow("Erosion")
cv2.namedWindow("Dilatation") """


def morph_func():
    size = MorphSize*2+1
    #kernel = np.ones((sizeDelate,sizeDelate),np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size,size))
    #image_morph = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel,iterations=1)
    image_morph = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations=1)
    cv2.imshow("morph",image_morph)


def delate_func():
    #kernel = np.ones((sizeDelate,sizeDelate),np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(DelateSize*2+1,DelateSize*2+1))
    image_delate = cv2.dilate(img,kernel,iterations=1)
    cv2.imshow("dilatation",image_delate)




def erode_func():
    size = ErodeSize*2+1
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size,size))
    image_erode = cv2.erode(img,kernel,iterations=1)
    cv2.imshow("erosion",image_erode)

def changeErodeSize(x):
    global ErodeSize
    ErodeSize = x 
    #print(erodeSize)
    erode_func()

def changeDilateSize(x):
    global DelateSize
    DelateSize = x 
    #print(erodeSize)
    delate_func()


def changeMorphSize(x):
    global MorphSize
    MorphSize = x 
    #print(erodeSize)
    morph_func()







cv2.createTrackbar("sizeErode","erosion",0,11,changeErodeSize)
cv2.createTrackbar("sizeDelate","dilatation",0,11,changeDilateSize)
cv2.createTrackbar("sizeMorph","morph",0,11,changeMorphSize)

erode_func()
delate_func()
morph_func()

cv2.imshow("image_init",img)
cv2.waitKey(0)
cv2.destroyAllWindows()