import math
x=int(input("Введите x: "))
y=int(input("Введите y: "))
z=int(input("Введите z: "))
c=int(input("Введите c: "))
G=(math.tan((x**4)-6)-(math.cos(z+(x*y))**3))/((math.cos(x**3)**4)*(c**2))
print(G)
