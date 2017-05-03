N=int(input("Введите N: "))
i=1
while i<=N:
    g=i
    s=0
    while g>0:
        s=s+g%10
        g=int(g/10)
    if ((i%5!=0)and(i%3==0)and((s%5!=0)and(s%3==0))):
        print(i)
    i=i+1
