import math
import numpy as np

def gauss(x,y,sigma):
    part1= 1/(2*math.pi*pow(sigma,2))
    part2= -(x*x+y*y)/(2*pow(sigma,2))
    return part1 * math.pow(math.e,part2)

def print_gauss(sigma = 1.4, vois_mat=3):
    vois = int(vois_mat/2)
    x,y = 0,0
    som = 0.0
    for i in range(-vois, vois+1):
        for j in range(-vois, vois+1):
            val = gauss(i,j,sigma)
            val = round( val*185,0)
            print('{:02.2f}'.format)