x = "Hello World" #str
print(type(x))
x = 1 + 2 + 3
print(type(x))
a = 5
b = 2
tmp = a
a = b
b = tmp
print(a, b, tmp)
x = y = z = 0 #каскадное присваивание
print(x, y, z)
# множественное присваивание
x, y, z = 1, 2, 3
print(x, y, z)
a, b = 1, 2
a, b = b, a
print(a, b)
x = 5
y = 3
z = 2
print(x ** y ** z)
print(2/3)
x = 5
y = 2
print(x // y) #div
print(x % y) #mod
x = 0
counter = 0
while x < 5 :
    counter += 1
    x += 1
    print(x, counter)



