# Exercise 1 Создать переменную типа String.
a = 'string'
print(type(a))
# Exercise 2 Создать переменную типа Integer.
b = 21
print(type(b))
# Exercise 3 Создать переменную типа Float.
c = 2.1
print(type(c))
# Exercise 4 Создать переменную типа Bytes.
d = 'байты'.encode('utf-8')
print(type(d))
# Exercise 5 Создать переменную типа List.
e = [1, 2, 'three']
print(type(e))
# Exercise 6 Создать переменную типа Tuple.
f = ('one', 'two', 'three', 4)
print(type(f))
# Exercise 7 Создать переменную типа Set.
g = {'a', 1, 'b', 2}
print(type(g))
# Exercise 8 Создать переменную типа Frozen set.
k = frozenset('object')
print(type(k))
# Exercise 9 Создать переменную типа Dict.
m = {'a': 1, 'b': 2}
print(type(m))
# Exercise 10 Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, '=', type(a))
print(b, '=', type(b))
print(c, '=', type(c))
print(d, '=', type(d))
print(e, '=', type(e))
print(f, '=', type(f))
print(g, '=', type(g))
print(k, '=', type(k))
print(m, '=', type(m))
# Exercise 11 Создать 2 переменные String, создать переменную в которой сконкатенируете эти переменные.
# Вывести в консоль.
first = 'Michajlasheva'
last = ' street'
address = first + last
print(address)
# Exercise 12 Вывести в одну строку переменные типа String и Integer используя “,” (Запятую).
a = 'one'
b = 1
print(a, ",", b, sep="")
print(a, ",", 1, sep="")
print(a, b, sep=",")
print(a, 1, sep=",")
print(f"{a},{b}")
print(f"{a},1")
# Exercise 13 Вывести в одну строку переменные типа String и Integer используя “+” (Плюс).
a = 'one'
b = 1
print(a, "+", b, sep="")
print(a, "+", 1, sep="")
print(a, b, sep="+")
print(a, 1, sep="+")
print(f"{a}+{b}")
print(f"{a}+1")
