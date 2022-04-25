f = open('zadanie24_2.txt').readline()
k = 1
m = 0
for i in range(len(f)-1):
    if f[i] == 'D' and f[i+1] == 'D':
        k += 1
        m = max(m, k)
    else: k = 1
print(m)