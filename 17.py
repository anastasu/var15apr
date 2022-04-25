
f = open('17-2.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))
k = 0
m = 0
for i in range(len(a)-1):
    if (a[i]%5==0 or a[i+1]%5==0) and (a[i]+a[i+1])%7==0:
        k+=1
        if (a[i]+a[i+1])>m:
            m=a[i]+a[i+1]
print(k, m)