tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)
print()
# operador + une duas ou mais tuplas

# operador * multiplica o conteúdo de uma tupla um determinado número de vezes
fruits = ("apple", "banana", "cherry")
mytuple = fruits*2 
print(mytuple) # output: apple, banana, cherry, apple, banana, cherry
print()

# MÉTODOS DE TUPLA - count() e index()
# apenas esses 2 built-in aparentemente

# count() - retorna a qtd de vezes que um valor específico ocorre numa tupla
print(mytuple.count("cherry")) # output: 2 

# index() - procura na tupla por um valor específico e retorna a posição onde foi achado
print(fruits.index("banana")) # output: 1 (index 1)
print(mytuple.index("apple")) # output: 0 (aparece primeiro no index 0, então não conta valores duplicados)