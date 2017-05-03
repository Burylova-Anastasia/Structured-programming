import math
x=0.1
print('x  -  y')
while x<=2.2:
    y=(x**2)-((math.cos(x+1))**2)
    print(round(x,2), '-' , (round(y,2)))
    x+=0.2
