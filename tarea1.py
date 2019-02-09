import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0 , c=1):
    sizea, sizeb = np.shape(image)
    c = c*255;
    out = np.zeros((sizea, sizeb), dtype=np.uint8)
    for x in range(sizea):
        for y in range(sizeb):
            value = image[x][y]
            pixel = c*((value/255) ** gamma)
            if pixel >= 255:
                out[x][y] = 255
            else:
                out[x][y] = pixel
    return out

def seg1(image,A,B,k):
    sizea,sizeb = np.shape(image)
    out = np.zeros((sizea,sizeb),dtype=np.uint8)
    for x in range(sizea):
        for y in range(sizeb):
            if image[x][y] >= A and image[x][y] <= B:
                out[x][y] = k
            else:
                out[x][y] = 0
    return out

def seg2(image,A,B,k):
    sizea, sizeb = np.shape(image)
    out = np.zeros((sizea, sizeb), dtype=np.uint8)
    for x in range(sizea):
        for y in range(sizeb):
            if image[x][y] >= A and image[x][y] <= B:
                out[x][y] = k
            else:
                out[x][y] = image[x][y]
    return out

#-----------------------------------
#           Primer Punto a
#-----------------------------------

img1 = cv2.imread("Test0.tif",0)

gamma = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.05,1.1,1.15,1.2,1.25,1.3]
c = 1
for i in gamma:
    img = adjust_gamma(img1,i,c)
    title = 'Imagen Original(Test0.tif) con gamma = ' + str(i) + ' y c = ' + str(c)
    cv2.imshow(title, img)
    title = 'resultado/'+ title + '.png'
    cv2.imwrite(title, img)

c = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.5,1.8,2,2.2,2.4,2.5,3,4,5]
gamma = 1
for i in c:
    img = adjust_gamma(img1,gamma,i)
    title = 'Imagen Original(Test0.tif) con gamma = ' + str(gamma) + ' y c = ' + str(i)
    cv2.imshow(title, img)
    title = 'resultado/'+ title + '.png'
    cv2.imwrite(title, img)


#-----------------------------------
#           Primer Punto b
#-----------------------------------

c = [2.13,0.88,1.15]
gamma = [0.8,3,0.65]

for i in range(3):
    root = "Test"+str(i+1)+".tif"
    img = cv2.imread(root,0)
    img = adjust_gamma(img,gamma[i],c[i])
    title = 'Imagen Original(Test' +str(i+1)+ '.tif) con gamma = ' + str(gamma[i]) + ' y c = ' + str(c[i])
    cv2.imshow(title, img)
    title = 'resultado/'+ title + '.png'
    cv2.imwrite(title, img)

#-----------------------------------
#           Segundo Punto
#-----------------------------------

img5 = cv2.imread("Test4.tif",0)

img5_1 = seg1(img5,72,98,255)
img5_2 = seg2(img5,72,98,255)

cv2.imshow('Imagen (Test4.tif)',img5)
cv2.imwrite('resultado/Imagen (Test4.tif).png',img5)

cv2.imshow('Imagen (Test4.tif) con segmentacion1 entre 72 y 98',img5_1)
cv2.imwrite('resultado/Imagen (Test4.tif) con segmentacion1 entre 72 y 98.png',img5_1)

cv2.imshow('Imagen (Test4.tif) con segmentacion2 entre 72 y 98',img5_2)
cv2.imwrite('resultado/Imagen (Test4.tif) con segmentacion2 entre 72 y 98.png',img5_2)

cv2.waitKey(0)
cv2.destroyAllWindows()

