# pack a tuple: atribuir valores à tupla

fruits = ("cherry", "mango", "grapefruit")

# para extrair esses valores, colocando-os em variáveis
# o processo se chama UNPACKING

(green, yellow, red) = fruits

print(green) # output: cherry
print(yellow) # output: mango
print(red) # output: grapefruit

# o número de variáveis deve ser igual ao número de valores na tupla
# caso contrário, usa asterisco para coletar os valores restantes numa LISTA - *??
# !!!!!! IMPORTANTE: LISTA = [], exemplo, ['apple', 'banana', 'cherry']

fruits2 = ("strawberry", "blueberry", "raspberry", "apple", "pineapple")

(green, yellow, *red) = fruits2

print(green) # output: strawberry
print(yellow) # output: blueberry
print(red) # output: raspberry, apple, pineapple

# coleta os valores restantes num formato de lista []

# se os asteriscos forem adicionados a uma variável que não a última, python coloca +
# os valores nessa variável como lista, até que a quantidade de valores restantes na tupla
# sejam iguais à quantidade de variáveis livres restantes

print()

(blue, *pink, purple) = fruits2
print(blue) # output: strawberry
print(pink) # output: blueberry, raspberry, apple
print(purple) # output: pineapple
    # certo