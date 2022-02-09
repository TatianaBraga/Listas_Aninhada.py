# 1) Faça uma função que receba, por parâmetro, uma
# matriz quadrada de ordem 3, M, e retorne o determinante dessa matriz: det(M).
'''
import math
def diagonalprincipal(N):
    v = (N[0][0] *N[1][1] * N[2][2]) + (N[0][1] *N[1][2] * N[2][0]) + (N[0][2] *N[1][0] * N[2][1])
    w = (N[0][2] *N[1][1] * N[2][0]) + (N[0][0] *N[1][2] * N[2][1]) + (N[0][1] *N[1][0] * N[2][2])
    return v-w


d = int(input('Dimensão da matriz: '))
X = []
for i in range(d):
    L = []
    for j in range(d):
        a = float(input(f'{i},{j}: '))
        L.append(a)
    X.append(L)
print(X)
z = diagonalprincipal(X)
print(f'Determinante = {z}')
'''
# 2) Faça uma função que receba, por parâmetro, o número de linhas m e o número de colunas n e retorne
# uma matriz A, m×n, com valores inteiros aleatórios
# no intervalo [1, 100].
'''
import random
l = int(input('Linhas: '))  
c = int(input('Colunas: ')) 
X = l*[0]        
for k in range(l):
    X[k] = c*[0] 
for i in range(l):
    for j in range(c):
        X[i][j] = random.randint(10,100)
print(X)


import random  # Resolução correta 
def aletorio(X,m,n):
    for k in range(l):
        X[k] = c*[0]
    for i in range(l):
        for j in range(c):
            X[i][j]  = random.randint(10,100)
    return X

l = int(input('Linhas: '))
c = int(input('Colunas: '))
A = l*[0]
e = aletorio(A,l,c)
print(e)
'''
















