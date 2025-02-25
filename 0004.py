import numpy as np 

# shape: retorna uma tupla *?

# tuplas - armazenar multiplos itens numa unica variavel
# uma dos 4 tipos de dados em python para armazenar coleções de dados 
# LISTS, SET, DICTIONARY, TUPLES

# !!!!!!!!!!!!
# TUPLAS IMUTÁVEIS - NÃO SE PODE EDITAR, ADICIONAR OU REMOVER ITENS DEPOIS QUE A TUPLA FOI CRIADA

t = ("apple", "banana", "cherry")
print(t) # output: ('apple', 'banana', 'cherry')

# tuplas - ORDENDAS E IMUTÁVEIS (UNCHANGEABLE)
    # ordem não muda!
# round brackets - parênteses
# permite valores duplicados
# itens são indexados, começando pelo index [0]

print(t[0]) # output: apple

print(len(t)) # len() determina quantos itens a tupla tem

# criando tupla com um item apenas: tem que colocar uma vírgula, se não python não entende que é tupla 

t2 = ("apple",)
print(type(t2)) # output: <class: 'tuple'>

t3 = ("apple")
print(type(t3)) # output: <class 'str'>

# IMPORTANTE! TUPLAS PODEM CONTER DIFERENTES TIPOS DE DADOS 
    # heterogêneos?

print()
t4 = ("apple", True, 34, "cherry", 40, False)
for t in t4:
    print(type(t)) # imprime str, bool, int, str, int, bool

# tb é possível usar o construtor tuple() pra criar uma tupla 

t5 = tuple(("apple", 2, "banana"))
print(t5)

# ESTUDAR COLEÇÕES DE DADOS EM PYTHON (ARRAYS): LISTS, SETS, TUPLE, DICTIONARY