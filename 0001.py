import numpy as np 
a = np.array([6,1,9,9,3,2,9,7,8,0,4])

            # 0 1 2 3 4 5 6 7 8 9 10
           # 11 d 9 8 7 6 5 4 3 2 1   (-)
             
#print(a.size)

print(a[:4]) # do index 0 até o index 3 (4 não conta); output: 6 1 9 9
print(a[-3:-1]) # começando do index -3 até o index -2 (-1 é o primeiro a não ser considerado)
                # output: 8 0
                
# STEPS

print(a[::2]) # terceiro parâmetro - steps, no exemplo, vai de 2 em 2
                # de 0 até o final; output: 6 9 3 9 8 4
                # esse é o exemplo para imprimir every other

# from the second element, slice elements from index 1 to 4 (not included)
arr = np.array([
        [1,2,3,4,5],
        [6,7,8,9,10]
    ])

print(arr[1, 1:4]) # que notação é essa mds
                   # ah sim, é pq é uma matriz 2d
                   # do segundo elemento, slice do index 1 até o 4 (não incluso)
                   
print(arr[0, 3]) # elemento 0, dentro dele pego o elemento de index 3
                 # output: 4
                 
# from both elements, return index 2
print(arr[0, 2])
print(arr[1, 2])

# resposta dele:
print(arr[0:2, 2]) # elementos de 0 até 1 (2 é o primeiro a não ser considerado)
                   # vírgula
                   # index 2
                   # carai btf

# from both elements, slice index 1 to index 4 (not included)
print(arr[0:2, 1:4]) # certo!

'''
como imprimir tamanho de um array numpy?
.size
.shape dá tipo (3,2) para uma matrix 3x2
'''