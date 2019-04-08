#           Thales de Castro Soares 86958
import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import misc,stats

def main():
    
    f = misc.imread("lena512.jpg")
    
    f = f.astype(float)
    
    #mascara
    w_size = 5
    
    size = np.shape(f)
    
    w = 1/(float)(w_size*w_size) * np.ones([w_size,w_size])

    #g = np.zeros((2*f.shape[0], 2*f.shape[1]), 'uint8')

    #g = np.zeros((2*size[0], 2*size[1]))
    #g = redimensionar(g,f)
    g = np.zeros(size)
    #plt.imshow(g)

    filtro_media(g,w,w_size,f, size)
    filtro_mediana(f,g,size,w_size)
    filtro_min(f, g, size,w_size)
    filtro_max(f, g, size,w_size)
    filtro_moda(f, g, size,w_size)

###############################################################################

#arrumar...
def filtro_moda(f, g, size,w_size):

    vetor_moda=np.zeros(w_size*w_size)


    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            k = 0
            for u in range(w_size):
                for v in range(w_size):
                    vetor_moda[k] = f[i-(w_size//2)+u,j-(w_size//2)+v]
                    k = k+1
                    
            vetor_moda = sorted(vetor_moda)
            #print(vetor_moda)
            #print(stats.mode(vetor_moda)[0])
            #achar a moda do vetor moda...
            #g[i,j] = vetor_moda[int((w_size*w_size)/2+1)]
            g[i,j] = stats.mode(vetor_moda)[0]
    #plt.show(g)
    cv2.imwrite('imgModa.jpg', g)
    #cv2.imshow('imgModa', g)
    
###############################################################################
#       filtro de minimo
def filtro_min(f, g, size,w_size):

    vetor_min=np.zeros(w_size*w_size)


    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            k = 0
            for u in range(w_size):
                for v in range(w_size):
                    vetor_min[k] = f[i-(w_size//2)+u,j-(w_size//2)+v]
                    k = k+1
                    
            vetor_min = sorted(vetor_min)
            
            #achar a moda do vetor moda...
            #g[i,j] = vetor_min[int((w_size*w_size)/2+1)]
            #pegar o primeiro elemento do vetor...
            g[i,j] = vetor_min[0]
    #plt.show(g)
    cv2.imwrite('imgMin.jpg', g)    
    #cv2.imshow('imgMin', g)
###############################################################################
#       filtro de maximo
def filtro_max(f, g, size,w_size):

    vetor_max=np.zeros(w_size*w_size)
    tam = (w_size*w_size)-1

    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            k = 0
            for u in range(w_size):
                for v in range(w_size):
                    vetor_max[k] = f[i-(w_size//2)+u,j-(w_size//2)+v]
                    k = k+1
                    
            vetor_max = sorted(vetor_max)
            
            #achar a moda do vetor moda...
            #g[i,j] = vetor_max[int((w_size*w_size)/2+1)]
            #pegar o ultimo elemento do vetor...
            g[i,j] = vetor_max[tam]
            
    #plt.show(g)
    cv2.imwrite('imgMax.jpg', g)
    #cv2.imshow('imgMax', g)    

###############################################################################
#       filtro de mediana
def filtro_mediana(f, g, size,w_size):

    vetor_mediana=np.zeros(w_size*w_size)


    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            k = 0
            for u in range(w_size):
                for v in range(w_size):
                    vetor_mediana[k] = f[i-(w_size//2)+u,j-(w_size//2)+v]
                    k = k+1
                    
            vetor_mediana = sorted(vetor_mediana)
            g[i,j] = vetor_mediana[int((w_size*w_size)/2+1)]
    
    #plt.show(g)
    cv2.imwrite('imgMediana.jpg', g)
    #cv2.imshow('imgMediana', g)       
###############################################################################
#               filtro de media...
def filtro_media(g,w,w_size, f, size):
    #g = np.zeros(size)
    
    soma = 0
    
    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            soma = 0
            for u in range(w_size):
                for v in range(w_size):
                    if i>=w_size//2 and j>=w_size//2:
                        soma = soma + f[i-(w_size//2)+u,j-(w_size//2)+v]*w[u,v]
            g[i,j] = soma
            
    #plt.figure(1)
    #plt.subplot(1,2,1)
    #plt.imshow(f, cmap='gray',vmin=0,vmax=255)
    #plt.subplot(1,2,2)
    #plt.imshow(g, cmap='gray',vmin=0,vmax=255)
    cv2.imwrite('imagemMedia.jpg', g)
    #cv2.imshow('imagemMedia', g)
###############################################################################

def redimensionar(img1, img2):
    
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            if(i%2 != 0):
                img1[i+1][j] = img2[i][j]
            elif(j%2 != 0):
                img1[i][j+1] = img2[i][j]
            else:
                img1[i][j] = img2[i][j]
    
    #plt.imshow(img1)
    #cv2.imwrite('img1.jpg', img1)
    return img1
###############################################################################

if __name__ == "__main__":
    main()