# tuplas: index -1 é o último item, -2 é o penúltimo, etc 
t = ("apple", "banana", "cherry", True, 40, False, "kiwi", "melon", "mango")
print(t[-1])
print(t[-2])

print(t[:4]) # index 4 é o primeiro a não ser impresso, aquela slice notation

# range of negative indexes
print(t[-4:-1]) # vai imprimir do index -4 até o -1 (não incluso)
                # output: False, 'kiwi', 'melon' - certo
                
# checar se um item existe, usa 'in'
if "apple" in t:
    print("sim, 'apple' está contido na tupla")

print()

# ------------------------------------------------------------------------------

# tuplas são imutáveis: não pode ADICIONAR, MUDAR ou REMOVER itens depois da criação
# gambiarras:

# EDITAR ITENS: converter a tupla para uma lista, mudar a lista, e converter a lista de volta para uma tupla

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x) # output: apple, kiwi, cherry

# ADICIONAR ITENS:
# como tuplas são imutáveis, não tem o método .append()
# 1) converte para uma lista, igual o modo anterior

y = list(x)
y.append("orange")
x = tuple(y)
print(x) # output: apple, kiwi, cherry, orange

# 2) adicionar uma tupla a uma tupla
# cria uma nova tupla com o(s) item(ns) novo(s)
# e adiciona essa nova tupla à tupla já existente

y = ("mango",) # lembra: tupla com 1 item só tem vírgula
x += y
print(x) # output: apple, kiwi, cherry, orange, mango

# REMOVER ITENS
# mesma gambiarra, converte pra lista
y = list(x)
y.remove("apple")
x = tuple(y)
print(x) # output: kiwi, cherry, orange, mango

# DELETAR UMA TUPLA COMPLETAMENTE: keyword del 
del x 
print(x) # erro pq a tupla não existe mais