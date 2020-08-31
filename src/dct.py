""""
    Discrete Cosine Transform Implementation
"""

import math
import numpy as np

def ccons(_a):
    if(_a==0): return 1.0/math.sqrt(2.0)
    else: return 1

def dct(data):
    #   get dimension
    M,N = data.shape
    #   calculate DCT
    F = np.zeros((M,N))
    c = 2/math.sqrt(M * N)
    for u in range(M):
        for v in range(N):
            sum = 0
            for i in range(M):
                for j in range(N):
                    sum += ccons(u)*ccons(v)*math.cos((math.pi*u)*(2*i+1)/(2*M))*math.cos((math.pi*v)*(2*j+1)/(2*N))*data[i][j]
            F[u][v] = c*sum
    return F

def idct(data):
    #   get dimension
    M,N = data.shape

    F = np.zeros(shape=(M,N))
    
    
    #   calculate IDCT
    c = 2/math.sqrt(M * N)
    for u in range(M):
        for v in range(N):
            sum = 0
            for i in range(M):
                for j in range(N):
                    sum += ccons(u)*ccons(v)*math.cos((math.pi*u)*(2*i+1)/(2*M))*math.cos((math.pi*v)*(2*j+1)/(2*N))*data[i][j]
            F[u][v] = c*sum

    return F





if __name__=="__main__":
    print("Main program DCT")
    #   define data
    data = np.zeros(shape=(2,2))
    data[0] = [90,100]
    data[1] = [100,105]

    #   process data
    
else:
    print("DCT module")