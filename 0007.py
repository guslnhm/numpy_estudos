# loop for é intuitivo pra mim
# for t in tuple:
# importante o ':'

# loop por indexes
thistuple = ("don l", "black alien", "flora matos")
for i in range(len(thistuple)):
    print(thistuple[i])

# tem que usar o range e o len juntos, aparentemente. aprender mais sobre os 2
# sobre range na vdd, pq len é o tamanho da tupla

# range()
x = range(6)
for n in x:
    print(n)
print()

# sequência de números, de 0 a 5 nesse caso 
# por padrão incrementa de 1 a 1, pode alterar com step
# pode especificar condição de parada também
# range(start, stop, step)
# observar que start e step são opcionais - stop é obrigatório

x = range(3,6) # começa no 3 e para no 5? CERTO
for n in x:
    print(n)
print()
    
# crie uma sequência de números de 3 a 19, mas incremente de 2 em 2 ao invés de 1 
x = range(3, 20, 2) # CERTO
for n in x:
    print(n)

# + PYTHON BUILT-IN FUNCTIONS https://www.w3schools.com/python/python_ref_functions.asp

# então range(len(tuple)) é um range de 0 até o fim da tupla, não incluso
# o que é justamente o que precisamos para percorrê-la, como um array, de 0 à n-1


# loop while
i = 0 
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1 # PYTHON NÃO TEM i++ wtf
              # mas pd usar i += 1

