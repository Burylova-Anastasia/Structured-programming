s=str(input("Введите строку: "))
n='!'
r=''
for i in range(len(s)):
    if s[i]==n:
       r+=str(i)
    else:
        r+=s[i]
print(r)
