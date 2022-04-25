a=[]
def F(n):

    if n > 0:
        print ("*")
        F(n - 1)
        F(n // 3)
        a.append("*")

print (F(6))
print (len(a))

