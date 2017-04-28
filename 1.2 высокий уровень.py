import math
a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите c: "))
D=(b**2)-4*a*c
if (D<0):print("Корней нет")
elif (D==0):
    x=(-b+math.sqrt(D))/2*a;print(x)
elif (D>0):
    x1=(-b+math.sqrt(D))/2*a;print(x1)
    x2=(-b-math.sqrt(D))/2*a;print(x2)
