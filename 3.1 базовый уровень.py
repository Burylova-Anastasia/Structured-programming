A=float(input("Введите A: "))
N=int(input("Введите N (N>0): "))
s=1
p=1
for i in range(1,N):
    p=p*A
    s=s+p;
print(s);
t=1
for i in range(1,N):
    t=t*A*(-1)
    p=p+t;
print(p)
