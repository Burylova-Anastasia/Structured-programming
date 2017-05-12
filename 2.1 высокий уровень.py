x=float(input("Введите x: "))
y=float(input("Введите y: "))
x=0.1
if(((y<=x-1)or(y>=x+1))and(x*x+y*y<=1)>0):
	print("Точка попадает")
else:print("Точка не попадает")
