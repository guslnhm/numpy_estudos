import numpy as np 

# arrays 2d: normalmente representam matrizes ou 2nd order tensors
# numpy tem submódulo dedicado a operações de matrizes, chamado numpy.mat

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)
print()

# arrays 3d: um array que tem matrizes (arrays 2d) como seus elementos
# normalmente representam 3rd order tensor

arr3 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ], 
    [
        [1,2,3],
        [4,5,6]
    ]
])
print(arr3)
print()

# .ndim - atributo que retorna um int que é o número de dimensões que o array tem
print(arr.ndim) # output: 2, tem 2 dimensões 
print(arr3.ndim) # output: 3, tem 3 dimensões
print()

# .ndmin - definir o número de dimensões de um array na sua criação
arr_new = np.array([1,2,3,4], ndmin=5)
print(arr_new) # output: [[[[[1,2,3,4]]]]]
print(arr_new.ndim) # output: 5

# 5 dimensões: o elemento mais interno (quinta dimensão) tem 4 elementos
# a quarta dimensão tem 1 elemento que é esse vetor de 4 elementos
# a terceira dimensão tem um elemento que é a matriz com o vetor ??
# a segunda dimensão tem 1 elemento que é o array 3d 
# e a primeira dimensão tem 1 elemento que é o array 4d