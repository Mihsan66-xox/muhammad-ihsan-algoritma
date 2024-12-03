# Operasi logika boolean

# not, or, and

# NOT

print("===NOT===")
a = False
c = not a
print("print data a", "=", a)
print("..............NOT")
print("print data c", "=", c)

# OR - Jika Salah Satu Bernilai TRUE maka hasill = TRUE

a = False
b = False
c = a or b
print(a, "or", b, "=", c)
a = False
b = True
c = a or b
print(a, "or", b, "=", c)
a = True
b = False
c = a or b
print(a, "or", b, "=", c)
a = True
b = True
c = a or b
print(a, "or", b, "=", c)

# AND - Jika Salah Satu Bernilai FALSE maka hasill = FALSE
a = False
b = False
c = a and b
print(a, "and", b, "=", c)
a = False
b = True
c = a and b
print(a, "and", b, "=", c)
a = True
b = False
c = a and b
print(a, "and", b, "=", c)
a = True
b = True
c = a and b
print(a, "and", b, "=", c)


