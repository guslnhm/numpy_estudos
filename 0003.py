import numpy as np 

# copy - novo array
    # logo, mudanças feitas na cópia NÃO AFETAM O ARRAY ORIGINAL, e vice-versa
    # copy OWNS THE DATA
    
# view - visualização do array original
    # logo, quaisuqer mudanças feitas na view vão afetar o array original, e vice-versa
    # view DOESN'T OWN THE DATA
    
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr) # 42 2 3 4 5
print(x) # 1 2 3 4 5
print()

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr) # 42 2 3 4 5
print(x) # 42 3 4 5
print()

arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 49
print(arr) # 49 2 3 4 5 - mudança na view afetou array original
print()

# atributo .base checa se o array é dono/possui (own) os dados ou não
# retorna 'None' se o array possui os dados

arr = np.array([1,2,3,4,5])
x = arr.copy() # owns the data
y = arr.view() # doesnt own the data
print(x.base) # output: None
print(y.base) #output: 1 2 3 4 5