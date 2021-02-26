a = []
b = a
print(a)
print(b)
print(id(a))
print(id(b))
a = []
b = []
print(a)
print(b)
print(id(a))
print(id(b))

a = 8597
b = 8597

print(id(a))
print(id(b))

a = 8599

print(id(a))
print(id(b))

a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

print(id(a))
print(id(b))