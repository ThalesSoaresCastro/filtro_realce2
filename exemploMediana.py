#Exemplo - Filtro Mediana

f = misc.imread("lena512.jpg")

f_noisy = f

X = np.random.rand(size[0],size[1])

f_noisy[X<=0.025] = 0
for i in range(size[0]):
    for j in range(size[1]):
        if 0.025<X[i,j]<=0.05:
            f_noisy[i,j]=255
plt.imshow(f_noisy,cmap='gray')

g = np.zeros(size)

w_size = 3

vetor_mediana = np.zeros(w_size*w_size)

for i in range(size[0]-w_size//2):
    for j in range(size[1]-w_size//2):
        soma = 0
        k = 0
        for u in range(w_size):
            for v in range(w_size):
                vetor_mediana[k] = f[i-(w_size//2)+u,j-(w_size//2)+v]
                k = k+1
        vetor_mediana = sorted(vetor_mediana)
        g[i,j] = vetor_mediana[(w_size*w_size)/2+1]

plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(f, cmap='gray',vmin=0,vmax=255)
plt.subplot(1,2,2)
plt.imshow(g, cmap='gray',vmin=0,vmax=255)