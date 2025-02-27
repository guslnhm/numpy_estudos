import numpy as np 

# shape de um array: tupla com a quantidade de elementos em cada dimensão

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape) # output: (2,4)
                 # primeira dimensão tem 2 elementos e a segunda tem 4
                 # ij, linha coluna

arr = np.array([1,2,3,4], ndmin=5) # .ndim especifica qtas dimensões vai ter nesse array 
print(arr)
print(arr.shape) # output: 1, 1, 1, 1, 4
# última dimensão tem 4 elementos
print()

# ------------------------------------------------------------------------------

# reshape: mudar o shape de um array, podemos adicionar/remover/mudar o nº de elementos em cada dimensão

# reshape de 1d para 2d

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3) # 4 linhas 3 colunas? certo
print(newarr) # 4 arrays, cada um com 3 elementos

# reshape de 1d pra 3d

newarr = arr.reshape(2,3,2) # 2 matrizes, cada qual com 1 matriz de 3x2 (3 linhas, 2 colunas)
print(newarr) # certo

# podemos fazer reshape para qualquer shape, desde que os elementos sejam iguais em ambos os shapes
# 2*3*2 = 12, q é a qtd de elementos do array original

# exemplo, array 1d de 8 elementos pode virar uma array 2d de 2x4 e 4x2?
print()

arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(4,2)
print(newarr)
newarr = arr.reshape(2,4)
print(newarr)

# sim! array 1d de 8 elementos pode virar array 2d 4x2 ou 2x4

# mas não pode virar, por ex, uma array 2d 3x3, pq isso requere 9 elementos
# observe o erro:
# newarr = arr.reshape(3,3) #erro
print()

arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3).base)
# retorna o array original (1,2,3,4,5,6)
# então é uma view (?) view é o array original, does not own the data
# mudanças na view afetam array original, e vice-versa
# então mudanças no reshape afetam array original?

print()

array = np.array([1,2,3,4,5,6])
newarr = array.reshape(2,3)
print(newarr)
newarr[1,2] = 4
print(newarr)
print(array)
# SIM! MUDANÇA NO RESHAPE AFETA ARRAY ORIGINAL 
# deve ser bem útil na vdd

print()

# é possível ter UMA dimensão desconhecida
# você não precisa especificar um número exato de uma das dimensões no método reshape
# passa -1 como o valor, numpy calcula o valor
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
newarr = arr.reshape(3,-1)
print(newarr.shape) # output: 3,3
print(newarr)
# não pode passar -1 para mais do que uma dimensão

# FLATTENING THE ARRAYS - converter um array multidimensional para um array 1d
# usamos reshape(-1)
print()
print(newarr)
newarr = newarr.reshape(-1)
print(newarr)
print(newarr.ndim) # output: 1

# outras funções para mudar shapes de arrays no numpy:
# flatten, ravel
# rearranjar os elementos: rot90, flip, fliplr, flipud, etc
