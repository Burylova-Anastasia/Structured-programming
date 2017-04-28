import math
a=int(input("Введите a: "))
t=int(input("Введите t: "))
y=int(input("Введите y: "))
D=(7.8*(a**2)+3.52*t)/(math.log(a+2*y)+math.exp(y))
print(D)
