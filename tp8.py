import cv2
import numpy as np
import time

cap = cv2.VideoCapture("output_out.avi")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc('X','Y','I','D')
out = cv2.VideoWriter("output_out1.avi",fourcc,34,(frame_width,frame_height)) #fps

if not cap.isOpened():
    print("error capture")
    exit(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    t_start = time.time()
    if not ret :
        print("error end frame")
        break
    frame = cv2.flip(frame,1)
    out.write(frame)
    cv2.imshow("image",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    print("time",1/(time.time()- t_start))  # nombre d'images par secondes 'temps d'echantillonage'

out.release()
cap.release()
cv2.destroyAllWindows()   