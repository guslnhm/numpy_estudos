import numpy as np 

arr = np.array([1,2,3,4])
print(arr.dtype) # .dtype retorna o tipo dos dados do array

arr = np.array(["a", "b", "c"])
print(arr.dtype) # retornando U1, U6 ou U25, dependendo do que eu coloco
                 # ?

arr = np.array([1,2,3,4], dtype='S') # transforma os dados em String - é maiúsculo o 'S'!
print(arr.dtype)
print(arr)
# CUIDADO, aqui transforma em byte literal, por isso imprime b'1', etc *
# pra transformar em string, usa dtype='U' ou dtype='str'

arr = np.array([1,2,3,4], dtype='f')
print(arr.dtype)
print(arr)

arr = np.array([1,2,3,4], dtype='U')
print(arr.dtype)
print(arr)

arr = np.array([1,2,3,4], dtype='i4')
print(arr.dtype)
print(arr)

#arr = np.array(['a', '2', '3'], dtype='i') # erro, não tem como transformar 'a' em int

# astype() - cria uma cópia de um array já existente, e muda o dtype
print()
arr = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
print(arr)
print(arr.dtype)
newarr = arr.astype(int) # também posso passar 'i' como argumento, funciona igual
print(newarr)
print(newarr.dtype)
print()

arr = np.array([0,1,3])
newarr = arr.astype(bool)
print(newarr) # output: false false true true
print(newarr.dtype)