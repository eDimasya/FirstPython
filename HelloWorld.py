i = "Hello World" #str
print(type(i))
i = 1 + 2 + 3
print(type(i))
a = 5
b = 2
tmp = a
a = b
b = tmp
print(a, b, tmp)
i = y = z = 0 #каскадное присваивание
print(i, y, z)
# множественное присваивание
i, y, z = 1, 2, 3
print(i, y, z)
a, b = 1, 2
a, b = b, a
print(a, b)
i = 5
y = 3
z = 2
print(i ** y ** z)
print(2/3)
i = 5
y = 2
print(i // y) #div
print(i % y) #mod
i = 0
counter = 0
while i < 5 :
    counter += 1
    i += 1
    print(i, counter)



