for i in range(1,1000):
    x=i
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x%100)
        x = x//100
    if (a ==2) and (b==5) :
        print(i)