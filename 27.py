f = open('27_A.txt')
n = int(f.readline())
a = [int(s) for s in f]
m = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % 43==0 and s>m:
            m=s
print(m)